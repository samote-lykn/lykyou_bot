from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from const.emoji import Emoji
from const.lykn import MembersLink, Members
from mongoDB.about_member_selection import update_selected_member, get_user_selection, delete_user_selection
from mongoDB.classes import User

class aboutHandles:
    SOCIAL= 'social'
    MEMBERS = 'members'

#toggle handler
def disable_all_about_handlers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from modules.handlers import toggle_handler
    from modules.handlers import (
        MEMBER_CHOICE_HANDLER,
        ASK_SOCIALS_HANDLER
    )
    app = context.application  # Get the Application instance
    toggle_handler(app, MEMBER_CHOICE_HANDLER, False)
    toggle_handler(app, ASK_SOCIALS_HANDLER, False)

def enable_one_about_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, handlerKey: str):
    from modules.handlers import toggle_handler
    from modules.handlers import (
        MEMBER_CHOICE_HANDLER,
        ASK_SOCIALS_HANDLER
    )
    app = context.application  # Get the Application instance
    toggle_handler(app, ASK_SOCIALS_HANDLER, handlerKey == aboutHandles.SOCIAL)
    toggle_handler(app, MEMBER_CHOICE_HANDLER,  handlerKey == aboutHandles.MEMBERS)



# Command
async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{Emoji.PARTY} Do you wanna know more about LYKN?")
    await suggestions_members(update, context)

# Suggestion

async def suggestions_members(update: Update, context):
    enable_one_about_handler(update, context, aboutHandles.MEMBERS)

    # Suggested replies
    keyboard = [[Members.NUT.upper(),
                 Members.TUI.upper(),
                 Members.LEGO.upper(),
                 Members.WILLIAM.upper(),
                 Members.HONG.upper()]]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True,
                                       input_field_placeholder="Type or select a member...")

    if update.message:
        # Regular message
        await update.message.reply_text(f"{Emoji.RIGHT_ARROW} Choose a member:", reply_markup=reply_markup)
    elif update.callback_query:
        # Inline button callback
        await update.callback_query.message.reply_text(f"{Emoji.RIGHT_ARROW} Choose a member:",
                                                       reply_markup=reply_markup)

    # Remove the keyboard after user selects something
    # update.message.reply_text(f"You said: {user_text}", reply_markup=ReplyKeyboardRemove())

async def ask_for_socials(update: Update, context):
    enable_one_about_handler(update, context, aboutHandles.SOCIAL)

    # Suggested replies
    keyboard = [['YES',
                 'NO']]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True,
                                       input_field_placeholder="Type or select a answear...")

    if update.message:
        # Regular message
        await update.message.reply_text(f"{Emoji.RIGHT_ARROW} Do you wanna follow him on socials?", reply_markup=reply_markup)
    elif update.callback_query:
        # Inline button callback
        await update.callback_query.message.reply_text(f"{Emoji.RIGHT_ARROW} Do you wanna follow him on socials?",
                                                       reply_markup=reply_markup)


# Handle member selection
async def handle_member_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    chosen_member = update.message.text.lower()  # Convert to uppercase to match Members class

    print(f"{Emoji.RIGHT_ARROW} Chosen member: {chosen_member}")
    if chosen_member not in [Members.WILLIAM, Members.NUT, Members.TUI, Members.HONG, Members.LEGO]:
        await update.message.reply_text(f"{Emoji.CROSS_MARK} Invalid choice. Please select a valid member.")
        return

    # Save user selection
    await update_selected_member(user_id, chosen_member)

    await update.message.reply_text(f"{Emoji.PARTY} You selected '{chosen_member.upper()}'",
                                    reply_markup=ReplyKeyboardRemove())  # Removes reply keyboard

    wiki =  MembersLink.WIKI_LINKS.get(chosen_member, "No link available.")
    if wiki == "No link available.":
        await update.message.reply_text(f"{Emoji.POLICE_ALARM} {wiki}")
    else:
        await update.message.reply_text(
            f"{Emoji.PROGRESS} Learn more about '{chosen_member.upper()}': {wiki}")
        # Ask for social platform selection
        await ask_for_socials(update, context)


async def handle_ask_for_socials(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'YES' in update.message.text.upper():
        await update.message.reply_text(f"{Emoji.PARTY} Let me load his socials...'",
                                        reply_markup=ReplyKeyboardRemove())  # Removes reply keyboard
        # Ask for social platform selection
        await button_socials(update, context)
    else:
        await update.message.reply_text(f"{Emoji.CROSS_MARK} Nevermind...'",
                                        reply_markup=ReplyKeyboardRemove())  # Removes reply keyboard
        app = context.application  # Get the Application instance
        disable_all_about_handlers(update, context)

# Send social media buttons
async def button_socials(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Instagram", callback_data='INSTAGRAM')],
        [InlineKeyboardButton("Twitter", callback_data='TWITTER')],
        [InlineKeyboardButton("TikTok", callback_data='TIKTOK')],
        [InlineKeyboardButton("Select another member", callback_data='suggestions_members')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(  # Now send inline buttons
        f"{Emoji.RIGHT_ARROW} Now choose a social:",
        reply_markup=reply_markup
    )
# Handle button clicks
async def button_social_response(update: Update, context) -> None:
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id  # FIXED: Use `query.from_user.id`
    chosen_social = query.data  # FIXED: No need for `.lower()` (already uppercase)

    # Get the user's selection
    user_selection: User = await get_user_selection(user_id)

    # Check if user selection is None or doesn't have a valid 'selected_member'
    if not user_selection or not user_selection.selected_member:
        # Send a warning message if no selection is made
        await update.message.reply_text(f"{Emoji.WARNING} Please select a member first.")

        # Call the function to show suggestions or prompt the user to select a member
        await suggestions_members(update, context)
        return

    selected_member = user_selection.selected_member

    # Get the correct social media link
    social_links = {
        "INSTAGRAM": MembersLink.INSTAGRAM_LINKS,
        "TWITTER": MembersLink.TWITTER_LINKS,
        "TIKTOK": MembersLink.TIKTOK_LINKS,
    }

    print(f"{Emoji.RIGHT_ARROW} Chosen social: {chosen_social}")

    if chosen_social == 'suggestions_members':
        print(f"{Emoji.EXCLAMATION_MARK} Deleting chosen member")
        await delete_user_selection(user_id)
        await suggestions_members(update, context)
        print(f"{Emoji.WARNING} Suggestions reloaded")
        return

    if chosen_social in social_links:
        link = social_links[chosen_social].get(selected_member, "No link available.")
        if link == "No link available.":
            await query.message.reply_text(f"{Emoji.POLICE_ALARM} {link}")
        else:
            await query.message.reply_text(f"{Emoji.PROGRESS} Follow {selected_member.upper()} on {chosen_social}: {link}")
    else:
        await query.message.reply_text(f"{Emoji.CROSS_MARK} Invalid social media choice. Please try again.")
