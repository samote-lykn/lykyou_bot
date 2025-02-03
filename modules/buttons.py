from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from const.lykn import Members


async def example_button_generation(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Last Youtube video", callback_data='lastvideo')],
        [InlineKeyboardButton('Tui', callback_data=Members.TUI)],
        [InlineKeyboardButton('Nut', callback_data=Members.NUT)],
        [InlineKeyboardButton('Lego', callback_data=Members.LEGO)],
        [InlineKeyboardButton('Hong', callback_data=Members.HONG)],
        [InlineKeyboardButton('William', callback_data=Members.WILLIAM)],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Select a command:", reply_markup=reply_markup)


async def button(update: Update, context) -> None:
    #load buttons like this in main -> app.add_handler(CallbackQueryHandler(button))
    query = update.callback_query
    await query.answer()

    match query.data:
        case "lastvideo": # do something
            await query.edit_message_text(text="something")
        case Members.TUI | Members.LEGO | Members.NUT | Members.HONG | Members.WILLIAM:
            await context.bot.send_message(chat_id=query.message.chat.id, text=query.data)
        case _:
            await query.edit_message_text(text="Command not recognized.")
