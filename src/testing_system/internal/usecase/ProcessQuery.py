from typing import Any, Dict, Optional

from testing_system.internal.domain.interfaces import IAssistant, IRetriever
from testing_system.internal.domain.value_objects import AssistantResponse, \
    AssistantRequest, RetrievalRequest, RetrievalResponse

class Processor:
    def __init__(self, 
                 assistant: IAssistant, 
                 retriever: IRetriever,
                 ):
        self.assistant = assistant
        self.retriever = retriever

    def execute(self, 
                question:str,  
                system_prompt: Optional[str] = None,
                temperature: Optional[float] = None,
                metadata: Dict[str,Any] = None
                ) -> AssistantResponse:
        retrieve_request = RetrievalRequest(
            query=question,
        )
        retrieve_response = self.retriever.retrieve(request=retrieve_request)

        assistant_request = AssistantRequest(
            question=question,
            retrieved_context=retrieve_response.documents,
            system_prompt=system_prompt,
            temperature=temperature,
            metadata=metadata
        )

        assistant_response = self.assistant.ask(assistant_request)
        return assistant_response