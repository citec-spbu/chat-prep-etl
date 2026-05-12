import re
from typing import List

import numpy as np
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
                    if not self.encoder:
                        self.encoder = SentenceTransformer(
                            model
                        )
                    self.metric_evaluators.append(self._hallucination_rate)
                case "numeric_accuracy":
                    self.metric_evaluators.append(self._numeric_accuracy)
                case "overlap":
                    self.metric_evaluators.append(self._overlap)

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
        sentences = re.split(r'[.!?]+', '\n'.join(i.content for i in a.retrieved_context))
        sentences = [s.strip() for s in sentences if s.strip()]
        if not sentences:
            return 0.0
        pred_emb = self.encoder.encode([a.text])[0]
        sentences_embs = self.encoder.encode(sentences)
        similarities = self.encoder.similarity(pred_emb, sentences_embs)[0]
        return MetricValue(
            type = MetricType.HALLUCINATION_RATE,
            value = float(np.max(similarities))
        )
    def _numeric_accuracy(self, q: Question, a: Answer) -> MetricValue:
        pred_numbers = set(re.findall(r'-?\d+/\d+|-?\d+\.\d+|-?\d+', a.text))
        ref_numbers = set(re.findall(r'-?\d+/\d+|-?\d+\.\d+|-?\d+', q.ground_true))
        if not ref_numbers:  
            return 1.0 
        if not pred_numbers:
            return 0.0
        intersection = pred_numbers.intersection(ref_numbers)
        return MetricValue(
            type = MetricType.NUMERIC_ACCURACY,
            value = len(intersection) / len(ref_numbers)
        )
    def _overlap(self, q: Question, a: Answer) -> MetricValue:
        """
        3 overlap metrics:
        - overlap_recall: the proportion of ethalon tokens in answer
        - overlap_precision: the proportion of given tokens to ethalon's
        - overlap_symmetric: the intersection divided by minimum size (as a metric default value)
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
                "overlap_recall": recall,
                "overlap_precision": precision,
            }
        )
    
    def execute(self, q: Question, a: Answer) -> List[MetricValue]:
        metrics = []

        for metric_evaluator in self.metric_evaluators:
            metrics.append(metric_evaluator(q,a))

        return metrics
