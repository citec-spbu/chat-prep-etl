import logging
from contextlib import asynccontextmanager
from typing import List, Optional
import asyncio

from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel

from testing_system.internal.controller.Orchestrator import Orchestrator
from testing_system.internal.domain.entities import Experiment

class RunExperimentsRequest(BaseModel):
    experiments_path: Optional[str] = None

class RunExperimentsResponse(BaseModel):
    message: str
    path: str

def create_app(
    *,
    orchestrator: Orchestrator,
    config: dict,
    logger: logging.Logger
) -> FastAPI:
    """Создаёт и настраивает экземпляр FastAPI."""
    
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        logger.info("HTTP server initializing")
        yield
        logger.info("HTTP server shutting down")

    app = FastAPI(
        title="Testing System API",
        version="0.1.0",
        lifespan=lifespan,
    )

    @app.get("/health")
    async def health():
        """Проверка работоспособности сервиса."""
        return {"status": "ok"}
    
    @app.get("/experiments/progress")
    async def get_progress():
        """Прогресс выполнения экспериментов"""
        return orchestrator.progress

    @app.get("/experiments", response_model=List[Experiment])
    async def list_experiments():
        """Возвращает список известных экспериментов с их статусами."""
        if orchestrator is None:
            raise HTTPException(status_code=503, detail="Service not initialized")
        try:
            experiments = orchestrator.show_experiments()
            return experiments
        except Exception as e:
            logger.exception("Failed to list experiments")
            raise HTTPException(status_code=500, detail=str(e))

    @app.post("/experiments/run", status_code=202)
    async def run_experiments(request: RunExperimentsRequest = Body(...)):
        """Запускает выполнение экспериментов асинхронно (202 Accepted)."""
        if orchestrator is None:
            raise HTTPException(status_code=503, detail="Service not initialized")
        path = request.experiments_path or config.get("testing_system", {}).get("loaders", {}).get("path")
        if not path:
            raise HTTPException(status_code=400, detail="No experiments path provided")

        asyncio.create_task(orchestrator.execute_experiments(path))
        logger.info(f"Experiment execution started for path: {path}")
        return RunExperimentsResponse(message="Execution started", path=path)

    return app