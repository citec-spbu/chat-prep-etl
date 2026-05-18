import os
from telethon import TelegramClient
from dotenv import load_dotenv, set_key

async def create_client():
    # берем из переменных окружения
    dotenv_path = ".env"
    load_dotenv(dotenv_path)
    api_id = os.getenv("TG_API_ID")
    api_hash = os.getenv("TG_API_HASH")

    if not api_id or not api_hash:
        print("\n Настройка TelegramClient")
        api_id = input("Введите ваш API ID: ").strip()
        api_hash = input("Введите ваш API HASH: ").strip()
        
        # Сохраняем в текущую сессию процесса (или можно дописать в .env программно)
        set_key(dotenv_path, "TG_API_ID", api_id)
        set_key(dotenv_path, "TG_API_HASH", api_hash)

        os.environ["TG_API_ID"] = api_id
        os.environ["TG_API_HASH"] = api_hash


    proxy = None
    proxy_addr = os.getenv("TG_PROXY_ADDR")
    
    if not proxy_addr:
        answer = input("\n Использовать прокси (нужно для VPN/Happ)? (y/n): ").lower().strip()
        if answer == 'y':
            addr = input("Введите адрес (по умолчанию 127.0.0.1): ").strip() or "127.0.0.1"
            port = input("Введите порт (для Happ обычно 10808 или 1080): ").strip()
            ptype = input("Тип прокси (socks5/http, по умолчанию socks5): ").strip() or "socks5"
            

            set_key(dotenv_path, "TG_PROXY_ADDR", addr)
            set_key(dotenv_path, "TG_PROXY_PORT", port)
            set_key(dotenv_path, "TG_PROXY_TYPE", ptype)

            os.environ["TG_PROXY_ADDR"] = addr
            os.environ["TG_PROXY_PORT"] = port
            os.environ["TG_PROXY_TYPE"] = ptype
            proxy_addr = addr

    if proxy_addr:
        import socks
        proxy = (
            os.getenv("TG_PROXY_TYPE", "socks5"),
            os.getenv("TG_PROXY_ADDR"),
            int(os.getenv("TG_PROXY_PORT", 10808)),
            True 
        )
        print(f"{os.getenv('TG_PROXY_TYPE')}://{proxy_addr}")

    session_path = os.path.join(os.getcwd(), "sessions", "user_session")
    client = TelegramClient(session_path, int(api_id), api_hash, proxy=proxy)
    return client