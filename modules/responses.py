from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from const import FanBase, Members, BotChatType
import config

# responses

def handle_response(text:str) -> str:
    processed: str = text.lower()
    print(processed)
    if FanBase.LYKN in processed:
        return 'Hi LYKYOU!'
    if Members.TUI in processed:
        return 'Hi Tui!'
    if Members.NUT in processed:
        return 'Hi Nut!'
    if Members.LEGO in processed:
        return 'Hi Lego!'
    if Members.WILLIAM in processed:
        return 'Hi William!'
    if Members.HONG in processed:
        return 'Hi Hong!'
    return 'Hi LYKYOU!'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str =update.message.chat.type #from group or solo
    text: str = update.message.text #incoming message

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == BotChatType.GROUP:
        print('Group')
        if config.BOT_USERNAME not in text:  # bot not mentioned in group
            return
        new_text: str = text.replace(config.BOT_USERNAME, '').strip() #remove bot name from message
        response: str = handle_response(new_text)
    else:
        print('Private')
        response: str = handle_response(text)
    print('Bot', response)
    await update.message.reply_text(response)
