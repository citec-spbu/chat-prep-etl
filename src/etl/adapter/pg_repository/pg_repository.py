from typing import Self, List
import asyncpg

from src.etl.domain.interfaces import IRepository
from src.etl.domain.value_objects import MessageMetadata


class PostgresRepository(IRepository):
    """
    Асинхронный репозиторий для работы с базой данных PostgreSQL.
    """

    def __init__(self, pool) -> None:
        """
        Инициализирует репозиторий.
        Для создания экземпляра класса используется асинхронный
        метод `create()`.

        Args:
            pool: Активный пул соединений `asyncpg.Pool`.
        """

        self._pool = pool

    @classmethod
    async def create(cls, dsn: str, min_size: int = 1, max_size: int = 10) -> Self:
        """
        Асинхронный фабричный метод для создания и инициализации репозитория.

        Args:
            dsn: Строка подключения к PostgreSQL (Data Source Name), например:
                `postgresql://user:password@localhost:5432/dbname`.
            min_size: Минимальное количество постоянно удерживаемых соединений в пуле.
            max_size: Максимально допустимое количество параллельных соединений в пуле.
        """
        pool = await asyncpg.create_pool(
            dsn=dsn,
            min_size=min_size,
            max_size=max_size
        )
        return cls(pool=pool)

    async def close(self) -> None:
        """
        Освобождает все удерживаемые ресурсы и сетевые сокеты. Метод необходимо
        вызывать при остановке или перезапуске основного приложения.
        """
        await self._pool.close()

    async def save_batch(self, messages: List[MessageMetadata]) -> None:
        if not messages:
            return

        records = [
            (msg.chat_id, msg.sender_id, msg.text, msg.attached_files)
            for msg in messages
        ]

        query = """
            INSERT INTO message_metadata (chat_id, sender_id, text, attached_files)
            VALUES ($1, $2, $3, $4)
        """

        async with self._pool.acquire() as conn:
            async with conn.transaction():
                await conn.executemany(query, records)

    async def search_similar(self, query_text: str, chat_id: int, k: int=0) -> List[
        MessageMetadata]:
        return await self.search(chat_id)

    async def search(self, chat_id: int) -> List[MessageMetadata]:
        query = """
            SELECT chat_id, sender_id, text, attached_files
            FROM message_metadata
            WHERE chat_id = $1
            ORDER BY created_at ASC
        """

        async with self._pool.acquire() as conn:
            rows = await conn.fetch(query, chat_id)

        return [
            MessageMetadata(
                chat_id=row['chat_id'],
                sender_id=row['sender_id'],
                text=row['text'],
                attached_files=row['attached_files']
            )
            for row in rows
        ]
