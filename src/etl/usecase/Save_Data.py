from src.etl.domain.interfaces import IRepository
from loguru import logger


class SaveDataUseCase:
    def __init__(self, loader, repository: IRepository):
        self.loader = loader
        self.repository = repository

    async def execute(self, source: str):
        messages = await self.loader.load(source)


        await self.repository.save_batch(messages)