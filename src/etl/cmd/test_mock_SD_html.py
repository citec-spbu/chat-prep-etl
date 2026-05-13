import asyncio
from src.etl.adapter.yd_parser import HTMLParser, HTMLGrabber
from src.etl.adapter.loader import HTMLLoader
from src.etl.usecase.Save_Data import SaveDataUseCase
from src.etl.domain.interfaces import IRepository
from src.etl.usecase.anonymiser import TelegramAnonymizer

class FakeRepository(IRepository):

    async def save_batch(self, messages):

        print(f"\nSAVED: {len(messages)} messages\n")

        for msg in messages[:5]:
            print(msg)

    async def search_similar(self, *args, **kwargs):

        return []

async def main():
    anonymizer = TelegramAnonymizer()

    html_parser = HTMLParser(
        anonymizer=anonymizer
    )

    html_grabber = HTMLGrabber(html_parser)

    loader = HTMLLoader(html_grabber)

    repo = FakeRepository()

    usecase = SaveDataUseCase(
        loader=loader,
        repository=repo
    )

    # html export path
    source = r"C:\Users\Alina\Desktop\chat-prep-etl\messages.html"

    await usecase.execute(source)


if __name__ == "__main__":
    asyncio.run(main())