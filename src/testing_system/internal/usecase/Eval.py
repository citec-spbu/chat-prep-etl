from typing import List
from testing_system.internal.domain.entities import MetricValue, Question, Answer, MetricType
import torch
from sentence_transformers import SentenceTransformer
from rouge_score import rouge_scorer

class Eval:
    """
    The measurer of the experiment
    Takes metrics names, available:
    - latency
    - token_count
    - bert_score
    - exact_match
    - rouge_l_f1
    - hallucination_rate (notImplemented)
    and the model for debug version

    The evaluation method 'execute'
    input: Question, Answer
    output: List[MetricValue] 

    check all the entities in the
    testing_system/internal/domain/entities.py
    """
    
    def __init__(self, metrics: List[str], model):
        self.metric_evaluators = []
        self.encoder = None
        for i in range(len(metrics)):
            match metrics[i]:
                case "latency":
                    self.metric_evaluators.append(self._latency)
                case "token_count":
                    self.metric_evaluators.append(self._token_count)
                case "bert_score":
                    if not self.encoder:
                        self.encoder = SentenceTransformer(
                            model
                        )
                    self.metric_evaluators.append(self._bert_score)
                case "exact_match":
                    self.metric_evaluators.append(self._exact_match)
                case "rouge_l_f1":
                    self.metric_evaluators.append(self._rouge_l_f1)
                case "hallucination_rate":
                    self.metric_evaluators.append(self._hallucination_rate)

    def _latency(self, q: Question, a: Answer) -> MetricValue:
        return MetricValue(
                type = MetricType.LATENCY,
                value = a.latency_ms,
                metadata=None
            )
    def _token_count(self, q: Question, a: Answer) -> MetricValue:
        return MetricValue(
                type = MetricType.TOKEN_COUNT,
                value = a.token_count,
                metadata=None
            )
    def _bert_score(self, q: Question, a: Answer) -> MetricValue:
        emb_pred = self.encoder.encode([a.text])[0]
        emb_true = self.encoder.encode([q.ground_true])[0]
        return MetricValue(
                type = MetricType.BERT_SCORE,
                value = self.encoder.similarity(emb_pred, emb_true)[0][0],
                metadata=None
            )
    def _exact_match(self, q: Question, a: Answer) -> MetricValue:
        return MetricValue(
                type = MetricType.EXACT_MATCH,
                value = float(q.ground_true.strip() == a.text.strip()),
                metadata=None
            )
    def _rouge_l_f1(self, q: Question, a: Answer) -> MetricValue:
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
        '''pred_emb = self.encoder.encode(a.text)
        doc_emb = self._embed(source_doc)
        # Косинусное сходство (векторы нормализованы, поэтому просто скалярное произведение)
        sim = float(np.dot(pred_emb, doc_emb))
        return 1.0 - sim'''
        raise NotImplementedError

    def execute(self, q: Question, a: Answer) -> List[MetricValue]:
        metrics = []

        for metric_evaluator in self.metric_evaluators:
            metrics.append(metric_evaluator(q,a))

        return metrics
