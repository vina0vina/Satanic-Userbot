import os

from dotenv import load_dotenv

load_dotenv(".env")

API_ID: int = os.getenv('API_ID', 22353526)
API_HASH: str = os.getenv('API_HASH', "ca3bc21bc1f8970fc12ad76790ff8e0e")

BOT_TOKEN = os.getenv("7331678485:AAGvdOPCUwxP3y-5-feW-BlRyT7juo-a-6E")

OWNER_ID = int(os.getenv("6960845020"))

LOGS_MAKER_UBOT = int(os.getenv("-4590999823"))

MAX_BOT = int(os.getenv("9999"))

RMBG_API = os.getenv("RMBG_API")

OPENAI_KEY = os.getenv("OPENAI_KEY")

MONGO_URL = os.getenv("mongodb+srv://kobieldstruick:kobieldstruick@cluster0.sep0l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster")
