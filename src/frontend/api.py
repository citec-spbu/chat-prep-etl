import requests

BACKEND_URL = "http://localhost:8000"

def check_health():

    return requests.get(
        f"{BACKEND_URL}/health"
    )


def run_ingest(payload):

    return requests.post(
        f"{BACKEND_URL}/ingest",
        json=payload
    )


def search_messages(params):

    return requests.get(
        f"{BACKEND_URL}/search",
        params=params
    )


def run_experiments(payload):

    return requests.post(
        f"{BACKEND_URL}/experiments/run",
        json=payload
    )


def get_progress():

    return requests.get(
        f"{BACKEND_URL}/experiments/progress"
    )


def get_experiments():

    return requests.get(
        f"{BACKEND_URL}/experiments"
    )

def send_tg_code(payload):
    return requests.post(
        f"{BACKEND_URL}/tg/send-code",
        json=payload
    )


def tg_login(payload):
    return requests.post(
        f"{BACKEND_URL}/tg/login",
        json=payload
    )