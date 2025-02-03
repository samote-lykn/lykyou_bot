from telegram import ReplyKeyboardMarkup, Update
from const.lykn import Members

async def suggestions_members(update: Update, context):
    # Suggested replies
    keyboard = [[Members.NUT.upper(),
                 Members.TUI.upper(),
                 Members.LEGO.upper(),
                 Members.WILLIAM.upper(),
                 Members.HONG.upper()]]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True,
                                       input_field_placeholder="Type or select a member...")

    await update.message.reply_text("Choose a member:", reply_markup=reply_markup)

    # Remove the keyboard after user selects something
    # update.message.reply_text(f"You said: {user_text}", reply_markup=ReplyKeyboardRemove())
