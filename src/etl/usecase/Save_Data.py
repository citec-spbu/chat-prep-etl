from src.etl.domain.interfaces import IRepository
from src.etl.adapter.tg_grabber import TelegramGrabber
from src.etl.domain.value_objects import MessageMetadata
from src.etl.adapter.yd_parser import YandexParser, HTMLGrabber

class SaveDataUseCase:

    def __init__(self, grabber: TelegramGrabber, repository: IRepository, yd_parser: YandexParser, html_grabber: HTMLGrabber):
        self.grabber = grabber
        self.repository = repository
        self.yd_parser = yd_parser
        self.html_grab = html_grabber

    
    async def execute(self, source_type: str, source: str):

        # 1. Получаем сообщения (уже MessageMetadata)/Яндекс Диск
        # В TelegramGrabber и YandexGrabber уже выполняется и парсинг и перевод в текста в сущность.
        if source_type == "tg":
            messages = await self.grabber.grab_chat(source)
        elif source_type == "yd":
            messages = await self.yd_parser.parse(source)
        elif source_type == "html":
            messages = await self.html_grab.grab_from_file(source)
        else:
            raise ValueError("Unknown source type")

        #2. Сохранение
        await self.repository.save_batch(messages)