import asyncio
import asyncpg

from src.etl.adapter.pg_repository.test_messages import test_messages
from src.etl.adapter.pg_repository.pg_repository import PostgresRepository


async def init_database(dsn: str, with_drop: bool = True) -> None:
    drop_table_query = """
    DROP TABLE IF EXISTS message_metadata;
    """

    create_table_query = """
    CREATE TABLE IF NOT EXISTS message_metadata (
        id SERIAL PRIMARY KEY,
        chat_id BIGINT NOT NULL,
        sender_id BIGINT,
        text TEXT,
        attached_files TEXT[] NOT NULL DEFAULT '{}',
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );

    CREATE INDEX IF NOT EXISTS idx_messages_chat_id_created 
    ON message_metadata(chat_id, created_at DESC);
    """

    print("Проверка и инициализация структуры Базы Данных...")

    conn = await asyncpg.connect(dsn=dsn)
    try:
        if with_drop:
            await conn.execute(drop_table_query)
        await conn.execute(create_table_query)
        print("Инициализация структуры БД успешно завершена.")
    finally:
        await conn.close()


async def main():
    DATABASE_URL = "postgresql://postgres:123@localhost:5432/chats"
    TARGET_CHAT_ID = 4224

    try:
        await init_database(DATABASE_URL)
    except Exception as e:
        print(f"Не удалось подключиться к PostgreSQL. Ошибка: {e}")
        return

    print("Инициализация репозитория и пула соединений...")
    repository = await PostgresRepository.create(dsn=DATABASE_URL)


    print("Подготовка пакета тестовых сообщений...")

    print(f"Сохраняем {len(test_messages)} сообщений в базу данных...")
    await repository.save_batch(test_messages)
    print("Пакет сообщений успешно сохранен.")

    print(f"Запрос всех сообщений для chat_id: {TARGET_CHAT_ID}...")
    history = await repository.search_similar(query_text="", chat_id=TARGET_CHAT_ID)

    print("\n=== ИСТОРИЯ ЧАТА ===")
    for index, msg in enumerate(history, 1):
        print(f"{index}. {msg.sender_id}: {msg.text}")

    await repository.close()
    print("Работа скрипта успешно завершена.")


if __name__ == "__main__":
    # Запуск асинхронного event loop
    asyncio.run(main())