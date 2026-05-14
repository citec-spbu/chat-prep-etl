import logging
import re
from typing import List
import numpy as np

from testing_system.internal.domain.entities import MetricValue, Question, Answer, MetricType
from testing_system.internal.domain.value_objects import RetrievedDocument

logger = logging.getLogger(__name__)

class Eval:
    """
    The measurer of the experiment
    Takes metrics names, available:
    - latency
    - token_count
    - bert_score
    - exact_match
    - jaccard_distance
    - rouge_l_f1
    - hallucination_rate
    - numeric_accuracy
    - overlap
    and the encoder-model parameter for debug version

    The evaluation method 'execute'
    input: Question, Answer
    output: List[MetricValue] 

    check all the entities in the
    testing_system/internal/domain/entities.py
    """
    
    def __init__(self, 
                 metrics: List[str], 
                 bert_model: str = "bert-base-multilingual-cased",
                 hallucination_model: str = None,
                 ):
        self.metric_evaluators = []
        self.device = "cpu"
        self.model_path = bert_model
        if hallucination_model:
            self.hallucination_model = hallucination_model
        else:
            self.hallucination_model = bert_model
        for i in range(len(metrics)):
            match metrics[i]:
                case "latency":
                    self.metric_evaluators.append(self._latency)
                case "token_count":
                    self.metric_evaluators.append(self._token_count)
                case "bert_score":
                    try:
                        from bert_score import BERTScorer
                    except ModuleNotFoundError as e:
                        logger.error("Please install bert_score module. Command: pip install bert-score")
                        continue
                    try:
                        import torch
                    except ModuleNotFoundError as e:
                        logger.error("Please install torch module. Command: pip install torch")
                        continue
                    if torch.cuda.is_available():
                        self.device = "cuda"
                    elif torch.backends.mps.is_available():
                        self.device = "mps"
                    else:
                        self.device = "cpu"
                    self.bert_scorer = BERTScorer(
                        model_type=self.model_path,
                        lang="ru",
                        rescale_with_baseline=False,
                        device=self.device,
                    )
                    self.metric_evaluators.append(self._bert_score)
                case "exact_match":
                    self.metric_evaluators.append(self._exact_match)
                case "jaccard_distance":
                    import nltk
                    nltk.download('stopwords')
                    self.metric_evaluators.append(self._jaccard_distance)
                case "rouge_l_f1":
                    self.metric_evaluators.append(self._rouge_l_f1)
                case "hallucination_rate":
                    self.metric_evaluators.append(self._hallucination_rate)
                    try:
                        from deepeval.models.hallucination_model import (
                            HallucinationModel,
                        )
                        import sentence_transformers
                        logger.debug("Loading h model")
                        from transformers import AutoModel, AutoTokenizer
                        AutoTokenizer.from_pretrained(self.hallucination_model, trust_remote_code=True)
                        AutoModel.from_pretrained(self.hallucination_model, trust_remote_code=True)
                    except ImportError as e:
                        logger.error(
                            f"Vectera Hallucination detection model can not be loaded.\n{e}"
                        )
                        continue
                    self.hallucination_scorer = HallucinationModel(model_name=self.hallucination_model)
                case "numeric_accuracy":
                    self.metric_evaluators.append(self._numeric_accuracy)
                case "overlap":
                    self.metric_evaluators.append(self._overlap)

    def _latency(self, q: Question, a: Answer) -> MetricValue:
        """
        Calculate latency (the time to get answer) for one Q and A.
        Args:
            q (Question): A question to compare with (ground_true is in it)
            a (Answer): An answer to evaluate
        Returns:
            MetricValue - Latency
        """
        return MetricValue(
                type = MetricType.LATENCY,
                value = a.latency_ms,
                metadata=None
            )
    def _token_count(self, q: Question, a: Answer) -> MetricValue:
        """
        Calculate count of tokens used in answer for one Q and A.
        Args:
            q (Question): A question
            a (Answer): An answer to evaluate
        Returns:
            MetricValue - An amount of tokens
        """
        return MetricValue(
                type = MetricType.TOKEN_COUNT,
                value = a.token_count,
                metadata=None
            )
    def _bert_score(self, q: Question, a: Answer) -> MetricValue:
        """
        Calculate BERTScore for one Q and A using a specified BERT model.
        Args:
            q (Question): A question to compare with (ground_true is in it)
            a (Answer): An answer to evaluate
        Returns:
            MetricValue - BERT_score f1 with precision and recall in metadata
        Note:
            Before using this function, make sure to install the 'bert_score' module by running the following command:
            ```
            pip install bert-score
            ```
        """
        if isinstance(a.text, str):
            predictions = [a.text]
        else:
            logger.error(f"answer is not str: {type(a.text)}")
            return MetricValue(
                type=MetricType.INVALID,
                value = 0.0,
                matadata = None
            )
        if isinstance(q.ground_true, str):
            references = [q.ground_true]
        else:
            logger.error(f"ground_true is not str: {type(q.ground_true)}")
            return MetricValue(
                type=MetricType.INVALID,
                value = 0.0,
                matadata = None
            )
        if not self.bert_scorer:
            return MetricValue(
                type=MetricType.INVALID,
                value = 0.0,
                matadata = None
            )
        precision, recall, f1 = self.bert_scorer.score(
            cands=predictions, refs=references
        )
        return MetricValue(
            type = MetricType.BERT_SCORE,
            value = f1.detach().numpy().tolist()[0],
            metadata={
                "recall" : recall.detach().numpy().tolist()[0],
                "precision": precision.detach().numpy().tolist()[0]
            }
        )
    def _exact_match(self, q: Question, a: Answer) -> MetricValue:
        """
        Indicates if the answer is equal to ground true.
        Args:
            q (Question): A question to compare with (ground_true is in it)
            a (Answer): An answer to evaluate
        Returns:
            MetricValue - Exact match (0 or 1)
        """
        return MetricValue(
                type = MetricType.EXACT_MATCH,
                value = float(q.ground_true.strip() == a.text.strip()),
                metadata=None
            )
    def _jaccard_distance(self, q: Question, a: Answer) -> MetricValue:
        """
        Jaccard distance (1 - |intersection|/|union|) between two texts (stemming is used).
        Args:
            q (Question): A question
            a (Answer): An answer to evaluate
        Returns:
            MetricValue - The Jaccard distance between stemmed Q and A (the lower - the better)
        """        
        try:
            import string
            from nltk.stem import SnowballStemmer
            from nltk.corpus import stopwords
            def clean_stem_text(text: str) -> str:
                text = text.lower()
                punct = string.punctuation + '«»—…'
                text = text.translate(str.maketrans('', '', punct))
                text = re.sub(r'\s+', ' ', text).strip()
                tokens = text.split() if text else []
                return [stemmer.stem(tok) for tok in tokens if tok]
            stemmer = SnowballStemmer("russian")
            stop_words = set(stopwords.words('russian'))
            ref_tokens = clean_stem_text(q.ground_true)
            gen_tokens = clean_stem_text(a.text)
            
            set_ref = set([t for t in ref_tokens if t not in stop_words])
            set_gen = set([t for t in gen_tokens if t not in stop_words])
            
            if not set_ref and not set_gen:
                return 0.0
            if not set_ref or not set_gen:
                return 1.0
            
            intersection = len(set_ref & set_gen)
            union = len(set_ref | set_gen)
            return MetricValue(
                type = MetricType.JACCARD,
                value=1 - (intersection / union),
                metadata=None
            )
        except Exception as e:
            logger.error(f"jaccard failed: {e}")
            return MetricValue(
                type = MetricType.INVALID,
                value=1.0,
                metadata=None
            )
    def _rouge_l_f1(self, q: Question, a: Answer) -> MetricValue:
        """
        Calculate latency (the time to get answer) for one Q and A.
        Args:
            q (Question): A question to compare with (ground_true is in it)
            a (Answer): An answer to evaluate
        Returns:
            MetricValue - Rouge_l_f1 with precision and recall in metadata
        """
        try:
            from rouge_score import rouge_scorer
        except Exception as e:
            logger.error(f"rouge failed: {e}")
            return MetricValue(
                type=MetricType.INVALID,
                value = -1.0,
                matadata = None
            )
        scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=True)
        scores = scorer.score(q.ground_true, a.text)
        return MetricValue(
            type = MetricType.ROUGE_L_F1,
            value = scores["rougeL"].fmeasure,
            metadata={
                "recall": scores["rougeL"].recall,
                "precision": scores["rougeL"].precision
                }
        )
    def _hallucination_rate(self, q: Question, a: Answer) -> MetricValue:
        """Calculate the hallucination score of a prediction compared to a source text.
        This method computes a hallucination score, which measures the extent to which a generated prediction contains hallucinations.
        The score is based on the Vectara Hallucination Evaluation Model.
        Args:
            q (Question): The source document where the information is summarized from.
            a (Answer): The generated summary that is validated against the source summary.

        Returns:
            MetricValue - The computed hallucination score. Lower values indicate greater hallucination.
        """
        if isinstance(a.retrieved_context, list):
            source = '\n'.join([d.content for d in a.retrieved_context])
        else:
            logger.error(f"retrieved documents are not in list: {type(a.retrieved_context)}")
            return MetricValue(
                type=MetricType.INVALID,
                value = 0,
                matadata = None
            )
        if self.hallucination_scorer:
            score = self.hallucination_scorer.model.predict([(source, a.text)])[0]
            if isinstance(score, np.ndarray) and len(score) == 3:
                hallucination_index = float(score[2]) - float(score[0]) 
                e_x = np.exp(score - np.max(score))
                score = e_x / e_x.sum(axis=0)
                contradictory_index = float(score[2])
                entailment_index = float(score[0])
                score = hallucination_index
                metadata={
                    "contradictory_index": contradictory_index,
                    "entailment_index": entailment_index
                }
            elif isinstance(score, np.ndarray):
                score = float(score[0])
            return MetricValue(
                type = MetricType.HALLUCINATION_RATE,
                value = score,
                metadata=metadata
            )
        else:
            logger.error("hallucination model not found")
            return MetricValue(
                type=MetricType.INVALID,
                value=0.0,
                metadata=None
            )
    def _numeric_accuracy(self, q: Question, a: Answer) -> MetricValue:
        """
        Calculate accuracy of number-generation for one Q and A.
        Numbers are called "equal to each other", if our system could recognize the equal pattern
        during preprocessing (not ideal).
        Args:
            q (Question): A question to compare with (ground_true is in it)
            a (Answer): An answer to evaluate
        Returns:
            MetricValue - Numeric accuracy
        """
        _RU_NUMS = {
            "ноль": "0", "один": "1", "два": "2", "три": "3", "четыре": "4",
            "пять": "5", "шесть": "6", "семь": "7", "восемь": "8",
            "девять": "9", "десять": "10", "одиннадцать": "11",
            "двенадцать": "12", "тринадцать": "13", "четырнадцать": "14",
            "пятнадцать": "15", "шестнадцать": "16", "семнадцать": "17",
            "восемнадцать": "18", "девятнадцать": "19", "двадцать": "20",
            "тридцать": "30", "сорок": "40", "пятьдесят": "50",
            "шестьдесят": "60", "семьдесят": "70", "восемьдесят": "80",
            "девяносто": "90", "сто": "100", "двести": "200",
            "триста": "300", "четыреста": "400", "пятьсот": "500",
            "шестьсот": "600", "семьсот": "700", "восемьсот": "800",
            "девятьсот": "900", "тысяча": "1000", "тысячи": "000",
            "тысяч": "000"
        }
        pred_text = ' '.join([_RU_NUMS.get(i, i) for i in a.text.lower().split(' ')])
        ref_text = ' '.join([_RU_NUMS.get(i, i) for i in q.ground_true.lower().split(' ')])
        pred_numbers = set(re.findall(r'-?\d+/\d+|-?\d+\.\d+|-?\d+', pred_text))
        ref_numbers = set(re.findall(r'-?\d+/\d+|-?\d+\.\d+|-?\d+', ref_text))
        if not ref_numbers:  
            return MetricValue(
                type = MetricType.NUMERIC_ACCURACY,
                value = 1.0,
                metadata=None
            )
        if not pred_numbers:
            return MetricValue(
                type = MetricType.NUMERIC_ACCURACY,
                value = 0.0,
                metadata=None
            )
        intersection = pred_numbers.intersection(ref_numbers)
        return MetricValue(
            type = MetricType.NUMERIC_ACCURACY,
            value = len(intersection) / len(ref_numbers),
            metadata=None
        )
    def _overlap(self, q: Question, a: Answer) -> MetricValue:
        """
        There are 3 overlap metrics:
        - overlap_recall: the proportion of ethalon tokens in answer
        - overlap_precision: the proportion of given tokens to ethalon's
        - overlap_symmetric: the intersection divided by minimum size (as a metric default value)
        Args:
            q (Question): A question to compare with (ground_true is in it)
            a (Answer): An answer to evaluate
        Returns:
            MetricValue - Overlap f1 with precision and recall in metadata
        """
        pred_tokens = set(re.findall(r'\w+', a.text.lower()))
        ref_tokens = set(re.findall(r'\w+', q.ground_true.lower()))
        
        intersection = pred_tokens.intersection(ref_tokens)
        inter_size = len(intersection)
        
        recall = inter_size / len(ref_tokens) if ref_tokens else (1.0 if not pred_tokens else 0.0)
        precision = inter_size / len(pred_tokens) if pred_tokens else (1.0 if not ref_tokens else 0.0)
        
        if not pred_tokens and not ref_tokens:
            symmetric = 1.0
        elif not pred_tokens or not ref_tokens:
            symmetric = 0.0
        else:
            symmetric = inter_size / min(len(pred_tokens), len(ref_tokens))
        
        return MetricValue(
            type = MetricType.OVERLAP,
            value = symmetric,
            metadata={
                "recall": recall,
                "precision": precision,
            }
        )
    
    def execute(self, q: Question, a: Answer) -> List[MetricValue]:
        metrics = []

        for metric_evaluator in self.metric_evaluators:
            metrics.append(metric_evaluator(q,a))

        return metrics
