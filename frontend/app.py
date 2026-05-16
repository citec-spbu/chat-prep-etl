import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title= "Chat Preparation ETL", layout = "wide")

st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #111827 50%,
        #1e1b4b 100%
    );
}
/* CARDS */

[data-testid="column"] {

    background: rgba(30, 27, 75, 0.55);
    border-radius: 28px;
    padding: 28px;
    border: 1px solid rgba(139, 92, 246, 0.18);
    backdrop-filter: blur(18px);
}
            
/* TITLES */

h1 {
    color: white !important;
    font-size: 42px !important;
    font-weight: 700 !important;
}

h2, h3 {
    color: #c084fc !important;
}
/* INPUTS */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {

    background-color: rgba(255,255,255,0.03) !important;

    border-radius: 16px !important;

    border: 1px solid rgba(139,92,246,0.2) !important;

    color: white !important;
}
/* BUTTONS */

.stButton button {

    width: 100%;

    height: 54px;

    border-radius: 18px;

    border: none;

    background: linear-gradient(
        90deg,
        #7c3aed,
        #8b5cf6
    );

    color: white;

    font-size: 17px;

    font-weight: 600;

    transition: 0.3s ease;
}
/* HOVER */

.stButton button:hover {

    transform: scale(1.02);

    box-shadow: 0 0 24px rgba(139,92,246,0.35);
}

/* LABELS */

label {
    color: #d1d5db !important;
}

/* SUCCESS */

.stSuccess {
    border-radius: 16px;
}

/* WARNING */

.stWarning {
    border-radius: 16px;
}

/* RESULTS BLOCK */

.result-box {

    background: rgba(255,255,255,0.03);

    border-radius: 18px;

    padding: 18px;

    margin-bottom: 15px;

    border: 1px solid rgba(139,92,246,0.15);
}

</style>
""", unsafe_allow_html=True)


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

col1, col2 = st.columns(2)

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

        st.subheader("📄 Результаты поиска")

            
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