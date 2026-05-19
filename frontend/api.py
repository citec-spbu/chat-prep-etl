import requests

BACKEND_URL = "http://localhost:8000"

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