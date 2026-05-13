from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional, List, Any, Dict

from testing_system.internal.domain.value_objects import RetrievedDocument

@dataclass
class Question:
    """
    The question for the assistant
    """
    id: str
    text: str
    ground_true: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

@dataclass
class Answer:
    """The assistant`s answer (text and details)"""
    id: str
    text: str
    retrieved_context: List[RetrievedDocument]
    token_count: int 
    latency_ms: float 
    metadata: Optional[Dict[str,Any]] = None

class MetricType(Enum):
    INVALID = "invalid"
    EXACT_MATCH = "exact_match"
    NUMERIC_ACCURACY = "numeric_accuracy"
    OVERLAP = "overlap"
    JACCARD = "jaccard_distance"
    ROUGE_L_F1 = "rouge_l_f1"

    BERT_SCORE = "bert_score"
    HALLUCINATION_RATE = "hallucination_rate"
    
    TOKEN_COUNT = "token_count"
    LATENCY = "latency"

@dataclass
class MetricValue:
    """The result of metric calculation"""
    type: MetricType
    value: float
    metadata: Optional[Dict[str, Any]]

@dataclass
class Experiment:
    """
    The main entity for the system - experiment
    Provides all the methods and attributes for storage and comparison
    """
    id: str
    name: str
    questions: List[Question]
    ground_truth: Dict[str, Any]
    answers: List[Answer]
    metrics: Dict[str, List[MetricValue]]
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None

    def add(self, answer: Answer, m: List[MetricValue]) -> None:
        self.answers.append(answer)
        self.metrics[answer.id] = m
