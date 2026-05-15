import json
from dataclasses import asdict
from src.etl.usecase.clear_service import clear_data
from src.etl.domain.value_objects import MessageMetadata

def run_clean_pipeline(input_path, output_path):
    #1.Загрузка данных
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            raw_json = json.load(f)
    except FileNotFoundError:
        print(f"Файл {input_path} не найден")
        return
    
    # 2. Превращаем словари в объекты MessageMetadata
    messages = []
    for item in raw_json:
        msg = MessageMetadata(
            chat_id=item.get('chat_id'),
            sender_id=item.get('sender_id'),
            text=item.get('text'),
            attached_files=item.get('attached_files', [])
        )
        messages.append(msg)

     # 3. Очистка
    cleaned_objects = clear_data(messages)

    # 4. Превращаем обратно в список словарей для сохранения
    result_data = [asdict(m) for m in cleaned_objects]

    # 5. Сохранение результата
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result_data, f, ensure_ascii=False, indent=4)
    
    print(f"Готово! Сохранено {len(result_data)} сообщений в {output_path}")

# Пример запуска
import os

if __name__ == "__main__":
        base_path = r"C:\Users\Alina\Desktop\chat-prep-etl\test_servise"
        files = os.listdir(base_path)
        target = "messages3_dump.json"
        if target in files:
            print(f"\nФайл '{target}' найден. Запускаю очистку...")
            run_clean_pipeline(os.path.join(base_path, target), 
                                 os.path.join(base_path, "cleaned_results(mes_3).json"))
        else:
            print(f"\nФайла '{target}' нет в списке выше.")



