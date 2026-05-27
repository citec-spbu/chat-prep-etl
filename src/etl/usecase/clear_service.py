import re
import emoji
import logging

from src.etl.domain.value_objects import MessageMetadata

logger = logging.getLogger(__name__)

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
    except Exception as e:
        logger.exception(f"Ошибка c очисткой: {e}")
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

        logger.info("Cleaner: Маркеры поставлены")
        return " ".join(markers)
    
    except Exception as e:
        logger.exception(f"Cleaner: Ошибка c маркерами: {e}")
        return ""


def process_message(msg: MessageMetadata):

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
        logger.info(f"Cleaner: Сообщение {msg.chat_id}:{msg.sender_id} пустое -> удаляем")
        return None
    
    result = MessageMetadata(
        chat_id = msg.chat_id,
        sender_id = msg.sender_id,
        text = text,
        attached_files = attached_files
    )
    return result


def clear_data(messages):
    logger.info(f"Cleaner: Начата очистка {len(messages)} сообщений")

    cleaned = []

    for msg in messages:
        processed = process_message(msg)
        if processed:
            cleaned.append(processed)

    logger.info(f"Cleaner: Очистка завершена. Итог: {len(cleaned)} сообщений")
    return cleaned