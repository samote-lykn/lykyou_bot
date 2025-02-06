import feedparser
from telegram.ext import CallbackContext
import json
from tiktok.config import CHAT_ID_TIKTOK_FILE

# ✅ Load chat IDs
def load_chat_ids():
    try:
        with open(CHAT_ID_TIKTOK_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# ✅ Save chat IDs
def save_chat_ids(chat_ids):
    with open(CHAT_ID_TIKTOK_FILE, "w") as f:
        json.dump(chat_ids, f)

async def check_rss(context: CallbackContext, rss_feed_url):
    """Check the RSS feed for new videos."""
    feed = feedparser.parse(rss_feed_url)
    last_video_url = context.job.data.get("last_video_url", None)
    bot = context.bot

    if len(feed.entries) > 0:
        latest_video = feed.entries[0]  # Get the newest entry
        if latest_video.link != last_video_url:  # Check if it's new
            last_video_url = latest_video.link
            message = f"🚀 New TikTok Video!\n\n🎥 {latest_video.title}\n🔗 {latest_video.link}"
            chat_ids = load_chat_ids()
            for chat_id in chat_ids:
                await bot.send_message(chat_id, message)

            context.job.data["last_video_url"] = last_video_url
            return  # Stop after finding the most recent matching video