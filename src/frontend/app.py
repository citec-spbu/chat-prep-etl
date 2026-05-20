import streamlit as st
import requests
import time
from styles import load_css
from mock_data import EXPERIMENTS
from api import (check_health, run_ingest, search_messages, run_experiments, get_progress, get_experiments, send_tg_code, tg_login)
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
    "search": "Поиск",
    "experiments_title": "Эксперименты",
    
    # Telegram блок
    "telegram_login": "Telegram Авторизация",
    "phone_number": "Номер телефона",
    "api_id": "API ID",
    "api_hash": "API HASH",
    "send_code": "Отправить код",
    "telegram_code": "Код из Telegram",
    "telegram_password": "Пароль Telegram (2FA)",
    "login": "Войти",
    "enter_phone": "Введите номер телефона",
    "enter_code": "Введите код из Telegram",
    "sending_code": "Отправка кода...",
    "code_sent": "Код отправлен в Telegram",
    "auth_success": "✅ Авторизация успешна",
    "already_authorized": "✅ Вы уже успешно авторизованы в системе!",
    "auth_error": "Ошибка",
    "authenticating": "Авторизация...",
    
    # Эксперименты
    "experiments": "Эксперименты",
    "experiments_path": "Путь к экспериментам",
    "experiments_count": "Количество экспериментов",
    "run_experiments": "Запустить эксперименты",
    "show_experiments": "Показать эксперименты",
    "running_experiments": "Запуск экспериментов...",
    "experiments_started": "✅ Эксперименты запущены",
    "completed": "Завершено",
    "no_experiments_path": "Введите путь к экспериментам",
    "loading_experiments": "Загрузка экспериментов...",
    "no_data_to_display": "Нет данных для отображения",
    "experiments_control": "⚙️ Управление экспериментами",
    "experiments_results": "📊 Результаты экспериментов",
    
    "source_type": "Тип источника",
    "source_path": "Ссылка на загрузку данных",
    "question": "Вопрос",
    "chat_id": "Chat ID",
    "number_chat": "Номер чата",
    "limit": "Лимит",
    "results_count": "Количество ответов",
    "clean_mode": "Очистка",
    "download": "Скачать",
    "ingest_success": "✅ Данные успешно загружены",
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
    "clean_both": "Оба варианта",
    "search_results": "Результаты поиска",
    "status": "Статус",
    "message": "Сообщение"
},

"EN": {
    "title": "Chat Preparation ETL",
    "upload": "Upload Chat",
    "search": "Search",
    "experiments_title": "Experiments",
    
    # Telegram block
    "telegram_login": "Telegram Login",
    "phone_number": "Phone Number",
    "api_id": "API ID",
    "api_hash": "API HASH",
    "send_code": "Send Code",
    "telegram_code": "Telegram Code",
    "telegram_password": "Telegram Password (2FA)",
    "login": "Login",
    "enter_phone": "Enter phone number",
    "enter_code": "Enter code from Telegram",
    "sending_code": "Sending code...",
    "code_sent": "Code sent to Telegram",
    "auth_success": "✅ Authorization successful",
    "already_authorized": "✅ You are already authorized in the system!",
    "auth_error": "Error",
    "authenticating": "Authenticating...",
    
    # Experiments
    "experiments": "Experiments",
    "experiments_path": "Experiments Path",
    "experiments_count": "Experiments Count",
    "run_experiments": "Run Experiments",
    "show_experiments": "Show Experiments",
    "running_experiments": "Running experiments...",
    "experiments_started": "✅ Experiments started",
    "completed": "Completed",
    "no_experiments_path": "Enter experiments path",
    "loading_experiments": "Loading experiments...",
    "no_data_to_display": "No data to display",
    "experiments_control": "⚙️ Experiments Control",
    "experiments_results": "📊 Experiments Results",
    
    "source_type": "Source Type",
    "source_path": "Data Source URL",
    "question": "Question",
    "chat_id": "Chat ID",
    "number_chat": "Chat Number",
    "limit": "Limit",
    "results_count": "Results Count",
    "clean_mode": "Cleaning",
    "download": "Download",
    "ingest_success": "✅ Data successfully loaded",
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
    "clean_both": "Both Variants",
    "search_results": "Search Results",
    "status": "Status",
    "message": "Message"
}
}

t = TEXT[st.session_state.lang]

# Создаем навигацию
st.sidebar.image("https://img.icons8.com/fluency/96/chat.png", width=80)
st.sidebar.title("Навигация")

# Выбор страницы
page = st.sidebar.radio(
    "Перейти к разделу:",
    [f"📝 {t['upload']}", f"🧪 {t['experiments']}"],
    label_visibility="collapsed"
)

# Переключатель языка в сайдбаре
st.sidebar.markdown("---")
st.sidebar.subheader("🌐 Язык / Language")
new_lang = st.sidebar.selectbox(
    "Выберите язык",
    ["RU", "EN"],
    label_visibility="collapsed"
)

