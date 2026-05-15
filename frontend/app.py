import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title= "Chat Preparation ETL", layout = "wide")

st.title("Chat Preparation ETL")

col1, col2 = st.columns(2)

#POST BLOCK
with col1:
    st.header("Загрузка чата")
    source_type = st.selectbox("Тип источника", ["telegram", "yandex", "html"])

    source_path = st.text_input("Ссылка на загрузку данных")
    chat_id = st.number_input("Chat ID", value=0, step=1)
    limit = st.number_input("Limit", value=100, step=1)

    download_button = st.button("Скачать")

#GET BlOK
with col2:
    st.header("Поиск")
    query = st.text_input("Вопрос")

    search_chat_id = st.number_input("Номер чата", value=0, step=1, key="search_chat_id")
    k = st.number_input("Количество ответов", value=1, step=1)
    clean_mode = st.selectbox("Очистка", ["Без очистки", "С очисткой", "Оба варианта"])

    search_button = st.button("Поиск")

#Подключаю POST
if download_button:
    if not source_path:
        st.warning("Введите ссылку на загрузку данных")
        st.stop()

    payload = {
        "source_type": source_type,
        "source_path": source_path,
        "chat_id": int(chat_id),
        "limit": int(limit)
    }

    try:
        with st.spinner("Загрузка данных..."):
            response = requests.post(
                f"{BACKEND_URL}/ingest",
                json=payload
            )

        st.write(response.status_code)
        st.json(response.json())

    except Exception as e:
        st.error(str(e))


#Подключаю GET
if search_button:
    if not query:
        st.warning("Введите поисковый запрос")
        st.stop()

    clean_mapping = {
        "Без очистки": "raw",
        "С очисткой": "clean",
        "Оба варианта": "raw+clean"
        }

    params = {
        "query": query,
        "chat_id": int(search_chat_id),
        "k": int(k),
        "clean": clean_mapping[clean_mode]
    }

    try:
        with st.spinner("Поиск..."):
            response = requests.get(
                f"{BACKEND_URL}/search",
                params=params
            )

        data = response.json()

        if response.status_code == 200:

            results = data.get("results", [])

            if not results:
                st.warning("Ничего не найдено")

            else:
                st.success(f"Найдено результатов: {len(results)}")

                for i, result in enumerate(results, start=1):

                    st.subheader(f"Результат {i}")

                    st.write(result)

                    st.divider()

        else:
            st.error(f"Ошибка: {response.status_code}")
            st.json(data)

    except Exception as e:
        st.error(str(e))
