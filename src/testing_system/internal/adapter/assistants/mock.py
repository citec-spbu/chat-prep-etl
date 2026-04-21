from testing_system.internal.domain.interfaces import IAssistant
from testing_system.internal.domain.value_objects import AssistantRequest, AssistantResponse
from math import ceil

class MockAssistant(IAssistant):
    def __init__(self, name="MockAssistant"):
        self.name = name
        
    def ask(self, r: AssistantRequest) -> AssistantResponse:
        response = \
            f"""Я {self.name}, я ничего не знаю!

            Но у меня есть в это:

            """
        for d in r.retrieved_context:
            response += d.content + "\n            "
        return AssistantResponse(
            answer=response,
            token_count=ceil(len(response)/3),
            latency_ms=0,
            used_prompt=r.question,
            error=None,
            metadata=None
        )