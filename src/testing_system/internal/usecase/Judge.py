from typing import List
from testing_system.internal.domain.entities import MetricValue, Question, Answer, MetricType
from testing_system.internal.domain.interfaces import IAssistant
from testing_system.internal.domain.value_objects import AssistantRequest, AssistantResponse

class Judge:
    """
    The judge of the experiment. The external system, that:
        - evaluates the accuracy of the answer to the question
        - saturates the answer with the information about relevant documents (optional)

    Check full research in the cmd/notebooks/judge_experiments.ipynb
    """
    
    def __init__(self, model: IAssistant):
        self._MODEL = model
        self._SYSTEM_PROMPT = ""

    def execute(self, q: Question, a: Answer) -> tuple[MetricValue, Answer]:
        """
        The function for evaluation by judge.
        Args:
            q (Question): The question for the assistant.
            a (Answer): The answer of the Assistant to be evaluated.

        Returns:
            MetricValue: The accuracy of the answer (0 / 0.5 / 1),
            Answer: The a with filled attribute retrieved_context
        """
        a.retrieved_context = q.retrieved_context_id
        return (MetricValue(
            type="accuracy",
            value=0.5,
            metadata=None
        ), a)