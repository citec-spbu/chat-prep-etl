EXPERIMENTS = [
    {
        "id": "exp_1",
        "name": "Raw Experiment",
        "questions": [
            {
                "id": "q1",
                "text": "Какой размер алиментов?",
                "ground_true": "39 600 рублей"
            },
            {
                "id": "q2",
                "text": "Когда была последняя выплата?",
                "ground_true": "15 марта 2025"
            }
        ],
        "answers": [
            {
                "id": "q1",
                "text": "39 600 рублей в месяц"
            },
            {
                "id": "q2",
                "text": "Последняя выплата была 15 марта 2025"
            }
        ],
        "metrics": {
            "q1": {
                "bert_score": 0.94,
                "overlap": 1.0,
                "latency": 700
            },
            "q2": {
                "bert_score": 0.88,
                "overlap": 0.91,
                "latency": 820
            }
        }
    },
    {
        "id": "exp_2",
        "name": "Clean Experiment",
        "questions": [
            {
                "id": "q1",
                "text": "Как зовут клиента?",
                "ground_true": "Иван Петров"
            }
        ],
        "answers": [
            {
                "id": "q1",
                "text": "Клиента зовут Иван Петров"
            }
        ],
        "metrics": {
            "q1": {
                "bert_score": 0.97,
                "overlap": 1.0,
                "latency": 540
            }
        }
    }
]
