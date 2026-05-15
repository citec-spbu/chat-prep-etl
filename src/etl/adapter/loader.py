from typing import List
from src.etl.domain.interfaces import IDataLoader
from src.etl.domain.value_objects import MessageMetadata
from src.etl.adapter.yd_parser import HTMLGrabber, ArchiveChatParser
from src.etl.adapter.tg_grabber import TelegramGrabber

class TelegramLoader(IDataLoader):

    def __init__(self, grabber: TelegramGrabber):
        self.grabber = grabber

    async def load(self, source: str) -> List[MessageMetadata]:

        return await self.grabber.grab_chat(source)

class ArchiveChatLoader(IDataLoader):

    def __init__(self, parser: ArchiveChatParser):
        self.parser = parser

    async def load(self, source: str) -> List[MessageMetadata]:

        return await self.parser.parse(source)
    
class HTMLLoader(IDataLoader):

    def __init__(self, grabber: HTMLGrabber):
        self.grabber = grabber

    async def load(self, source: str) -> List[MessageMetadata]:

        return await self.grabber.grab_from_file(source)