if new_lang != st.session_state.lang:
    st.session_state.lang = new_lang
    st.rerun()

# Заголовок в зависимости от страницы
if page == f"📝 {t['upload']}":
    st.title(t["title"])
else:
    st.title(t["experiments_title"])

# Проверка здоровья системы
try:
    health_response = check_health()
    if health_response.status_code == 200:
        st.sidebar.success("🟢 System up")
    else:
        st.sidebar.error("🔴 System down")
except Exception:
    st.sidebar.error("🔴 System Offline")

# Функция для красивого вывода ответа API
def render_api_response(data, success_message=None):
    if isinstance(data, dict):
        status = data.get("status")
        message = data.get("message")
        
        if status == "success" or status == "ok":
            if success_message:
                st.success(success_message)
            elif message:
                st.success(f" {message}")
            else:
                st.success(" Успешно")
        elif status == "error":
            st.error(f" {message if message else 'Ошибка'}")
        else:
            if message:
                st.info(f" {message}")
    else:
        st.write(data)

# ==================== СТРАНИЦА 1: ОБРАБОТКА ЧАТОВ ====================
if page == f"📝 {t['upload']}":
    
    col1, col2, col3 = st.columns(3)
    
    # ------TG AUTH BLOCK-----
    with col1:
        with st.container(border=True):
            st.header(t["telegram_login"])
            
            phone = st.text_input(
                t["phone_number"],
                placeholder="+79999999999",
                key="phone"
            )
            
            api_id = st.text_input(t["api_id"], key="api_id")
            api_hash = st.text_input(t["api_hash"], key="api_hash")
            
            send_code_btn = st.button(t["send_code"], key="send_code_btn")
            code = st.text_input(t["telegram_code"], key="code")
            password = st.text_input(t["telegram_password"], type="password", key="password")
            login_btn = st.button(t["login"], key="login_btn")
        
        if send_code_btn:
            if not phone:
                st.warning(t["enter_phone"])
                st.stop()
            
            payload = {
                "phone": phone,
                "api_id": api_id,
                "api_hash": api_hash
            }
            
            try:
                with st.spinner(t["sending_code"]):
                    response = send_tg_code(payload)
                data = response.json()
                
                if response.status_code == 200:
                    if data.get("message") == "Вы уже успешно авторизованы в системе!":
                        st.success(t["already_authorized"])
                    else:
                        render_api_response(data, t["code_sent"])
                else:
                    st.error(f"{t['auth_error']}: {response.status_code}")
                    if data.get("message"):
                        st.error(f"{data['message']}")
            except Exception as e:
                st.error(str(e))
        
        if login_btn:
            if not phone:
                st.warning(t["enter_phone"])
                st.stop()
            if not code:
                st.warning(t["enter_code"])
                st.stop()
            
            payload = {"phone": phone, "code": code}
            if password:
                payload["password"] = password
            
            try:
                with st.spinner(t["authenticating"]):
                    response = tg_login(payload)
                data = response.json()
                
                if response.status_code == 200:
                    if data.get("message") == "Вы уже успешно авторизованы в системе!":
                        st.success(t["already_authorized"])
                    else:
                        render_api_response(data, t["auth_success"])
                else:
                    st.error(f"{t['auth_error']}: {response.status_code}")
                    if data.get("message"):
                        st.error(f" {data['message']}")
            except Exception as e:
                st.error(str(e))
    
    # ------POST BLOCK-----
    with col2:
        with st.container(border=True):
            st.header(t["upload"])
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
                
                if response.status_code == 200 or response.status_code == 202:
                    st.success(t["ingest_success"])
                    if data.get("message"):
                        st.info(f" {data['message']}")
                    else:
                        st.info("Задача поставлена в очередь на обработку")
                else:
                    st.error(f"{t['error']}: {response.status_code}")
                    if data.get("message"):
                        st.error(f" {data['message']}")
            except Exception as e:
                st.error(str(e))
    
    # -----GET BLOCK-----
    with col3:
        with st.container(border=True):
            st.header(t["search"])
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
                    st.error(f"{t['error']}: {response.status_code}")
                    if data.get("message"):
                        st.error(f" {data['message']}")
            except Exception as e:
                st.error(str(e))

# ==================== СТРАНИЦА 2: ЭКСПЕРИМЕНТЫ ====================
else:
    
    control_col, results_col = st.columns([1, 2])
    
    with control_col:
        with st.container(border=True):
            st.subheader(t["experiments_control"])
            
            experiments_count = st.number_input(
                t["experiments_count"],
                min_value=1,
                max_value=100,
                value=5,
                step=1,
                key="exp_count"
            )
            
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
                            st.error(f"{t['error']}: {response.status_code}")
                            if data.get("message"):
                                st.error(f" {data['message']}")
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
                            data = response.json()
                            if data.get("message"):
                                st.error(f" {data['message']}")
                    except Exception as e:
                        st.error(str(e))