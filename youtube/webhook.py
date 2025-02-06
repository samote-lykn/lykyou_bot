from flask import Flask, request
import requests
import json
import config
from youtube.config import CHAT_ID_FILE

URL = f"https://api.telegram.org/bot{config.TOKEN}"

app = Flask(__name__)

def load_chat_ids():
    """Load chat IDs from file."""
    try:
        with open(CHAT_ID_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_chat_ids(chat_ids):
    """Save chat IDs to file."""
    with open(CHAT_ID_FILE, "w") as f:
        json.dump(chat_ids, f)

@app.route(f"/{config.TOKEN}", methods=["POST"])
def receive_update():
    """Receive messages from Telegram users/groups."""
    update = request.json
    chat_id = update["message"]["chat"]["id"]

    chat_ids = load_chat_ids()
    if chat_id not in chat_ids:
        chat_ids.append(chat_id)
        save_chat_ids(chat_ids)

    return "OK", 200

# Set webhook (replace with your server URL)
def set_webhook():
    webhook_url = f"https://YOUR_SERVER_URL/{config.TOKEN}"
    requests.get(f"{URL}/setWebhook?url={webhook_url}")

