from telegram import Update
from telegram.ext import ContextTypes

async def handle_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
