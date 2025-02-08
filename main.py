from telegram.ext import ApplicationBuilder
import config
from modules.handlers import (
    START_HANDLER, HELP_HANDLER, ABOUT_HANDLER, MEMBER_CHOICE_HANDLER,
    ASK_SOCIALS_HANDLER, BUTTON_RESPONSE_HANDLER, toggle_handler
)
from modules.logger import handle_error


def main():
    print(f'Starting bot... {config.BOT_USERNAME}')

    app = ApplicationBuilder().token(config.TOKEN).build()

    # Use handler constants from `modules.handlers`
    toggle_handler(app, START_HANDLER, True)
    toggle_handler(app, HELP_HANDLER, True)
    toggle_handler(app, ABOUT_HANDLER, True)
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
