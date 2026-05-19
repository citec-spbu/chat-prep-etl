import streamlit as st
import requests
import time

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title= "Chat Preparation ETL", layout = "wide")


#язык по умолчанию
if "lang" not in st.session_state:
    st.session_state.lang = "RU"
left, right = st.columns([10, 1])

with right:
    st.session_state.lang = st.selectbox(
        "",
        ["RU", "EN"],
        label_visibility="collapsed"
    )
TEXT = {
"RU": {
    "title": "Подготовка и обработка чатов",
    "upload": "Загрузка чата",
    "search": "Поиск",

    "source_type": "Тип источника",
    "source_path": "Ссылка на загрузку данных",

    "question": "Вопрос",

    "chat_id": "Chat ID",
    "number_chat": "Номер чата",

    "limit": "Лимит",
    "results_count": "Количество ответов",

    "clean_mode": "Очистка",

    "download": "Скачать",

    "loading_data": "Загрузка данных...",
    "loading_search": "Поиск...",

    "enter_source": "Введите ссылку на загрузку данных",
    "enter_query": "Введите поисковый запрос",

    "nothing_found": "Ничего не найдено",

    "results_found": "Найдено результатов",

    "result": "Результат",

    "error": "Ошибка",

    "clean_none": "Без очистки",
    "clean_yes": "С очисткой",
    "clean_both": "Оба варианта"
},

"EN": {
    "title": "Chat Preparation ETL",
    "upload": "Upload Chat",
    "search": "Search",

    "source_type": "Source Type",
    "source_path": "Data Source URL",

    "question": "Question",

    "chat_id": "Chat ID",
    "number_chat": "Chat Number",

    "limit": "Limit",
    "results_count": "Results Count",

    "clean_mode": "Cleaning",

    "download": "Download",
    "search": "Search",

    "loading_data": "Loading data...",
    "loading_search": "Searching...",

        
    "enter_source": "Enter data source URL",
    "enter_query": "Enter search query",

    "nothing_found": "Nothing found",

    "results_found": "Results found",

    "result": "Result",

    "error": "Error",

    "clean_none": "Without Cleaning",
    "clean_yes": "With Cleaning",
    "clean_both": "Both Variants"
}
}

t = TEXT[st.session_state.lang]
st.title(t["title"])

try:
    health_response = requests.get(f"{BACKEND_URL}/health")

    if health_response.status_code == 200:
        st.success("🟢 Backend Online")

    else:
        st.error("🔴 Backend Error")

except Exception:
    st.error("🔴 Backend Offline")

col1, col2, col3 = st.columns(3)

#------POST BLOCK-----
with col1:
    with st.container(border=True):
        st.header(t["upload"])
        source_type = st.selectbox(t["source_type"],
        ["telegram", "yandex", "html"]
        )

        source_path = st.text_input(t["source_path"])
        chat_id = st.number_input(t["chat_id"], value=0, step=1)
        limit = st.number_input(t["limit"], value=100, step=1)

        download = st.button(t["download"])

    #Подключаю POST
    if download:
        if not source_path:
            st.warning(t["enter_source"])
            st.stop()

        payload = {
            "source_type": source_type,
            "source_path": source_path,
            "chat_id": int(chat_id),
            "limit": int(limit)
        }

        try:
            with st.spinner(t["loading_data"]):
                response = requests.post(
                    f"{BACKEND_URL}/ingest",
                    json=payload
                )

            st.write(response.status_code)
            st.json(response.json())

        except Exception as e:
            st.error(str(e))

