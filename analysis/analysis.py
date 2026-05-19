import json
from collections import defaultdict
from pathlib import Path


def aggregate_experiment_metrics(folder1_name, folder2_name):
    # Структура для хранения суммы значений и их количества
    stats = defaultdict(lambda: defaultdict(lambda: {'sum': 0.0, 'count': 0}))

    folders = [folder1_name, folder2_name]

    for folder in folders:
        folder_path = Path(folder)
        if not folder_path.exists() or not folder_path.is_dir():
            print(f"Папка '{folder}' не найдена.")
            continue

        model_name = folder_path.name

        for filepath in folder_path.glob('*.json'):
            filename = filepath.name.lower()

            # Определение уровня промпта
            if filename.startswith('baseline'):
                prompt_level = 'baseline'
            elif filename.startswith('evolution'):
                prompt_level = 'evolution'
            else:
                continue

                # Строгое определение чистоты данных по вашему формату
            if filename.endswith('clean.json'):
                data_purity = 'clean'
            elif filename.endswith('raw.json'):
                data_purity = 'raw'
            else:
                continue

            combination_key = (model_name, prompt_level, data_purity)

            with open(filepath, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    print(f"Ошибка чтения JSON файла: {filepath}")
                    continue

                # Извлекаем метрики
                metrics = data.get('metrics', {})

                for question_id, metric_list in metrics.items():
                    for metric in metric_list:
                        m_type = metric.get('type')
                        m_value = metric.get('value')

                        # Если значение - число, добавляем в статистику
                        if m_type and isinstance(m_value, (int, float)):
                            clean_m_type = m_type.replace('MetricType.', '')
                            stats[combination_key][clean_m_type]['sum'] += m_value
                            stats[combination_key][clean_m_type]['count'] += 1

    print("=== Средние значения метрик по 8 комбинациям ===\n")

    # Вывод результатов
    for combo in sorted(stats.keys()):
        model, prompt, purity = combo
        print(f"Модель: {model} | Промпт: {prompt} | Данные: {purity}")
        print("-" * 50)

        metric_data = stats[combo]
        for m_type in sorted(metric_data.keys()):
            values = metric_data[m_type]
            if values['count'] > 0:
                avg = values['sum'] / values['count']
                print(f"  {m_type}: {avg:.4f}")
        print()


if __name__ == "__main__":
    FOLDER_1 = r"Ollama"
    FOLDER_2 = r"GPT"

    aggregate_experiment_metrics(FOLDER_1, FOLDER_2)