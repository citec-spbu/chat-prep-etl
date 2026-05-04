import asyncio
from src.etl.adapter.yd_parser import HTMLParser
import os


async def test_parser():
    # Твой HTML контент (вставь сюда фрагмент или читай из файла)
    html_content = "zipdata/ChatExport_2026-04-28/messages.html"  # Путь к тестовому HTML файлу
    if not os.path.exists(html_content):
            # Если файла нет, используем строку для теста
            print("Файл не найден, используем захардкоженную строку...")
            html_content = """
            <div class="message default clearfix">
                <div class="from_name">Константин</div>
                <div class="text">Привет, это тест 1</div>
            </div>
            <div class="message default clearfix">
                <div class="from_name">Dzen</div>
                <div class="text">Привет, это тест 2</div>
            </div>
            """
    else:
        # ЧИТАЕМ ФАЙЛ
        with open(html_content, "r", encoding="utf-8") as f:
            html_content = f.read()

    parser = HTMLParser()
    
    # 2. ПРОВЕРКА: Что реально уходит в парсер
    print(f"Длина контента для парсинга: {len(html_content)} символов")
    
    messages = await parser.parse_batch(html_content)

    print(f"Найдено сообщений: {len(messages)}")
    
    for m in messages:
        print(f"Отправитель: {m.sender_id} | Текст: {m.text[:30]}")

    assert len(messages) >= 2, f"Ожидали >= 2, получили {len(messages)}"

if __name__ == "__main__":
    asyncio.run(test_parser())