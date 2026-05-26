import requests
from streamlit import cache_data

BACKEND_URL_1 = "http://127.0.0.1:8067"
BACKEND_URL_2 = "http://100.106.4.6:8881" 


@cache_data(ttl=10)
def check_health_1():

    return requests.get(
        f"{BACKEND_URL_1}/health"
    )
@cache_data(ttl=10)
def check_health_2():
    return requests.get(
        f"{BACKEND_URL_2}/health"
    )

def run_ingest(payload):

    return requests.post(
        f"{BACKEND_URL_1}/ingest",
        json=payload
    )


def search_messages(params):

    return requests.get(
        f"{BACKEND_URL_1}/search",
        params=params
    )


def run_experiments(payload):

    return requests.post(
        f"{BACKEND_URL_2}/experiments/run",
        json=payload
    )


def get_progress():

    return requests.get(
        f"{BACKEND_URL_2}/experiments/progress"
    )


def get_experiments(k: int = None):

    url = f"{BACKEND_URL_2}/experiments"
    
    if k is not None:
        return requests.get(url, params={"k": k})
    else:
        return requests.get(url)

def send_tg_code(payload):
    return requests.post(
        f"{BACKEND_URL_1}/tg/send-code",
        json=payload
    )


def tg_login(payload):
    return requests.post(
        f"{BACKEND_URL_1}/tg/login",
        json=payload
    )