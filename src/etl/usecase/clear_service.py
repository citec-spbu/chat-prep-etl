import re
import emoji

from src.etl.domain.value_objects import MessageMetadata

def remove_emoji(text):
    return emoji.replace_emoji(text, replace='')

    
# ----------------------------
# Очистка текста
# ----------------------------
def clean_text(text):
    if not text:
        return ""

    # удалить эмодзи
    text = remove_emoji(text)

    # нижний регистр
    text = text.lower()

    # убрать переносы строк
    text = re.sub(r'\n+', ' ', text)

    # убрать повторяющиеся символы (!!! → !)
    text = re.sub(r'([!?.,])\1+', r'\1', text)

    # убрать лишние пробелы
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# ----------------------------
# Замена сущностей
# ----------------------------
def replace_entities(text):
    if not text:
        return ""

    # ссылки
    text = re.sub(r'http\S+', '[LINK]', text)

    # email
    text = re.sub(r'\S+@\S+', '[EMAIL]', text)

    # файлы (примерно)
    text = re.sub(r'\S+\.(pdf|docx|zip|png|jpg)', '[FILE]', text)

    return text


# ----------------------------
# Обработка одного сообщения
# ----------------------------
def process_message(msg: MessageMetadata):
    #извлекаем текст из поля
    text = msg.text or ""

    #чистим текст
    text = replace_entities(text)
    text = clean_text(text)
    
    #проверка не остался после чистки текст пустой
    if not text.strip():
        return None

    #наш результат
    return MessageMetadata(
        chat_id = msg.chat_id,
        sender_id = msg.sender_id,
        text = text,
        attached_files = msg.attached_files
    )

# ----------------------------
# Обработка всего списка
# ----------------------------
def clear_data(messages):
    cleaned = []

    for msg in messages:
        processed = process_message(msg)
        if processed:
            cleaned.append(processed)

    return cleaned