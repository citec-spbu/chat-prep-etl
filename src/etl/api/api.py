from fastapi import FastAPI, UploadFile, BackgroundTasks
from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import List

app = FastAPI(title="AI Assistant Trainer API", version="1.0.0")

# Модели для Swagger
class DatasetResponse(BaseModel):
    dataset_id: UUID
    status: str

class ExperimentConfig(BaseModel):
    dataset_id: UUID
    prompt_id: str
    questions: List[str]

@app.post("/datasets/upload", response_model=DatasetResponse, tags=["Datasets"])
async def upload_dataset(file: UploadFile):
    # 1. Сохраняем файл
    dataset_id = uuid4()
    # 2. Пишем в БД Postgres (Dataset status: anonymizing)
    # 3. Отправляем в RabbitMQ (celery_app.send_task("anonymize", ...))
    return {"dataset_id": dataset_id, "status": "anonymizing"}

@app.get("/datasets/{id}", tags=["Datasets"])
async def get_dataset_status(id: UUID):
    # Читаем статус из Postgres
    return {"id": id, "status": "clean", "sample_data": "..."}

@app.post("/experiments", tags=["Experiments"])
async def create_experiment(config: ExperimentConfig):
    exp_id = uuid4()
    # Создаем запись в базе
    return {"experiment_id": exp_id}

@app.post("/experiments/{id}/run", tags=["Experiments"])
async def run_experiment(id: UUID):
    # Отправляем задачу в Celery (evaluation)
    return {"task_id": uuid4(), "status": "started"}

@app.get("/experiments/{id}/metrics", tags=["Experiments"])
async def get_metrics(id: UUID):
    # Возвращаем результаты (accuracy, hallucination_rate и т.д.)
    return {
        "accuracy": 0.85,
        "latency": "250ms",
        "cost_proxy": 0.12
    }