import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Access variables
TOKEN = os.getenv("TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")

PORT = os.getenv("PORT")
# File to store chat IDs
CHAT_ID_TIKTOK_FILE = "chat_ids.json"