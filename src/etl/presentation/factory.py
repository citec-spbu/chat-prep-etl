import os
import socks
from telethon import TelegramClient
from dotenv import load_dotenv
from pathlib import Path
from typing import Optional

async def create_client(api_id: Optional[int] = None, api_hash: Optional[str] = None):
    """
    Создает клиент Telethon. 
    Приоритет: аргументы функции (из Swagger) -> переменные окружения / .env (серверные)
    """
    # Загружаем .env, если он есть локально
    env_path = Path(__file__).parent.parent.parent / ".env"
    if env_path.exists():
        load_dotenv(env_path)
    else:
        load_dotenv()
        
    # Если аргументы не переданы в функцию, берем из окружения системы
    final_api_id = api_id or os.getenv("TG_API_ID")
    final_api_hash = api_hash or os.getenv("TG_API_HASH")

    if not final_api_id or not final_api_hash:
        raise RuntimeError(
            "Telegram API credentials are missing! "
            "Pass them to create_client() or set TG_API_ID and TG_API_HASH env variables."
        )

    proxy = None
    proxy_addr = os.getenv("TG_PROXY_ADDR")
    if proxy_addr:
        proxy_type_str = os.getenv("TG_PROXY_TYPE", "socks5").lower()
        proxy_type = socks.SOCKS5 if proxy_type_str == "socks5" else socks.HTTP
        proxy_port = int(os.getenv("TG_PROXY_PORT", 10808))
        proxy = (proxy_type, proxy_addr, proxy_port, True)

    # Задаем уникальное имя сессии на основе api_id
    session_name = f"user_session_{final_api_id}"
    session_path = os.path.join(os.getcwd(), "sessions", session_name)
    os.makedirs(os.path.dirname(session_path), exist_ok=True)

    client = TelegramClient(session_path, int(final_api_id), final_api_hash, proxy=proxy)
    return client