import asyncio
from src.etl.adapter.yd_parser import HTMLParser
from src.etl.usecase.anonymiser import TelegramAnonymizer
import os
import json

async def test_parser():
    # Твой HTML контент (вставь сюда фрагмент или читай из файла)
    html_content = "zipdata/ChatExport_2026-04-28/messages.html"  # Путь к тестовому HTML файлу
    with open(html_content, "r", encoding="utf-8") as f:
            html_content = f.read()
    anonymizer = TelegramAnonymizer()
    parser = HTMLParser(anonymizer=anonymizer)

    # 2. ПРОВЕРКА: Что реально уходит в парсер
    print(f"Длина контента для парсинга: {len(html_content)} символов")
    
    messages = await parser.parse_batch(html_content)

    for m in messages:
        print(f"Отправитель: {m.sender_id} | Текст: {m.text}")
    
    data_to_save = [vars(m) for m in messages]

    with open("messages_dump_.json", "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)

    print(f"Сохранено {len(data_to_save)} сообщений.")

if __name__ == "__main__":
    asyncio.run(test_parser())