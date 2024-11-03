import os

from dotenv import load_dotenv

load_dotenv(".env")

API_ID: int = os.getenv('API_ID', 26666537)
API_HASH: str = os.getenv('API_HASH', "6c2f0f671fbbfbfff8bca871a69c5692")

BOT_TOKEN = os.getenv("7648455672:AAEJrICgoCT9TxbpfJGxLEZsXLrC0FgGrQU")

OWNER_ID = int(os.getenv("7239918330"))

LOGS_MAKER_UBOT = int(os.getenv("-1002191896661"))

MAX_BOT = int(os.getenv("9999"))

RMBG_API = os.getenv("RMBG_API")

OPENAI_KEY = os.getenv("OPENAI_KEY")

MONGO_URL = os.getenv("mongodb+srv://kobieldstruick:kobieldstruick@cluster0.sep0l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster")
