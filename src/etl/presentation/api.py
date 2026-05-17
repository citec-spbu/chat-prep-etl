from fastapi import FastAPI, HTTPException, BackgroundTasks, status, Query
from pydantic import BaseModel, Field
from typing import Optional
import os
from src.api.factory import create_client
from src.etl.adapter.repository import QdrantFastEmbedRepository
from src.etl.usecase.get_data import GetMessageUseCase
from src.etl.usecase.Save_Data import SaveDataUseCase
from src.etl.adapter.loader import TelegramLoader, ArchiveChatLoader, HTMLLoader
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
    source_type: str = Field(..., description="Допустимые типы: telegram, yandex, html")
    source_path: str = Field(..., description="Путь к локальному файлу/архиву или имя чата")
    chat_id: Optional[int] = Field(0, description="Числовой ID чата")
    limit: Optional[int] = Field(100, description="Лимит сообщений для Telegram API")

@app.post("/ingest", status_code=status.HTTP_202_ACCEPTED)
async def ingest_messages(request: IngestRequest, background_tasks: BackgroundTasks):
    """Эндпоинт для запуска загрузки данных"""

    allowed_sources = ["telegram", "yandex", "html"]
    if request.source_type not in allowed_sources:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Неверный тип источника '{request.source_type}'. Допустимые: {', '.join(allowed_sources)}"
        )

    # 2. Валидация путей файлов (404 Not Found) — проверяем ДО ухода в фоновый поток
    if request.source_type in ["html", "yandex"]:
        if not os.path.exists(request.source_path):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Указанный путь не существует или недоступен: '{request.source_path}'"
            )

    try:
        if request.source_type == "telegram":
            client = await get_active_tg_client()
            parser = TelegramParser(client, anonymizer)
            grabber = TelegramGrabber(client, parser)
            loader = TelegramLoader(grabber)
        
        elif request.source_type == "yandex":
            loader = ArchiveChatLoader(ArchiveChatParser(HTMLParser(source_name=str(request.chat_id), anonymizer=anonymizer)))
            
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
    except HTTPException:
        # Пробрасываем созданные нами HTTPException без изменений
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Внутренняя ошибка сервера при запуске задачи: {str(e)}"
        )


@app.get("/search")
async def search(query: str = Query(..., description="Твой поисковый запрос (то, что мы тестировали)"),
                 chat_id: int = Query(..., description="ID чата (например, 101)"),
                 k: int = Query(1, description="Сколько сообщений вернуть"),
                 clean: str = Query("raw", description="Нужно ли прогнать через очистку (clear_service)")):
    """
    Семантический поиск по сообщениям.
    :param query: Твой поисковый запрос (то, что мы тестировали)
    :param chat_id: ID чата (например, 101)
    :param k: Сколько сообщений вернуть
    :param clean: Нужно ли прогнать через очистку (clear_service)
    """
    if not query.strip():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Строка поискового запроса 'query' не может быть пустой"
        )
        
    allowed_clean_modes = ["raw", "clean", "raw+clean"]
    if clean not in allowed_clean_modes:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Неверный режим 'clean'='{clean}'. Допустимые: {', '.join(allowed_clean_modes)}"
        )

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
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ошибка на стороне векторного хранилища: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    os.makedirs("sessions", exist_ok=True)
    uvicorn.run(app, host="0.0.0.0", port=8000)