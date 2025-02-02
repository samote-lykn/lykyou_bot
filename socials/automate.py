import feedparser
import time
import schedule
from telegram import Bot

TELEGRAM_BOT_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"

# Define the RSS feeds to track
RSS_FEEDS = {
    "YouTube": "https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID",
    "Twitter": "https://nitter.net/TWITTER_USERNAME/rss",
    "Spotify": "SPOTIFY_PODCAST_RSS_URL"
}

# Function to check RSS feeds for new updates
def check_rss():
    for platform, feed_url in RSS_FEEDS.items():
        feed = feedparser.parse(feed_url)
        latest_entry = feed.entries[0]
        message = f"New {platform} post: {latest_entry.title}\n{latest_entry.link}"
        send_telegram_message(message)

# Function to send Telegram messages
def send_telegram_message(message):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

# Schedule the script to run every 5 minutes
schedule.every(5).minutes.do(check_rss)

while True:
    schedule.run_pending()
    time.sleep(60)
