import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent.parent / ".env"
if env_path.exists():
    load_dotenv(env_path)
else:
    load_dotenv()

url = os.getenv("QDRANT_ENDPOINT") or os.getenv("QDRANT_URL")
api_key = os.getenv("QDRANT_API_KEY")

if api_key:
    api_key = api_key.strip()

collection_name = os.getenv("QDRANT_COLLECTION_NAME", "messages")
test_collection_name = os.getenv("QDRANT_TEST_COLLECTION_NAME", "messages_test")

missing = [
    name
    for name, value in {
            "QDRANT_ENDPOINT": url,
            "QDRANT_API_KEY": api_key,
            "QDRANT_COLLECTION_NAME": collection_name,
            "QDRANT_TEST_COLLECTION_NAME": test_collection_name,
    }.items()
    if not value
    ]

if missing:
    raise RuntimeError(f"Missing required Qdrant settings: {', '.join(missing)}")