import json
from collections import defaultdict
from pathlib import Path
import pandas as pd


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

    rows = []
    for combo, metrics_dict in stats.items():
        model, prompt, purity = combo

        row_data = {
            'Модель': model,
            'Промпт': prompt,
            'Данные': purity
        }

        # Считаем среднее для каждой метрики в этой комбинации
        for m_type, values in metrics_dict.items():
            if values['count'] > 0:
                row_data[m_type] = round(values['sum'] / values['count'], 4)
            else:
                row_data[m_type] = None

        rows.append(row_data)

    df = pd.DataFrame(rows)
    fixed_cols = ['Модель', 'Промпт', 'Данные']
    metric_cols = sorted([col for col in df.columns if col not in fixed_cols])
    df = df[fixed_cols + metric_cols]
    df = df.sort_values(by=fixed_cols).reset_index(drop=True)
    return df


if __name__ == "__main__":
    FOLDER_1 = r"Ollama"
    FOLDER_2 = r"GPT"

    df = aggregate_experiment_metrics(FOLDER_1, FOLDER_2)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    print(df)


# анализ работы rag:
# в среднем система действительно извлекает близкие к запросу пользователя сообщения,
# но ответ на пользовательский запрос содержится в этих данных лишь процентов на 30%.
# Проблема видится в очень большем размере тестовой переписки и ее однотипности
# (обсуждаются различные проблемы пользователей с tesla)
# проблемы и потенциальные улучшения:
# - эмбеддинг модель в значительной мере "цепляется" за общие слова (машина, проблема, карты, ошибка).
# Можно попробовать игнорировать слова с низким idf (как считать?)
# - вероятно, более сильная эмбеддинг модель будет лучше кодировать семантику сообщений.
# Текущая sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2,
# переводящая сообщения в векторы размера 384 не справляется с поставленной задачей,
# модель c большей размерностью выходных векторов будет лучше улавливать контекст
# - можно варьировать параметр k, отвечающий за количество извлекаемых из базы сообщений,
# так как, чем выше k, тем больше контекст у отвечающей llm
#
# анализ работы llm:
# В силу того, что ответы ассистента прямо зависят от качества извлеченных из базы данных сообщений,
# качество ответов llm также не высоко. Тем не менее, при анализе проведенных экспериментов видно,
# что модель корректно использует переданные ей данные.