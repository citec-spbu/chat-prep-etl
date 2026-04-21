import json
from telethon import TelegramClient, events
import socks
import asyncio
from dotenv import load_dotenv
import os


# Бд еще в разработке, пока не используем
# from internal.adapters.vector_db import QdrantAdapter, COLLECTION, PointStruct
# from internal.domain.services import Embedder


load_dotenv()
api_id = int(os.getenv('API_ID'))  
api_hash = os.getenv('API_HASH')  
chat_username = os.getenv('CHAT_USERNAME')  

proxy = (socks.SOCKS5, '127.0.0.1', 10808)        

client = TelegramClient('session_name', api_id, api_hash,proxy=proxy)
# qdrant = QdrantAdapter()
# embedder = Embedder()

# qdrant.get_collection(COLLECTION)  # Проверяем коллекцию, если нет - создаем

@client.on(events.NewMessage(chats=chat_username))
async def handler(event):
    text = event.message.message
    if not text:
        return
    #emb = await embed_text(text)
   # point = PointStruct(
        id=event.message.id,
        #vector=emb,
        payload={"text": text, "chat_id": event.chat_id} #)
    # qdrant.upsert(COLLECTION, points=[point])

async def sync_history():
    #last_id = qdrant.get_last_id()
    last_id = 0
    async for message in client.iter_messages(chat_username, min_id=last_id, limit=100):
        if message.text:
            print(f"[Sync] Подгружаем старое сообщение: {message.id}")



async def main():
    await client.start()
    await sync_history()
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())