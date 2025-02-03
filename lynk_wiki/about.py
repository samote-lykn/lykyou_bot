from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

from const.emoji import Emoji
from const.lykn import MembersLink, Members

user_selected_members = {}  # Stores user selections (user_id -> member)

# Handle member selection
async def handle_member_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    chosen_member = update.message.text.lower()  # Convert to uppercase to match Members class

    print(f"{Emoji.RIGHT_ARROW} Chosen member: {chosen_member}")
    if chosen_member not in [Members.WILLIAM, Members.NUT, Members.TUI, Members.HONG, Members.LEGO]:
        await update.message.reply_text(f"{Emoji.CROSS_MARK} Invalid choice. Please select a valid member.")
        return

    # Save user selection
    user_selected_members[user_id] = chosen_member

    # Ask for social platform selection
    await button_socials(update, context, chosen_member)


# Send social media buttons
async def button_socials(update: Update, context, chosen_member):
    keyboard = [
        [InlineKeyboardButton("Instagram", callback_data='INSTAGRAM')],
        [InlineKeyboardButton("Twitter", callback_data='TWITTER')],
        [InlineKeyboardButton("TikTok", callback_data='TIKTOK')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"{Emoji.RIGHT_ARROW} You selected {chosen_member}. Now choose a social:", reply_markup=reply_markup)


# Handle button clicks
async def button_social_response(update: Update, context) -> None:
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id  # FIXED: Use `query.from_user.id`
    chosen_social = query.data  # FIXED: No need for `.lower()` (already uppercase)

    if user_id not in user_selected_members:
        await query.message.reply_text(f"{Emoji.WARNING} Please select a member first.")
        return

    selected_member = user_selected_members[user_id]

    # Get the correct social media link
    social_links = {
        "INSTAGRAM": MembersLink.INSTAGRAM_LINKS,
        "TWITTER": MembersLink.TWITTER_LINKS,
        "TIKTOK": MembersLink.TIKTOK_LINKS,
    }

    print(f"{Emoji.RIGHT_ARROW} Chosen social: {chosen_social}")

    if chosen_social in social_links:
        link = social_links[chosen_social].get(selected_member, "No link available.")
        if link == "No link available.":
            await query.message.reply_text(f"{Emoji.POLICE_ALARM} {link}")
        else:
            await query.message.reply_text(f"{Emoji.PROGRESS} Follow {selected_member.upper()} on {chosen_social}: {link}")
    else:
        await query.message.reply_text(f"{Emoji.CROSS_MARK} Invalid social media choice. Please try again.")
