import streamlit as st
import requests
import time
from styles import load_css
from mock_data import EXPERIMENTS
from api import (check_health_1, check_health_2, run_ingest, search_messages, run_experiments, get_progress, get_experiments, send_tg_code, tg_login)
from components import render_experiments, render_search_results

st.set_page_config(page_title="Chat Preparation ETL", layout="wide")

load_css()

# Язык по умолчанию
if "lang" not in st.session_state:
    st.session_state.lang = "RU"

TEXT = {
"RU": {
    "title": "Подготовка и обработка чатов",
    "upload": "Загрузка чата",
    "search": "Поиск по базе",
    "experiments_title": "Эксперименты",
    
    # Telegram блок
    "telegram_login": "🔑 Авторизация Telegram",
    "phone_number": "Номер телефона",
    "api_id": "API ID (опционально)",
    "api_hash": "API HASH (опционально)",
    "send_code": "Получить код",
    "telegram_code": "Код из Telegram",
    "telegram_password": "Пароль (2FA)",
    "login": "Подтвердить вход",
    "enter_phone": "Введите номер телефона",
    "enter_code": "Введите код из Telegram",
    "sending_code": "Отправка кода...",
    "code_sent": "Код отправлен в Telegram",
    "auth_success": "✅ Авторизация успешна",
    "already_authorized": "✅ Вы уже авторизованы!",
    "auth_error": "Ошибка",
    "authenticating": "Авторизация...",
    
    # Эксперименты
    "experiments": "Эксперименты",
    "experiments_count": "Количество экспериментов",
    "run_experiments": "Запустить эксперименты",
    "show_experiments": "Показать эксперименты",
    "running_experiments": "Запуск экспериментов...",
    "experiments_started": "✅ Эксперименты запущены",
    "completed": "Завершено",
    "no_data_to_display": "Нет данных для отображения",
    "experiments_control": "⚙️ Управление экспериментами",
    "experiments_results": "📊 Результаты экспериментов",
    
    "source_type": "Тип источника",
    "source_path": "Путь к данным / Ссылка",
    "question": "Поисковый запрос (Вопрос)",
    "chat_id": "ID чата (для сохранения)",
    "number_chat": "ID чата (для поиска)",
    "limit": "Лимит сообщений",
    "results_count": "Сколько результатов вернуть",
    "clean_mode": "Режим очистки данных",
    "download": "Запустить импорт (Ingest)",
    "ingest_success": "✅ Данные успешно загружены",
    "loading_data": "Загрузка данных...",
    "loading_search": "Поиск...",
    "enter_source": "Введите ссылку на загрузку данных",
    "enter_query": "Введите поисковый запрос",
    "nothing_found": "Ничего не найдено",
    "results_found": "Найдено результатов",
    "result": "Результат",
    "error": "Ошибка",
    "clean_none": "Без очистки (raw)",
    "clean_yes": "С очисткой (clean)",
    "clean_both": "Оба варианта (raw+clean)",
    "search_results": "Результаты поиска из векторной БД",
    "status": "Статус",
    "message": "Сообщение"
},

"EN": {
    "title": "Chat Preparation ETL",
    "upload": "Upload Chat",
    "search": "Vector Search",
    "experiments_title": "Experiments",
    
    # Telegram block
    "telegram_login": "🔑 Telegram Auth",
    "phone_number": "Phone Number",
    "api_id": "API ID (optional)",
    "api_hash": "API HASH (optional)",
    "send_code": "Send Code",
    "telegram_code": "Telegram Code",
    "telegram_password": "Password (2FA)",
    "login": "Login",
    "enter_phone": "Enter phone number",
    "enter_code": "Enter code from Telegram",
    "sending_code": "Sending code...",
    "code_sent": "Code sent to Telegram",
    "auth_success": "✅ Authorization successful",
    "already_authorized": "✅ Already authorized!",
    "auth_error": "Error",
    "authenticating": "Authenticating...",
    
    # Experiments
    "experiments": "Experiments",
    "experiments_count": "Experiments Count",
    "run_experiments": "Run Experiments",
    "show_experiments": "Show Experiments",
    "running_experiments": "Running experiments...",
    "experiments_started": "✅ Experiments started",
    "completed": "Completed",
    "no_data_to_display": "No data to display",
    "experiments_control": "⚙️ Experiments Control",
    "experiments_results": "📊 Experiments Results",
    
    "source_type": "Source Type",
    "source_path": "Data Source Path / URL",
    "question": "Search Query (Question)",
    "chat_id": "Chat ID (for saving)",
    "number_chat": "Chat ID (for search)",
    "limit": "Messages Limit",
    "results_count": "Results Count",
    "clean_mode": "Cleaning Mode",
    "download": "Run Ingest",
    "ingest_success": "✅ Data successfully loaded",
    "loading_data": "Loading data...",
    "loading_search": "Searching...",
    "enter_source": "Enter data source URL",
    "enter_query": "Enter search query",
    "nothing_found": "Nothing found",
    "results_found": "Results found",
    "result": "Result",
    "error": "Error",
    "clean_none": "Without Cleaning (raw)",
    "clean_yes": "With Cleaning (clean)",
    "clean_both": "Both Variants (raw+clean)",
    "search_results": "Search Results from Vector DB",
    "status": "Status",
    "message": "Message"
}
}

