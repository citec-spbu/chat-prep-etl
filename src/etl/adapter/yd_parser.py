from typing import Any, List
import os
from bs4 import BeautifulSoup
from src.etl.internal.domain.interfaces import IParser
from src.etl.internal.domain.value_objects import MessageMetadata

class HTMLParser(IParser):
    def __init__(self):
        pass

    async def parse_message(self, element: Any) -> MessageMetadata:
        ...

    async def parse_batch(self, html_content: str) -> List[MessageMetadata]:
        soup = BeautifulSoup(html_content, 'html.parser')
        message_elements = soup.find_all("div", class_="message default")
        return [await self.parse_message(el) for el in message_elements]
    
class HTMLGrabber:
    def __init__(self, parser: IParser):
        self.parser = parser

    async def grab_from_file(self, file_path: str) -> List[MessageMetadata]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Передаем контент в парсер
        return await self.parser.parse_batch(content)