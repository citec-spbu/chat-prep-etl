from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import Optional
import os
from src.api.factory import create_client
from src.etl.adapter.repository import QdrantFastEmbedRepository
from src.etl.usecase.get_data import GetMessageUseCase
from src.etl.usecase.Save_Data import SaveDataUseCase
from src.etl.adapter.loader import TelegramLoader, YandexLoader, HTMLLoader
from src.etl.adapter.tg_grabber import TelegramGrabber, TelegramParser
from src.etl.adapter.yd_parser import HTMLGrabber, ArchiveChatParser, HTMLParser
from src.etl.dbconfig import url, api_key, test_collection_name, collection_name
from src.etl.usecase.anonymiser import TelegramAnonymizer

app = FastAPI(title="Chat Prep ETL API")

# Используем коллекцию, которую мы только что успешно проверили
repo = QdrantFastEmbedRepository(url, api_key, collection_name)
get_message_use_case = GetMessageUseCase(repo)
_tg_client = None
anonymizer = TelegramAnonymizer()


@app.on_event("startup")
async def startup_event():
    pass

async def get_active_tg_client():
    global _tg_client
    if _tg_client is None:
        _tg_client = await create_client()
    
    if not _tg_client.is_connected():
        await _tg_client.connect()
    
    if not await _tg_client.is_user_authorized():
        await _tg_client.start()
        
    return _tg_client


class IngestRequest(BaseModel):
    source_type: str  # "telegram", "yandex", "html"
    source_path: str  # Название чата, ссылка на Я.Диск или путь к файлу
    chat_id: Optional[int] = 0  # Для телеграма, если нужно указать явно
    limit: Optional[int] = 100

@app.post("/ingest")
async def ingest_messages(request: IngestRequest, background_tasks: BackgroundTasks):
    """Эндпоинт для запуска загрузки данных"""
    try:
        if request.source_type == "telegram":
            client = await get_active_tg_client()
            parser = TelegramParser(client, anonymizer)
            grabber = TelegramGrabber(client, parser)
            loader = TelegramLoader(grabber)
        
        elif request.source_type == "yandex":
            loader = YandexLoader(ArchiveChatParser(HTMLParser(source_name=str(request.chat_id), anonymizer=anonymizer)))
            
        elif request.source_type == "html":
            loader = HTMLLoader(HTMLGrabber(HTMLParser(source_name=str(request.chat_id), anonymizer=anonymizer)))
            
        else:
            raise HTTPException(status_code=400, detail="Unknown source type")

        # 2. Создаем UseCase и запускаем в фоне
        save_use_case = SaveDataUseCase(loader, repo)
        
        # Передаем в execute. Если это телеграм, source_path — имя чата.
        background_tasks.add_task(save_use_case.execute, request.source_path)

        return {
            "status": "accepted", 
            "message": f"Загрузка из {request.source_type} запущена в фоновом режиме"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/search")
async def search(query: str, chat_id: int, k: int = 1, clean: str = "raw"):
    """
    Семантический поиск по сообщениям.
    :param query: Твой поисковый запрос (то, что мы тестировали)
    :param chat_id: ID чата (например, 101)
    :param k: Сколько сообщений вернуть
    :param clean: Нужно ли прогнать через очистку (clear_service)
    """
    try:
        if clean == "clean":

            results = await get_message_use_case.get_clean(query, chat_id, k)
        elif clean == "raw+clean":

            results = await get_message_use_case.get_raw_clear(query, chat_id, k)
        elif clean == "raw":

            results = await get_message_use_case.get_raw(query, chat_id, k)
            
        if not results:
            return {"message": "Ничего не найдено", "results": []}
            
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    os.makedirs("sessions", exist_ok=True)
    uvicorn.run(app, host="0.0.0.0", port=8000)