import threading
import requests
import json
import time
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler
from youtube.utils import CHAT_ID_FILE, create_rss_youtube_url
import config

YOUTUBE_RSS_URL = create_rss_youtube_url(config.YOUTUBE_CHANNEL_ID)


# Load chat IDs
def load_chat_ids():
    try:
        with open(CHAT_ID_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Save chat IDs
def save_chat_ids(chat_ids):
    with open(CHAT_ID_FILE, "w") as f:
        json.dump(chat_ids, f)


# Start command
def save_chat_id_and_keep_updated(update: Update, context):
    chat_id = update.message.chat_id
    chat_ids = load_chat_ids()

    if chat_id not in chat_ids:
        chat_ids.append(chat_id)
        save_chat_ids(chat_ids)

    context.bot.send_message(chat_id=chat_id, text="✅ You will now receive YouTube updates!")  # ✅ FIXED


# YouTube Update Checker (Runs in a Separate Thread)
def check_youtube_updates(application: Application):
    last_video_id = None  # Store last video ID
    bot = application.bot  # ✅ Get the bot instance

    while True:
        try:
            response = requests.get(YOUTUBE_RSS_URL)
            if response.status_code == 200:
                data = response.text

                # Extract latest video ID
                video_id = data.split("<yt:videoId>")[1].split("</yt:videoId>")[0]

                if video_id != last_video_id:
                    last_video_id = video_id
                    video_url = f"https://www.youtube.com/watch?v={video_id}"

                    # Send update to all chat IDs
                    chat_ids = load_chat_ids()
                    for chat_id in chat_ids:
                        application.create_task(bot.send_message(chat_id, f"📢 New Video: {video_url}"))  # ✅ ASYNC SAFE

        except Exception as e:
            print(f"Error checking YouTube RSS: {e}")

        time.sleep(300)  # Check every 5 minutes