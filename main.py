from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ApplicationBuilder, CallbackQueryHandler
import config
from modules.logger import handle_error
from modules.responses import handle_message
from modules.commands import start_command, custom_command, help_command
from youtube.polling import save_chat_id_and_keep_updated, check_youtube_updates, fetch_latest_video_and_send
from modules.suggestions import suggestions_members


async def start(update: Update, context) -> None:
    await start_command(update, context)
    await suggestions_members(update, context)



def main():
    print(f'Starting bot... {config.BOT_USERNAME}')

    # ✅ Correct initialization
    app = ApplicationBuilder().token(config.TOKEN).build()

    # ✅ Schedule YouTube updates
    app.job_queue.run_repeating(check_youtube_updates, interval=300, first=5, data={"last_video_id": None})

    # ✅ Commands
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler("youtube", save_chat_id_and_keep_updated))
    app.add_handler(CommandHandler("youtubelatest", fetch_latest_video_and_send))

    print('Commands loaded.')

    # ✅ Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print('Messages handler loaded.')

    # ✅ Errors
    app.add_error_handler(handle_error)
    print('Error handler loaded.')

    print("Polling started...")
    app.run_polling(poll_interval=3)


if __name__ == "__main__":
    main()