#-----GET BlOK-----
with col2:
    with st.container(border=True):
        st.header(t["search"])
        query = st.text_input(t["question"])

        number_chat = st.number_input(t["number_chat"], value=0, step=1, key="search_chat_id")
        k = st.number_input(t["results_count"], value=1, step=1)
        clean_options = {
            t["clean_none"]: "raw",
            t["clean_yes"]: "clean",
            t["clean_both"]: "raw+clean"
        }

        clean_mode = st.selectbox(
            t["clean_mode"],
            list(clean_options.keys())
        )

        search = st.button(t["search"])

        st.divider()

        st.subheader("Результаты поиска")

            
    #Подключаю GET
    if search:
        if not query:
            st.warning(t["enter_query"])
            st.stop()

        params = {
            "query": query,
            "chat_id": int(number_chat),
            "k": int(k),
            "clean": clean_options[clean_mode]
        }

        try:
            with st.spinner(t["loading_search"]):
                response = requests.get(
                    f"{BACKEND_URL}/search",
                    params=params
                )

            data = response.json()

            if response.status_code == 200:

                results = data.get("results", [])

                if not results:
                    st.warning(t["nothing_found"])

                else:
                    st.success(f"{t['results_found']}: {len(results)}")

                    for i, result in enumerate(results, start=1):

                        st.subheader(f"{t['result']} {i}")

                        st.markdown(
                            f'''
                            <div class="result-box">
                                <h4 style="color:#c084fc;">{t["result"]} {i}</h4>
                                <p style="color:white;">{result}</p>
                            </div>
                            ''',
                            unsafe_allow_html=True
                        )

            else:
                st.error(f"{t['error']}: {response.status_code}")
                st.json(data)

        except Exception as e:
            st.error(str(e))

#-----EXPERIMENTS BLOCK-----
with col3:
    with st.container(border=True):

        st.header("Experiments")

        experiments_path = st.text_input(
            "Experiments Path"
        )

        run_experiments = st.button(
            "Run Experiments"
        )

        show_experiments = st.button(
            "Show Experiments"
        )

    if run_experiments:

        payload = {
            "experiments_path": experiments_path
        }

        try:
            with st.spinner("Running experiments..."):

                response = requests.post(
                    f"{BACKEND_URL}/experiments/run",
                    json=payload
                )

            data = response.json()

            if response.status_code == 202:

                st.success("Experiments started")

                progress_bar = st.progress(0)
                status_text = st.empty()

                while True:

                    progress_response = requests.get(
                        f"{BACKEND_URL}/experiments/progress"
                    )

                    progress_data = progress_response.json()

                    total = progress_data.get("total", 0)
                    completed = progress_data.get("completed", 0)

                    if total > 0:

                        progress_value = completed / total

                        progress_bar.progress(progress_value)

                        status_text.info(
                            f"Completed: {completed} / {total}"
                        )

                    if completed >= total and total > 0:
                        break

                    time.sleep(1)

            else:
                st.error(f"Error: {response.status_code}")

                st.json(data)

        except Exception as e:
            st.error(str(e))
    

    if show_experiments:

        data = [
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

        if not data:
            st.warning("No experiments found")

        for exp in data:

            exp_name = exp.get("name", "Experiment")
            exp_id = exp.get("id", "unknown")

            with st.expander(
                f"📋 {exp_name} ({exp_id})"
            ):

                questions = exp.get("questions", [])
                answers = exp.get("answers", [])
                metrics = exp.get("metrics", {})

                answers_map = {
                    a["id"]: a for a in answers
                }

                for q in questions:

                    st.markdown(
                        f"""
                        <div class="result-box">
                            <p style="color:#c084fc;">
                                ❓ <b>{q.get("id", "")}</b>
                            </p>
                                {q.get("text", "")}
                            </p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if q.get("ground_true"):

                        st.success(
                            f"🎯 {q['ground_true']}"
                        )

                    answer = answers_map.get(
                        q.get("id")
                    )

                    if answer and answer.get("text"):

                        st.info(
                            f"🤖 {answer['text']}"
                        )

                        metric_data = metrics.get(
                            answer["id"],
                            {}
                        )

                        st.json(metric_data)

                    else:
                        st.warning(
                            "No answer yet"
                        )