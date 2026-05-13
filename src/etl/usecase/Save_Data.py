from src.etl.domain.interfaces import IRepository

class SaveDataUseCase:
    def __init__(self, loader, repository: IRepository):
        self.loader = loader
        self.repository = repository

    async def execute(self, sourse: str):
        messages = await self.loader.load(sourse)

        await self.repository.save_batch(messages)