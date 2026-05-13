from typing import List, Tuple, Optional

from src.etl.domain.interfaces import IRepository
from src.etl.domain.value_objects import MessageMetadata
from src.etl.usecase.clear_service import process_message


class MessageMetadataUseCase:
    def __init__(self, repository: IRepository):
        self._repository = repository

    async def get_clean(self, query: str, chat_id: int, k: int = 5) -> List[
        MessageMetadata]:
        """
        Возвращает только очищенные результаты поиска.
        """
        raw_results = await self._repository.search_similar(query, chat_id, k)
        cleaned_results = []
        for msg in raw_results:
            cleared_msg = self._clear(msg)
            cleaned_results.append(cleared_msg)
        return cleaned_results

    async def get_raw(self, query: str, chat_id: int, k: int = 5) -> List[
        MessageMetadata]:
        """
        Возвращает сырые результаты поиска напрямую из репозитория.
        """
        return await self._repository.search_similar(query, chat_id, k)

    async def get_raw_clear(self, query: str, chat_id: int, k: int = 5) -> List[
        Tuple[MessageMetadata, MessageMetadata]]:
        """
        Возвращает пары сырых и очищенных данных.
        """
        raw_messages = await self.get_raw(query, chat_id, k)
        all_pairs = []

        for msg in raw_messages:
            cleared_msg = self._clear(msg)
            all_pairs.append((msg, cleared_msg))

        return all_pairs

    def _clear(self, message: MessageMetadata) -> MessageMetadata:
        return process_message(message)
