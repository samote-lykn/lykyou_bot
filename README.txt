Yes, but you need to make a few adjustments to ensure smooth deployment on **Heroku**.

---

## 🔹 **Steps to Deploy on Heroku**
Heroku does **not** keep your bot running by default (it **sleeps** after inactivity). To keep it active, you must use **webhooks** instead of polling.

### **1️⃣ Install Heroku CLI & Set Up a Heroku Project**
1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
2. Log in using:
   ```sh
   heroku login
   ```
3. Navigate to your project folder and create a new Heroku app:
   ```sh
   heroku create YOUR_APP_NAME
   ```
4. Add a **Procfile** to your project:
   ```sh
   echo "worker: python main.py" > Procfile
   ```

---

### **2️⃣ Modify Your Code to Use Webhooks**
Heroku doesn’t allow long-running **polling**, so replace:
```python
app.run_polling(poll_interval=3)
```
**with this webhook-based setup**:

```python
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os
import config
from modules.logger import handle_error
from modules.responses import handle_message
from modules.commands import start_command, custom_command, help_command
from youtube.polling import save_chat_id_and_keep_updated, check_youtube_updates

# Flask app for webhooks
app = Flask(__name__)

# Telegram Bot Setup
bot_app = ApplicationBuilder().token(config.TOKEN).build()

# ✅ Set up webhook route
@app.route(f"/{config.TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(), bot_app.bot)
    bot_app.update_queue.put(update)
    return "OK", 200

# ✅ Setup job queue for YouTube updates
async def start_youtube_job(application):
    job_name = "youtube_updates"
    if not application.job_queue.get_jobs_by_name(job_name):
        application.job_queue.run_repeating(check_youtube_updates, interval=300, first=5, name=job_name, data={"last_video_id": None})
        print("✅ YouTube update job started!")

async def start_bot():
    print(f'Starting bot... {config.BOT_USERNAME}')
    bot_app.add_handler(CommandHandler('start', start_command))
    bot_app.add_handler(CommandHandler('help', help_command))
    bot_app.add_handler(CommandHandler('custom', custom_command))
    bot_app.add_handler(CommandHandler("followYoutubeUpdates", save_chat_id_and_keep_updated))
    bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    bot_app.add_error_handler(handle_error)

    await start_youtube_job(bot_app)
    await bot_app.bot.set_webhook(f"{config.WEBHOOK_URL}/{config.TOKEN}")

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
```

---

### **3️⃣ Set Up Webhook & Deploy**
1. **Set Environment Variables** in Heroku:
   ```sh
   heroku config:set TOKEN=your-bot-token
   heroku config:set WEBHOOK_URL=https://your-app-name.herokuapp.com
   ```
2. **Push Code to Heroku:**
   ```sh
   git add .
   git commit -m "Deploy bot to Heroku"
   git push heroku main
   ```
3. **Scale the bot to run continuously:**
   ```sh
   heroku ps:scale worker=1
   ```

---

## ✅ **Now Your Bot Will Work on Heroku**
✔ Uses **webhooks** instead of polling (keeps Heroku happy)
✔ Sends **YouTube updates every 5 minutes**
✔ Sends the **latest video immediately** when subscribing

Let me know if you need help! 🚀