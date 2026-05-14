import re
import emoji
import logging

from src.etl.domain.value_objects import MessageMetadata

#Логер
logging.basicConfig(level = logging.INFO, filename="test_servise/cleaning.log", filemode="w", encoding="utf-8", format = "%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("test_clean.log")

def remove_emoji(text):
    return emoji.replace_emoji(text, replace='')

def clean_text(text):
    if not text:
        return ""
    try:
        # удалить эмоциональные скобки в конце сообщения
        text = re.sub(r'[()]{2,}$', '', text).strip()

        # удалить эмодзи
        text = remove_emoji(text)

        #Убирает лишние пробелы перед знаками препинания
        text = re.sub(r'\s+([?!.,])', r'\1', text)

        # нижний регистр
        text = text.lower()

        # убрать переносы строк
        text = re.sub(r'\n+', ' ', text)

        # убрать повторяющиеся символы (!!! → !)
        text = re.sub(r'([!?.,])\1+', r'\1', text)

        # убрать лишние пробелы
        text = re.sub(r'\s+', ' ', text).strip()
        
        logger.info("Текст очищен")
        return text
    except Exception:
        logger.exception("Ошибка c очисткой")
        return ""

def build_attachment_text(attached_files):

    try:
        markers = []

        for file in (attached_files or []):
            file_lower = file.lower()

            if "stikers" in file_lower:
                markers.append("[STIKERS]")

            elif file_lower.endswith((".jpg", ".jpeg", ".png", ".webp")):
                markers.append("[IMAGE]")

            elif file_lower.endswith((
                ".mp4", ".avi", ".mov"
            )):
                markers.append("[VIDEO]")

            elif file_lower.endswith((
                ".ogg", ".mp3", ".wav"
            )):
                markers.append("[VOICE]")

            else:
                markers.append("[FILE]")

        logger.info("Маркеры поставлены")
        return " ".join(markers)
    
    except Exception:
        logger.exception("Ошибка c маркерами")
        return ""


def process_message(msg: MessageMetadata):
    logger.info("Начинаю обработку сообщений")

    #извлекаем текст из поля
    text = msg.text or ""

    #очистка текста
    text = clean_text(text)
    
    #маркеры вложений
    attached_files = msg.attached_files or []
    attachment_text = build_attachment_text(attached_files)

    # объединение
    if attachment_text:
        text = f"{text} {attachment_text}".strip()

    #проверка не остался после чистки текст пустой
    if not text.strip() and not msg.attached_files:
        logger.info("Сообщение пустое -> удаляем")
        return None
    
    result = MessageMetadata(
        chat_id = msg.chat_id,
        sender_id = msg.sender_id,
        text = text,
        attached_files = attached_files
    )
    logger.info("Ура, сообщение обработалось")
    return result


def clear_data(messages):
    logger.info(f"Начата очистка {len(messages)} сообщений")

    cleaned = []

    for msg in messages:
        processed = process_message(msg)
        if processed:
            cleaned.append(processed)

    logger.info(f"Очистка завершена. Итог: {len(cleaned)} сообщений")
    return cleaned