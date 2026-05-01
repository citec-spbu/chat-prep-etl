from src.etl.domain.interfaces import IRepository
from src.etl.adapter.tg_grabber import TelegramGrabber
from src.etl.adapter.anonymizer import TelegramAnonymizer
from src.etl.domain.value_objects import MessageMetadata

class SaveDataUseCase:

    def __init__(self, grabber: TelegramGrabber, repository: IRepository, anonymizer: TelegramAnonymizer):
        self.grabber = grabber
        self.repository = repository
        self.anonymizer = anonymizer
    
    async def execute(self, source_type: str, source: str):

        # 1. Получаем сообщения (уже MessageMetadata)/Яндекс Диск
        # В TelegramGrabber уже выполняется и парсинг и перевод в текста в сущность.
        if source_type == "tg":
            messages = await self.grabber.grab_chat(source)
        elif source_type == "yd":
            messages = await self._yandex_loader(source)
        else:
            raise ValueError("Unknown source type")

        # 2. Обезличивание
        # Анонимизация выполняется с использованием TelegramAnonymizer:
        # - замена email, телефонов, ссылок (regex)
        # - распознавание сущностей (имена, города) через Natasha
        # - повторный проход для замены оставшихся сущностей
        messages = self._anonymize(messages)

        #3. Сохранение
        await self.repository.save_batch(messages)

    def _anonymize(self, messages: list[MessageMetadata]) -> list[MessageMetadata]:

        new_messages = []

        for msg in messages:
            new_text = self.anonymizer._TelegramAnonymizer__process_text(msg.text)
            new_text = self.anonymizer._TelegramAnonymizer__process_text_again(new_text)

            new_msg = MessageMetadata(
                chat_id=msg.chat_id,
                sender_id=msg.sender_id,
                text=new_text,
                attached_files=msg.attached_files
        )

            new_messages.append(new_msg)
        return new_messages