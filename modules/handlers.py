
# handlers_registry.py
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, filters
from modules.commands import start, help_command, custom_command
from youtube.polling import save_chat_id_and_keep_updated, fetch_latest_video_and_send
from lynk_wiki.about import handle_member_choice, handle_ask_for_socials, button_social_response, about_command

# ✅ COMMAND HANDLERS
START_HANDLER = CommandHandler("start", start)
HELP_HANDLER = CommandHandler("help", help_command)
ABOUT_HANDLER = CommandHandler("about", about_command)
CUSTOM_HANDLER = CommandHandler("custom", custom_command)
YOUTUBE_HANDLER = CommandHandler("youtube", save_chat_id_and_keep_updated)
YOUTUBE_LATEST_HANDLER = CommandHandler("youtubelatest", fetch_latest_video_and_send)

# ✅ MESSAGE HANDLERS
MEMBER_CHOICE_HANDLER = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_member_choice)
ASK_SOCIALS_HANDLER = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_ask_for_socials)

# ✅ CALLBACK QUERY HANDLER
BUTTON_RESPONSE_HANDLER = CallbackQueryHandler(button_social_response)

def toggle_handler(app, handler, enable=True):
    """Enable or disable a specific handler dynamically."""
    if enable:
        app.add_handler(handler)
        print(f"✅ Handler {handler} ENABLED")
    else:
        app.remove_handler(handler)
        print(f"❌ Handler {handler} DISABLED")
