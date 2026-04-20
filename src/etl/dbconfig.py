import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("QDRANT_ENDPOINT")
api_key = os.getenv("QDRANT_API_KEY")
collection_name = "messages_test1"