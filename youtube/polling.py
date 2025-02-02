from telegram import Update
from telegram.ext import CallbackContext
import json
import requests
from youtube.utils import CHAT_ID_FILE, create_rss_youtube_url
import config

YOUTUBE_RSS_URL = create_rss_youtube_url(config.YOUTUBE_CHANNEL_ID)

# ✅ Load chat IDs
def load_chat_ids():
    try:
        with open(CHAT_ID_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# ✅ Save chat IDs
def save_chat_ids(chat_ids):
    with open(CHAT_ID_FILE, "w") as f:
        json.dump(chat_ids, f)

# ✅ Fetch latest video from YouTube RSS feed
def get_latest_video():
    try:
        response = requests.get(YOUTUBE_RSS_URL)
        if response.status_code == 200:
            data = response.text
            video_id = data.split("<yt:videoId>")[1].split("</yt:videoId>")[0]
            return f"https://www.youtube.com/watch?v={video_id}"
    except Exception as e:
        print(f"Error fetching latest video: {e}")
    return None

# ✅ Function to check YouTube updates periodically
async def check_youtube_updates(context: CallbackContext):
    last_video_id = context.job.data.get("last_video_id", None)
    bot = context.bot

    try:
        response = requests.get(YOUTUBE_RSS_URL)
        if response.status_code == 200:
            data = response.text
            video_id = data.split("<yt:videoId>")[1].split("</yt:videoId>")[0]

            if video_id != last_video_id:
                last_video_id = video_id
                video_url = f"https://www.youtube.com/watch?v={video_id}"

                chat_ids = load_chat_ids()
                for chat_id in chat_ids:
                    await bot.send_message(chat_id, f"📢 New Video: {video_url}")

                context.job.data["last_video_id"] = last_video_id

    except Exception as e:
        print(f"Error checking YouTube RSS: {e}")

# ✅ Subscribe user, send first video, and start job
async def save_chat_id_and_keep_updated(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    chat_ids = load_chat_ids()

    if chat_id not in chat_ids:
        chat_ids.append(chat_id)
        save_chat_ids(chat_ids)

    await update.message.reply_text("✅ You are now subscribed to YouTube updates!")

    # ✅ Fetch the latest video and send it immediately
    latest_video = get_latest_video()
    if latest_video:
        await update.message.reply_text(f"🎬 Latest Video: {latest_video}")

    # ✅ Start job if not already running
    job_name = "youtube_updates"
    current_jobs = context.job_queue.get_jobs_by_name(job_name)

    if not current_jobs:
        context.job_queue.run_repeating(
            check_youtube_updates,
            interval=300,
            first=300,  # ✅ Start checking after 5 minutes (to avoid immediate duplicate)
            name=job_name,
            data={"last_video_id": None},
        )
        print("✅ YouTube update job started!")
