import asyncio
import time
from qdrant_client import QdrantClient
from qdrant_client.http import models

from src.etl.adapter.s import extra_messages
from src.etl.dbconfig import url, api_key, collection_name, test_collection_name
from src.etl.adapter.repository import QdrantFastEmbedRepository
from src.etl.domain.value_objects import MessageMetadata

async def test():
    print("Начало тестирования")

    URL = url
    API_KEY = api_key
    COLLECTION_NAME = test_collection_name

    client = QdrantClient(url=URL, api_key=API_KEY, check_compatibility=False)

    if client.collection_exists(collection_name=COLLECTION_NAME):
        client.delete_collection(collection_name=COLLECTION_NAME)

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(
            size=1024,
            distance=models.Distance.COSINE
        ),
        on_disk_payload=True
    )
    client.create_payload_index(
        collection_name=COLLECTION_NAME,
        field_name="chat_id",
        field_schema=models.PayloadSchemaType.KEYWORD,
    )

    repo = QdrantFastEmbedRepository(URL, API_KEY, COLLECTION_NAME)
    print("Инициализация репозитория завершена")

    start = time.perf_counter()
    await repo.save_batch(extra_messages)
    end = time.perf_counter()
    print(f"✅ Пакет успешно загружен. Время выполнения - {end-start}")

    query = "проблемы с доступом и логином"
    print(f"🔎 Ищем: '{query}' в чате 101...")
    start = time.perf_counter()
    results = await repo.search_similar(query, chat_id=101, k=3)
    end = time.perf_counter()
    print(f"✅ Ответ получен. Время выполнения - {end - start}")

    for m in results:
        print(f" - [{m.chat_id}] {m.text}")

if __name__ == "__main__":
    asyncio.run(test())