import os
import zipfile
import requests
import tempfile
import shutil
from typing import List, Any
from bs4 import BeautifulSoup
from src.etl.domain.interfaces import IParser
from src.etl.domain.value_objects import MessageMetadata


class HTMLParser(IParser):
    def __init__(self, source_name: str = "telegram_html_export"):
        self.source_name = source_name

    async def parse_message(self, element: Any) -> MessageMetadata:
            from_node = element.select_one('.from_name')
            sender_id = from_node.get_text(strip=True) if from_node else "Unknown"
            text_node = element.select_one('.text')
            text = text_node.get_text(separator="\n", strip=True) if text_node else ""
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
            return results
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
        self.base_url = "https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key="

    async def parse(self, public_key: str) -> List[MessageMetadata]:
        """
        public_key: ссылка на Яндекс.Диск
        """
        all_messages = []
        
        # 1. Создаем временную директорию для работы
        with tempfile.TemporaryDirectory() as tmp_dir:
            zip_path = os.path.join(tmp_dir, "download.zip")
            extract_path = os.path.join(tmp_dir, "extracted")

            # 2. Получаем прямую ссылку на скачивание через API Яндекса
            response = requests.get(f"{self.base_url}{public_key}")
            download_url = response.json().get('href')

            if not download_url:
                raise Exception("Не удалось получить ссылку на скачивание с Яндекс.Диска")

            # 3. Скачиваем ZIP
            with requests.get(download_url, stream=True) as r:
                with open(zip_path, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)

            # 4. Распаковываем
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)

            # 5. Ищем все HTML файлы в распакованном архиве и парсим их
            for root, dirs, files in os.walk(extract_path):
                for file in files:
                    if file.endswith(".html"):
                        file_full_path = os.path.join(root, file)
                        with open(file_full_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            # Используем наш HTMLParser для превращения текста в объекты
                            messages = await self.html_parser.parse_batch(content)
                            all_messages.extend(messages)

        return all_messages