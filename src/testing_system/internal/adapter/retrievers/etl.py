import logging

from testing_system.internal.domain.interfaces import IRetriever
from testing_system.internal.domain.value_objects import RetrievedDocument, \
RetrievalRequest, RetrievalResponse
import requests

logger = logging.getLogger(__name__)

class EtlRetriever(IRetriever):
    def __init__(self, url : str, chat_id: str, k: int, clean: str):
            self.ETL_SERVICE_URL = url
            self.chat_id = chat_id
            self.k = k
            self.clean = clean
    
    def retrieve(self, request: RetrievalRequest) -> RetrievalResponse:
        params = {
            "query": request.query,
            "chat_id": self.chat_id,
            "k": self.k,
            "clean": self.clean
        }
        response = requests.get(f"{self.ETL_SERVICE_URL}/search", params=params)
        logger.info("retriever: responce recieved")
        response.raise_for_status()

        data = response.json()
        documents = []
        for d in data["results"]:
             document = RetrievedDocument(
                  id=f'{d["chat_id"]}:{d["sender_id"]}',
                  content=d["text"],
                  metadata={"attached_files":d["attached_files"]}
             )
             documents.append(document)
        return RetrievalResponse(
            documents=documents,
            k=self.k
        )