import feedparser
import asyncio
from aiogram import Bot, Dispatcher, types
from config import TOKEN

CHAT_ID = "YOUR_CHAT_ID"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
last_video_url = None  # Store last checked video URL

async def check_rss(rss_feed):
    global last_video_url
    while True:
        feed = feedparser.parse(rss_feed)
        if len(feed.entries) > 0:
            latest_video = feed.entries[0]  # Get newest entry
            if latest_video.link != last_video_url:  # Check if it's new
                last_video_url = latest_video.link
                message = f"🚨 New TikTok Video!\n\n{latest_video.title}\n{latest_video.link}"
                await bot.send_message(CHAT_ID, message)
        await asyncio.sleep(60)  # Check every 60 seconds

# if __name__ == "__main__":
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(check_rss())
