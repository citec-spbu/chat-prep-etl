from abc import ABC, abstractmethod
from typing import List

from src.etl.domain.value_objects import MessageMetadata

from src.etl.adapter.tg_grabber import TelegramGrabber
from src.etl.adapter.yd_parser import YandexParser, HTMLGrabber

class IDataLoader(ABC):

    @abstractmethod
    async def load(self, source: str) -> List[MessageMetadata]:
        pass

class TelegramLoader(IDataLoader):

    def __init__(self, grabber: TelegramGrabber):
        self.grabber = grabber

    async def load(self, source: str) -> List[MessageMetadata]:

        return await self.grabber.grab_chat(source)

class YandexLoader(IDataLoader):

    def __init__(self, parser: YandexParser):
        self.parser = parser

    async def load(self, source: str) -> List[MessageMetadata]:

        return await self.parser.parse(source)
    
class HTMLLoader(IDataLoader):

    def __init__(self, grabber: HTMLGrabber):
        self.grabber = grabber

    async def load(self, source: str) -> List[MessageMetadata]:

        return await self.grabber.grab_from_file(source)