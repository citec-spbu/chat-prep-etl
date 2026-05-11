from typing import List
from testing_system.internal.domain.entities import MetricValue, Question, Answer, MetricType
from sklearn.metrics.pairwise import cosine_similarity
from light_embed import TextEmbedding
from rouge_score import rouge_scorer

class Eval:
    """
    The measurer of the experiment

    The evaluation method
    input: Question, Answer
    output: List[MetricValue] 

    check all the entities in the
    testing_system/internal/domain/entities.py
    """
    
    def __init__(self, metrics: List[str]):
        self.metric_evaluators = []
        self.encoder = None
        for i in range(len(metrics)):
            match metrics[i]:
                case "latency":
                    self.metric_evaluators.append(self._latency)
                case "token_count":
                    self.metric_evaluators.append(self._token_count)
                case "bert_score":
                    self.encoder = TextEmbedding(
                        "sentence-transformers/distiluse-base-multilingual-cased-v2"
                        )
                    self.metric_evaluators.append(self._bert_score)

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
        emb_true = self.encoder.encode([q.ground_truth])[0]
        return MetricValue(
                type = MetricType.TOKEN_COUNT,
                value = cosine_similarity([emb_pred], [emb_true])[0][0],
                metadata=None
            )
    def _rouge_score(self, q: Question, a: Answer) -> MetricValue:
        raise NotImplementedError
    
    def execute(self, q: Question, a: Answer) -> List[MetricValue]:
        metrics = []

        for metric_evaluator in self.metric_evaluators:
            metrics.append(metric_evaluator(q,a))

        if q.retrieved_context_id and a.retrieved_context:
            relevant_found = set(q.retrieved_context_id) & set(a.retrieved_context)

            #precision
            #кол-во правильных из всех найденных
            precision = len(relevant_found)/ len(a.retrieved_context)
            metrics.append(
            MetricValue(
                type = MetricType.PRECISION,
                value = precision,
                metadata=None
            )
        )
            #recall
            #кол-во правильных из всех документов
            recall = len(relevant_found) / len(q.retrieved_context_id)
            metrics.append(
            MetricValue(
                type = MetricType.RECALL,
                value = recall,
                metadata=None
            )
        )
        return metrics
