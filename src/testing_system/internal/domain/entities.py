from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional, List, Any, Dict

@dataclass
class Question:
    """
    The question for the assistant
    TODO there should be system prompt, i think
    """
    id: str
    text: str
    retrieved_context_id: Optional[List[str]] = None # for RECALL
    metadata: Optional[Dict[str, Any]] = None

@dataclass
class Answer:
    """The assistant`s answer (text and details)"""
    id: str
    text: str
    retrieved_context: List[str] # ID of the documents used
    token_count: int 
    latency_ms: float 
    metadata: Optional[Dict[str,Any]] = None

class MetricType(Enum):
    #PRECISION = "precision"
    #RECALL = "recall"
    #REUSABILITY = "reusability"
    EXACT_MATCH = "exact_match"

    TOKEN_PRECISION = "token_precision"
    TOKEN_RECALL = "token_recall"
    TOKEN_F1 = "token_f1"

    ROUGE_L_F1 = "rouge_l_F1"

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
    metrics: List[MetricValue]
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None

    def add_answer(self, answer: Answer) -> None:
        self.answers.append(answer)
    
    def add_metric(self, metric: MetricValue) -> None:
        self.metrics.append(metric)

    def is_complete(self) -> bool:
        return len(self.answers) == len(self.questions) and len(self.metrics) == len(self.questions)
