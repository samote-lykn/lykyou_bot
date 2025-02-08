import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Access variables
TOKEN = os.getenv("TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")

# MongoDB
MONGO_DB_URI = os.getenv("MONGO_DB_URI")
MONGO_DB_DATABASE = os.getenv("MONGO_DB_DATABASE")