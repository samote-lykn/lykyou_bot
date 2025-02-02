import feedparser
import requests
import time
import config
from utils import create_rss_youtube_url
import json
from utils import CHAT_ID_FILE

# Store the last video ID to avoid duplicates
last_video_id = None

def load_chat_ids():
    """Load all stored chat IDs."""
    try:
        with open(CHAT_ID_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def get_latest_video(channel_id):
    """Fetch the latest video from the RSS feed."""
    global last_video_id
    feed = feedparser.parse(create_rss_youtube_url(channel_id))

    if feed.entries:
        latest_entry = feed.entries[0]
        video_id = latest_entry.yt_videoid
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        if video_id != last_video_id:
            last_video_id = video_id
            return video_url
    return

def check_video_availability_and_send_message():
    new_video_url = get_latest_video(config.YOUTUBE_CHANNEL_ID)
    if new_video_url:
        send_telegram_message(new_video_url)


def send_telegram_message(message):
    """Send a message to all stored users and groups."""
    chat_ids = load_chat_ids()
    for chat_id in chat_ids:
        url = f"https://api.telegram.org/bot{config.TOKEN}/sendMessage"
        payload = {"chat_id": chat_id, "text": message}
        requests.post(url, data=payload)

# Run the script continuously (check every 5 minutes)
while True:
    get_latest_video()
    time.sleep(300)  # 300 seconds = 5 minutes
