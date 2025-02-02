import requests
import json
from youtube.utils import CHAT_ID_FILE, create_rss_youtube_url
from telegram import Update
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


async def save_chat_id_and_keep_updated(update: Update, context):
    chat_id = update.message.chat_id
    chat_ids = load_chat_ids()

    if chat_id not in chat_ids:
        chat_ids.append(chat_id)
        save_chat_ids(chat_ids)

    await context.bot.send_message(chat_id=chat_id, text="✅ You will now receive YouTube updates!")  # ✅ FIXED!

# YouTube Update Checker (Runs Periodically)
async def check_youtube_updates(context):
    """Fetches YouTube RSS Feed and sends updates to Telegram users."""
    last_video_id = context.job.data.get("last_video_id", None)  # Keep track of last video ID
    bot = context.bot

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
                    await bot.send_message(chat_id, f"📢 New Video: {video_url}")

                # Save latest video ID to prevent duplicate messages
                context.job.data["last_video_id"] = last_video_id

    except Exception as e:
        print(f"Error checking YouTube RSS: {e}")

