from src.etl.domain.interfaces import IRepository
from src.etl.adapter.loader import YandexLoader
from src.etl.usecase.Save_Data import SaveDataUseCase

class FakeRepository(IRepository):

    async def save_batch(self, messages):

        print(f"SAVED: {len(messages)} messages")

        for msg in messages[:3]:
            print(msg)

import asyncio

async def main():

    # HTML parser
    html_parser = HTMLParser()

    # Yandex parser
    yd_parser = YandexParser(html_parser)

    # Loader adapter
    loader = YandexLoader(yd_parser)

    # Fake repo
    repo = FakeRepository()

    # UseCase
    usecase = SaveDataUseCase(
        loader=loader,
        repository=repo
    )

    # Yandex Disk public link
    source = "https://disk.yandex.ru/d/S66VjvFp6vss3Q"

    await usecase.execute(source)


if __name__ == "__main__":
    asyncio.run(main())