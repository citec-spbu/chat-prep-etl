from src.etl.domain.interfaces import IRepository
from src.etl.adapter.loader import YandexLoader
from src.etl.adapter.yd_parser import HTMLParser, YandexParser
from src.etl.usecase.Save_Data import SaveDataUseCase
from src.etl.usecase.anonymiser import TelegramAnonymizer

import logging

logging.basicConfig(level=logging.INFO, filename="src/etl/cmd/yd.usecase_test.log", filemode="w", encoding="utf-8", format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

class FakeRepository(IRepository):

    async def save_batch(self, messages):

        try:

            logger.info(f"SAVED: {len(messages)} messages")

            for msg in messages[:3]:
                logger.info(msg)
        except Exception as e:
             logger.exception("Ошибка в репозитории")
             raise

    async def search_similar(self, *args, **kwargs):
        return []

import asyncio

async def main():
    try:
        logger.info("Создаем HTML parser...")
        # HTML parser
        html_parser = HTMLParser(anonymizer=TelegramAnonymizer())

        logger.info("Создаем Yandex parser...")
        # Yandex parser
        yd_parser = YandexParser(html_parser)

        logger.info("Creating loader...")
        # Loader adapter
        loader = YandexLoader(yd_parser)

        # Fake repo
        repo = FakeRepository()

        logger.info("Creating usecase...")
        # UseCase
        usecase = SaveDataUseCase(
            loader=loader,
            repository=repo
        )

        # Yandex Disk public link
        source = "https://disk.yandex.ru/d/S66VjvFp6vss3Q"

        await usecase.execute(source)
        logger.info("Ура, конец")

    except Exception as e:
        logger.exception("Беда, ошибка где-то")

        raise


if __name__ == "__main__":
    asyncio.run(main())