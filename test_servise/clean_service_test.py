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
    #Удаления ненужных скобок после сообщений
    text = re.sub(r'\s?[()]{1,}\s?', ' ', text)

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



# ----------------------------
# Обработка одного сообщения
# ----------------------------
def process_message(msg: MessageMetadata):
    #извлекаем текст из поля
    text = msg.text or ""

    #чистим текст
    text = clean_text(text)
    
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