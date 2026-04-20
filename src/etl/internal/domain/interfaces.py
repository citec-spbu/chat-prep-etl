from abc import ABC, abstractmethod
from typing import List

from src.etl.internal.domain.value_objects import MessageMetadata


class IRepository(ABC):
    @abstractmethod
    async def save_batch(self, messages: List[MessageMetadata]) -> None:
        pass

    @abstractmethod
    async def search_similar(self, query_text: str, chat_id: int, k: int) -> List[MessageMetadata]:
        pass