t = TEXT[st.session_state.lang]

# ==================== САЙДБАР (НАВИГАЦИЯ, СТАТУС, АВТОРИЗАЦИЯ) ====================
st.sidebar.image("https://img.icons8.com/fluency/96/chat.png", width=60)
st.sidebar.title("Навигация")

page = st.sidebar.radio(
    "Перейти к разделу:",
    [f"📝 {t['upload']}", f"🧪 {t['experiments']}"],
    label_visibility="collapsed"
)

# Проверка здоровья системы в сайдбаре
try:
    health_response = check_health_1()
    if health_response.status_code == 200:
        st.sidebar.success("🟢 ETL system up")
    else:
        st.sidebar.error("🔴 ETL system down")
    health_response_2 = check_health_2()
    if health_response_2.status_code == 200:
        st.sidebar.success("🟢 Testing system up")
    else:
        st.sidebar.error("🔴 Testing system down")
except Exception:
    st.sidebar.error("🔴 System Offline")

# --- БЛОК АВТОРИЗАЦИИ В САЙДБАРЕ ---
st.sidebar.markdown("---")
with st.sidebar.expander(t["telegram_login"], expanded=False):
    phone = st.text_input(t["phone_number"], placeholder="+79999999999", key="phone")
    api_id = st.text_input(t["api_id"], key="api_id")
    api_hash = st.text_input(t["api_hash"], type="password", key="api_hash")
    send_code_btn = st.button(t["send_code"], key="send_code_btn")
    
    st.markdown("---")
    code = st.text_input(t["telegram_code"], key="code")
    password = st.text_input(t["telegram_password"], type="password", key="password")
    login_btn = st.button(t["login"], key="login_btn")

# Обработка авторизации (Send Code)
if send_code_btn:
    if not phone:
        st.sidebar.warning(t["enter_phone"])
    else:
        payload = {"phone": phone, "api_id": api_id if api_id else None, "api_hash": api_hash if api_hash else None}
        try:
            with st.sidebar.spinner(t["sending_code"]):
                response = send_tg_code(payload)
            data = response.json()
            if response.status_code == 200:
                if data.get("message") == "Вы уже успешно авторизованы в системе!":
                    st.sidebar.success(t["already_authorized"])
                else:
                    st.sidebar.success(t["code_sent"])
            else:
                st.sidebar.error(f"{data.get('detail', 'Error')}")
        except Exception as e:
            st.sidebar.error(str(e))

# Обработка авторизации (Login)
if login_btn:
    if not phone: st.sidebar.warning(t["enter_phone"])
    elif not code: st.sidebar.warning(t["enter_code"])
    else:
        payload = {"phone": phone, "code": code}
        if password: payload["password"] = password
        try:
            with st.sidebar.spinner(t["authenticating"]):
                response = tg_login(payload)
            data = response.json()
            if response.status_code == 200:
                st.sidebar.success(t["auth_success"])
            else:
                st.sidebar.error(f"{data.get('detail', 'Error')}")
        except Exception as e:
            st.sidebar.error(str(e))


# Переключатель языка в самом низу сайдбара
st.sidebar.markdown("---")
st.sidebar.subheader("🌐 Язык / Language")
new_lang = st.sidebar.selectbox("Выберите язык", ["RU", "EN"], label_visibility="collapsed")
if new_lang != st.session_state.lang:
    st.session_state.lang = new_lang
    st.rerun()


