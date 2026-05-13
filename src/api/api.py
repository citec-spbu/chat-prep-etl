from fastapi import FastAPI, HTTPException
from src.etl.adapter.repository import QdrantFastEmbedRepository
from src.etl.usecase.get_data import GetMessageUseCase
from src.etl.dbconfig import url, api_key, test_collection_name

app = FastAPI(title="Chat Prep ETL API")

# Используем коллекцию, которую мы только что успешно проверили
repo = QdrantFastEmbedRepository(url, api_key, test_collection_name)
use_case = GetMessageUseCase(repo)

@app.get("/search")
async def search(query: str, chat_id: int, k: int = 1, clean: bool = False):
    """
    Семантический поиск по сообщениям.
    :param query: Твой поисковый запрос (то, что мы тестировали)
    :param chat_id: ID чата (например, 101)
    :param k: Сколько сообщений вернуть
    :param clean: Нужно ли прогнать через очистку (clear_service)
    """
    try:
        if clean:
            # Используем твой метод get_clean из UseCase
            results = await use_case.get_clean(query, chat_id, k)
        else:
            # Обычный сырой поиск
            results = await use_case.get_raw(query, chat_id, k)
            
        if not results:
            return {"message": "Ничего не найдено", "results": []}
            
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)