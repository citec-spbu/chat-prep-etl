import asyncio
from src.etl.adapter.repository import QdrantFastEmbedRepository
from src.etl.dbconfig import url, api_key, test_collection_name
from src.etl.domain.value_objects import MessageMetadata

async def check_and_fix():
    repo = QdrantFastEmbedRepository(url, api_key, test_collection_name)
    
    # 1. Проверим, что в базе хоть что-то есть
    # Если поиск по пустому запросу ничего не дает, значит база пуста
    test_query = "сбросить пароль"
    chat_id = 101
    
    print(f"📡 Проверяем базу {test_collection_name}...")
    results = await repo.search_similar(test_query, chat_id, k=1)
    
    if not results:
        print("❌ База пуста или chat_id не совпадает. Перезаписываем тестовые данные...")
        msg = MessageMetadata(
            chat_id=101, 
            sender_id=1, 
            text="Как сбросить пароль от учетной записи?", 
            attached_files=[]
        )
        await repo.save_batch([msg])
        print("✅ Данные записаны. Пробуем найти снова...")
        results = await repo.search_similar(test_query, chat_id, k=1)
    
    for r in results:
        print(f"🎯 Найдено: {r.text}")

if __name__ == "__main__":
    asyncio.run(check_and_fix())