from typing import Any, List
from src.etl.domain.interfaces import IParser
from src.etl.domain.value_objects import MessageMetadata
from telethon import TelegramClient
from src.etl.usecase.anonymiser import TelegramAnonymizer
from dataclasses import replace

class TelegramGrabber:
    def __init__(self, client: TelegramClient, parser: IParser):
        self.client = client
        self.parser = parser

    async def grab_chat(self, chat_entity: str, limit: int = 10):
        # Убеждаемся, что клиент запущен
        if not self.client.is_connected():
            await self.client.start()

        results = []
        # Получаем сообщения
        async for message in self.client.iter_messages(chat_entity, limit=limit):
            # Передаем client в парсер, если нужно качать медиа
            metadata = await self.parser.parse_message(message)
            results.append(metadata)
        
        return results


class TelegramParser(IParser ):
    def __init__(self, client: TelegramClient, anonymizer: Optional[TelegramAnonymizer] = None):
        self.client = client
        self.anonymizer = anonymizer
    async def parse_message(self, event: Any) -> MessageMetadata:
        msg = event
        text = msg if isinstance(msg, str) else getattr(msg, 'message', "")
        chat_id = getattr(msg, 'chat_id', 0)
        sender_id = getattr(msg, 'sender_id', 0)
        if self.anonymizer:
                sender_id = sender_id = self.anonymizer._TelegramAnonymizer__get_label(sender_id, "PER")
                text = self.anonymizer._TelegramAnonymizer__process_text(text)
        
        attached_files = []
        if hasattr(msg, 'media') and msg.media:
            file_path = f"media/{chat_id}/{msg.id}"
            path = await self.client.download_media(msg, file=file_path)
            attached_files.append(path)
        return MessageMetadata(
            chat_id=chat_id,
            sender_id=sender_id,
            text=text,
            attached_files=attached_files
        )

    async def parse_batch(self, raw_events: List[Any]) -> List[MessageMetadata]:
        results = []
        for event in raw_events:
            metadata = await self.parse_message(event)
            if metadata.text or metadata.attached_files:
                results.append(metadata)
        if self.anonymizer:
            final_results = []
            for msg in results:
                new_text = self.anonymizer._TelegramAnonymizer__process_text_again(msg.text)
                new_msg = replace(msg, text=new_text)
                final_results.append(new_msg)
        return final_results
