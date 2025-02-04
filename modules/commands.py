from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context) -> None:
    await start_command(update, context)

# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello LYKYOU, welcome to the fanbase. Hope you will enjoy my updates with joy. Keep the fam kind and fun.')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'I am LYKYOU, the mascott. You can ask me anything about LYKN.')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'They need to implement it.')