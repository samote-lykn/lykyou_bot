import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Access variables
TOKEN = os.getenv("TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")

API_KEY_YOUTUBE = os.getenv("API_KEY_YOUTUBE")
YOUTUBE_CHANNEL_ID = os.getenv("YOUTUBE_CHANNEL_ID")
PORT = os.getenv("PORT")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
REQUIRED_KEYWORD = os.getenv("REQUIRED_KEYWORD")

bot_api = f'https://api.telegram.org/bot{TOKEN}'