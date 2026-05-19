import streamlit as st
import requests
import time
from styles import load_css
from mock_data import EXPERIMENTS
from api import (check_health, run_ingest, search_messages, run_experiments, get_progress, get_experiments)
from components import render_experiments

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title= "Chat Preparation ETL", layout = "wide")

load_css()

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
    health_response = check_health()

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
                response = run_ingest(payload)

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
                response = search_messages(params)

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

        run_experiments_btn = st.button(
            "Run Experiments"
        )

        show_experiment_btn = st.button(
            "Show Experiments"
        )

    if run_experiments_btn:

        payload = {
            "experiments_path": experiments_path
        }

        try:
            with st.spinner("Running experiments..."):

                response = run_experiments(payload)

            data = response.json()

            if response.status_code == 202:

                st.success("Experiments started")

                progress_bar = st.progress(0)
                status_text = st.empty()

                while True:

                    progress_response = get_progress()

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
    

    if show_experiment_btn:
        data = EXPERIMENTS
        render_experiments(data)
    