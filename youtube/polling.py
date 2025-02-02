from telegram import Update
from telegram.ext import CallbackContext
import json
import requests
from youtube.utils import CHAT_ID_FILE, create_rss_youtube_url
import config
import xml.etree.ElementTree as ET

YOUTUBE_RSS_URL = create_rss_youtube_url(config.YOUTUBE_CHANNEL_ID)
REQUIRED_KEYWORD = config.REQUIRED_KEYWORD.lower()  # Convert to lowercase  # Replace with your specific hashtag

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
            root = ET.fromstring(response.text)
            entries = root.findall("{http://www.w3.org/2005/Atom}entry")
            print(entries)
            for entry in entries:  # Iterate through all videos in the feed
                video_id = entry.find("{http://www.youtube.com/xml/schemas/2015}videoId").text
                title = entry.find("{http://www.w3.org/2005/Atom}title").text.lower()  # Convert to lowercase

                # Check if the title contains the required hashtag
                if REQUIRED_KEYWORD in title:
                    return f"https://www.youtube.com/watch?v={video_id}"  # Return the first matching video

    except Exception as e:
        print(f"Error fetching latest video: {e}")

    return None  # No video found with the required hashtag

# ✅ Function to check YouTube updates periodically
async def check_youtube_updates(context: CallbackContext):
    last_video_id = context.job.data.get("last_video_id", None)
    bot = context.bot

    try:
        response = requests.get(YOUTUBE_RSS_URL)
        if response.status_code == 200:
            root = ET.fromstring(response.text)
            entries = root.findall("{http://www.w3.org/2005/Atom}entry")

            for entry in entries:  # Iterate through all recent videos
                video_id = entry.find("{http://www.youtube.com/xml/schemas/2015}videoId").text
                title = entry.find("{http://www.w3.org/2005/Atom}title").text.lower()  # Convert to lowercase
                print(title)
                if REQUIRED_KEYWORD in title:
                    if video_id != last_video_id:  # Ensure it's a new video
                        last_video_id = video_id
                        video_url = f"https://www.youtube.com/watch?v={video_id}"

                        chat_ids = load_chat_ids()
                        for chat_id in chat_ids:
                            await bot.send_message(chat_id, f"📢 New Video: {video_url}")

                        context.job.data["last_video_id"] = last_video_id
                        return  # Stop after finding the most recent matching video

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
