import re
import emoji

from src.etl.domain.value_objects import MessageMetadata

def remove_emoji(text):
    return emoji.replace_emoji(text, replace='')


def clean_text(text):
    if not text:
        return ""
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

    return text

def build_attachment_text(attached_files):
    markers = []

    for file in attached_files:
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

    return " ".join(markers)


def process_message(msg: MessageMetadata):
    #извлекаем текст из поля
    text = msg.text or ""

    #очистка текста
    text = clean_text(text)
    
    #маркеры вложений
    attachment_text = build_attachment_text(msg.attached_files)

    # объединение
    if attachment_text:
        text = f"{text} {attachment_text}".strip()

    #проверка не остался после чистки текст пустой
    if not text.strip() and not msg.attached_files:
        return None

    #наш результат
    return MessageMetadata(
        chat_id = msg.chat_id,
        sender_id = msg.sender_id,
        text = text,
        attached_files = msg.attached_files
    )


def clear_data(messages):
    cleaned = []

    for msg in messages:
        processed = process_message(msg)
        if processed:
            cleaned.append(processed)

    return cleaned