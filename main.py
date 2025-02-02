from telegram.ext import CommandHandler, MessageHandler, filters, ApplicationBuilder
import config
from modules.logger import handle_error
from modules.responses import handle_message
from modules.commands import start_command, custom_command, help_command
from youtube.polling import save_chat_id_and_keep_updated, check_youtube_updates

def main():
    print(f'Starting bot... {config.BOT_USERNAME}')

    # ✅ Correct initialization
    app = ApplicationBuilder().token(config.TOKEN).build()

    # ✅ Schedule YouTube updates
    app.job_queue.run_repeating(check_youtube_updates, interval=300, first=5, data={"last_video_id": None})

    # ✅ Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler("followYoutubeUpdates", save_chat_id_and_keep_updated))

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
