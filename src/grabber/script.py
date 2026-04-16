import json
from telethon import TelegramClient
import socks

with open('config.txt', 'r') as f:
    # Читаем строку, разделяем по знаку "=" и берем правую часть
    api_id = int(f.readline().split('=')[1].strip())
    api_hash = f.readline().split('=')[1].strip()
    chat_username = f.readline().split('=')[1].strip()  # Читаем имя пользователя чата

proxy = (socks.SOCKS5, '127.0.0.1', 10808)  # Пример прокси, если нужно       

client = TelegramClient('session_name', api_id, api_hash,proxy=proxy)

async def main():
    data = []
    # Получаем сущность чата
    async for message in client.iter_messages(chat_username, limit=100):
        # Формируем структуру данных
        msg_data = {
            "id": message.id,
            "date": str(message.date),
            "sender_id": message.sender_id,
            "text": message.text,
            "is_reply": message.is_reply,
        }
        data.append(msg_data)

    # Сохраняем в JSON
    with open('chat_history.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print("Готово! Данные сохранены в chat_history.json")

with client:
    client.loop.run_until_complete(main())