# ==================== ОСНОВНОЙ КОНТЕНТ СТРАНИЦ ====================

if page == f"📝 {t['upload']}":
    st.title(t["title"])
    
    # Разделяем на 2 большие функциональные колонки (Загрузка данных и Поиск)
    col_upload, col_search = st.columns(2)
    
    # КОЛ ОНКА 1: ЗАГРУЗКА ДАННЫХ (INGEST)
    with col_upload:
        with st.container(border=True):
            st.header(f"📥 {t['upload']}")
            source_type = st.selectbox(t["source_type"], ["telegram", "yandex", "html"])
            source_path = st.text_input(t["source_path"])
            chat_id = st.number_input(t["chat_id"], value=0, step=1)
            limit = st.number_input(t["limit"], value=100, step=1)
            download = st.button(t["download"])
        
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
                data = response.json()
                
                if response.status_code in [200, 202]:
                    st.success(t["ingest_success"])
                    st.info(data.get("message", "Задача поставлена в очередь на обработку"))
                else:
                    st.error(f"{t['error']}: {response.status_code} - {data.get('detail', '')}")
            except Exception as e:
                st.error(str(e))
    
    # КОЛОНКА 2: СЕМАНТИЧЕСКИЙ ПОИСК В ВЕКТОРНОЙ БД
    with col_search:
        with st.container(border=True):
            st.header(f"🔍 {t['search']}")
            query = st.text_input(t["question"], key="query")
            number_chat = st.number_input(t["number_chat"], value=0, step=1, key="search_chat_id")
            k = st.number_input(t["results_count"], value=1, step=1, key="k")
            
            clean_options = {
                t["clean_none"]: "raw",
                t["clean_yes"]: "clean",
                t["clean_both"]: "raw+clean"
            }
            clean_mode = st.selectbox(t["clean_mode"], list(clean_options.keys()))
            search = st.button(t["search"], key="search_btn")
            
            st.divider()
            st.subheader(t["search_results"])
        
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
                    if results:
                        render_search_results(results, t)
                    else:
                        st.info(t["nothing_found"])
                else:
                    st.error(f"{t['error']}: {response.status_code} - {data.get('detail', '')}")
            except Exception as e:
                st.error(str(e))

# ==================== СТРАНИЦА 2: ЭКСПЕРИМЕНТЫ ====================
else:
    st.title(t["experiments_title"])
    control_col, results_col = st.columns([1, 2])
    
    with control_col:
        with st.container(border=True):
            st.subheader(t["experiments_control"])
            experiments_count = st.number_input(t["experiments_count"], min_value=1, max_value=100, value=5, step=1, key="exp_count")
            run_experiments_btn = st.button(t["run_experiments"], key="run_exp_btn", use_container_width=True)
            show_experiment_btn = st.button(t["show_experiments"], key="show_exp_btn", use_container_width=True)
    
    with results_col:
        with st.container(border=True):
            st.subheader(t["experiments_results"])
            
            if run_experiments_btn:
                    payload = {"experiments_path": None}
                    try:
                        with st.spinner(t["running_experiments"]):
                            response = run_experiments(payload)
                        data = response.json()
                        
                        if response.status_code == 202:
                            st.success(t["experiments_started"])
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
                                    status_text.info(f"{t['completed']}: {completed} / {total}")
                                if completed >= total and total > 0:
                                    break
                                time.sleep(1)
                            st.success("✅ Все эксперименты завершены!")
                        else:
                            st.error(f"{t['error']}: {response.status_code} - {data.get('detail', '')}")
                    except Exception as e:
                        st.error(str(e))
            
            if show_experiment_btn:
                    try:
                        with st.spinner(t["loading_experiments"]):
                            response = get_experiments(k=experiments_count)
                        if response.status_code == 200:
                            data = response.json()
                            if isinstance(data, list) and len(data) > 0:
                                render_experiments(data)
                            elif isinstance(data, dict) and "experiments" in data and data["experiments"]:
                                render_experiments(data["experiments"])
                            elif isinstance(data, dict) and "results" in data and data["results"]:
                                render_experiments(data["results"])
                            else:
                                st.warning(t["no_data_to_display"])
                        else:
                            st.error(f"{t['error']}: {response.status_code}")
                    except Exception as e:
                        st.error(str(e))