from telegram.ext import ApplicationBuilder
import config
from modules.handlers import (
    START_HANDLER, HELP_HANDLER, ABOUT_HANDLER, CUSTOM_HANDLER,
    YOUTUBE_HANDLER, YOUTUBE_LATEST_HANDLER, MEMBER_CHOICE_HANDLER,
    ASK_SOCIALS_HANDLER, BUTTON_RESPONSE_HANDLER, toggle_handler
)
from modules.logger import handle_error
from youtube.polling import check_youtube_updates


def main():
    print(f'Starting bot... {config.BOT_USERNAME}')

    app = ApplicationBuilder().token(config.TOKEN).build()

    app.job_queue.run_repeating(check_youtube_updates, interval=300, first=5, data={"last_video_id": None})

    # Use handler constants from `modules.handlers`
    toggle_handler(app, START_HANDLER, True)
    toggle_handler(app, HELP_HANDLER, True)
    toggle_handler(app, ABOUT_HANDLER, True)
    toggle_handler(app, CUSTOM_HANDLER, True)
    toggle_handler(app, YOUTUBE_HANDLER, True)
    toggle_handler(app, YOUTUBE_LATEST_HANDLER, True)
    toggle_handler(app, MEMBER_CHOICE_HANDLER, False)
    toggle_handler(app, ASK_SOCIALS_HANDLER, False)
    toggle_handler(app, BUTTON_RESPONSE_HANDLER, True)

    print("Handlers loaded.")

    app.add_error_handler(handle_error)
    print('Error handler loaded.')

    print("Polling started...")
    app.run_polling(poll_interval=3)

if __name__ == "__main__":
    main()
