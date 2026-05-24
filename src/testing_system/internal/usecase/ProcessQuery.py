import logging
from typing import Any, Dict, Optional

from testing_system.internal.domain.interfaces import IAssistant, IRetriever
from testing_system.internal.domain.value_objects import AssistantResponse, \
    AssistantRequest, RetrievalRequest, RetrievalResponse

logger = logging.getLogger(__name__)

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
        logger.debug(f"Processor: retrieve is complete with {len(retrieve_response.documents)} documents")
        assistant_request = AssistantRequest(
            question=question,
            retrieved_context=retrieve_response.documents,
            system_prompt=system_prompt,
            temperature=temperature,
            metadata=metadata
        )
        logger.debug(f"Processor: asking assistant")
        assistant_response = self.assistant.ask(assistant_request)
        return assistant_response