import uuid
from typing import List
from qdrant_client import AsyncQdrantClient
from qdrant_client.http import models
from dataclasses import asdict
from fastembed import TextEmbedding

from src.etl.internal.domain.interfaces import IRepository
from src.etl.internal.domain.value_objects import MessageMetadata


class QdrantFastEmbedRepository(IRepository):
    def __init__(self, url: str, api_key: str, collection_name: str):
        self._client = AsyncQdrantClient(url=url, api_key=api_key)
        self._collection_name = collection_name

        # Модель скачается автоматически при первом запуске
        print(TextEmbedding.list_supported_models())
        print(TextEmbedding.list_supported_models())
        self._model = TextEmbedding(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    async def save_batch(self, messages: List[MessageMetadata]) -> None:
        try:
            texts = [m.text if m.text else "" for m in messages]

            # Генерируем векторы (FastEmbed работает со списками строк)
            # Мы превращаем генератор в список
            embeddings = list(self._model.embed(texts))

            points = [
                models.PointStruct(
                    id=str(uuid.uuid4()),
                    vector=vector.tolist(),  # Конвертируем numpy array в list
                    payload=asdict(msg)
                )
                for vector, msg in zip(embeddings, messages)
            ]

            self._client.upload_points(
                collection_name=self._collection_name,
                points=points,
                wait=True
            )
        except Exception as e:
            raise

    async def search_similar(self, query_text: str, chat_id: int, k: int) -> List[
        MessageMetadata]:
        try:
            # Векторизуем поисковый запрос
            query_vector = list(self._model.embed([query_text]))[0].tolist()

            response = await self._client.query_points(
                collection_name=self._collection_name,
                query=query_vector,
                query_filter=models.Filter(
                    must=[
                        models.FieldCondition(
                            key="chat_id",
                            match=models.MatchValue(value=chat_id)
                        )
                    ]
                ),
                limit=k,
                with_payload=True
            )

            return [MessageMetadata(**hit.payload) for hit in response.points if
                    hit.payload]
        except Exception as e:
            raise
