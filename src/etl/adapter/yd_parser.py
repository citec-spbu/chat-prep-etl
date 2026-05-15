import os
import zipfile
import requests
import tempfile
import shutil
from dataclasses import replace
from typing import List, Any, Optional
from bs4 import BeautifulSoup
from loguru import logger
from src.etl.domain.interfaces import IParser
from src.etl.domain.value_objects import MessageMetadata
from src.etl.usecase.anonymiser import TelegramAnonymizer


class HTMLParser(IParser):
    def __init__(self, source_name: str = "telegram_html_export", anonymizer: Optional[TelegramAnonymizer] = None):
        self.source_name = source_name
        self.anonymizer = anonymizer

    async def parse_message(self, element: Any) -> MessageMetadata:
            from_node = element.select_one('.from_name')
            sender_id = from_node.get_text(strip=True) if from_node else "Unknown"
            text_node = element.select_one('.text')
            text = text_node.get_text(separator="\n", strip=True) if text_node else ""

            if self.anonymizer:
                sender_id = self.anonymizer._TelegramAnonymizer__get_label(sender_id, "PER")
                text = self.anonymizer._TelegramAnonymizer__process_text(text)
           
           
            attached_files = []
            for a in element.select('.photo_wrap'):
                if a.get("href"):
                    attached_files.append(a.get("href"))

            for title in element.select('.media_wrap .title'):
                attached_files.append(f"media_type: {title.get_text(strip=True)}")
            return MessageMetadata(
                chat_id=self.source_name,
                sender_id=sender_id,
                text=text,
                attached_files=attached_files
            )

    async def parse_batch(self, html_content: str) -> List[MessageMetadata]:
            try:
                soup = BeautifulSoup(html_content, 'lxml')
            except:
                soup = BeautifulSoup(html_content, 'html.parser')
            
            message_elements = soup.select('div.message.default')
            results = []
            for el in message_elements:
                if "service" in el.get("class", []):
                    continue    
                metadata = await self.parse_message(el)
                if metadata.text or metadata.attached_files:
                    results.append(metadata)
            final_results = []

            if self.anonymizer:
                for msg in results:
                    new_text = self.anonymizer._TelegramAnonymizer__process_text(msg.text)
                    new_msg = replace(msg, text=new_text)
                    final_results.append(new_msg)
            else:
                final_results = results

            return final_results
                    
class HTMLGrabber:
    def __init__(self, parser: IParser):
        self.parser = parser

    async def grab_from_file(self, file_path: str) -> List[MessageMetadata]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return await self.parser.parse_batch(content)
    
class YandexParser:
    def __init__(self, html_parser: HTMLParser):
        self.html_parser = html_parser

    async def parse(self, file_path: str) -> List[MessageMetadata]:
        """
        Принимает абсолютный путь к локальному ZIP-файлу.
        Распаковывает его во временную папку и парсит все HTML.
        """
        all_messages = []

        if not os.path.exists(file_path):
            logger.error(f"ZIP файл не найден по пути: {file_path}")
            raise FileNotFoundError(f"Файл {file_path} не существует")

        # 1. Создаем временную директорию
        with tempfile.TemporaryDirectory() as tmp_dir:
            extract_path = os.path.join(tmp_dir, "extracted")
            
            # 2. Распаковка
            try:
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)
            except zipfile.BadZipFile:
                logger.error(f"Файл {file_path} поврежден или не является ZIP-архивом")
                raise

            # 3. Рекурсивный обход распакованных файлов
            html_files_found = 0
            for root, _, files in os.walk(extract_path):
                # Сортируем файлы, чтобы сообщения шли в правильном порядке (messages1, messages2...)
                for file in sorted(files):
                    if file.endswith(".html"):
                        html_files_found += 1
                        file_full_path = os.path.join(root, file)
                        try:
                            with open(file_full_path, "r", encoding="utf-8") as f:
                                content = f.read()
                                # Вызываем HTMLParser для извлечения сообщений
                                messages = await self.html_parser.parse_batch(content)
                                all_messages.extend(messages)
                        except Exception as e:
                            logger.warning(f"Ошибка при чтении файла {file}: {e}")
        return all_messages

        return all_messages