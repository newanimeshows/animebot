from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.ext import CallbackContext
from db import add_reminder, remove_reminder, show_reminders, add_favorite, remove_favorite, get_favorites
from anime_api import get_weekly_top_anime, get_trending_anime, get_top_anime_list, search_anime, fetch_anime_data

async def remind_me(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if len(context.args) < 2:
        await update.message.reply_text("Please provide valid Name and Time. \n\nUsage: /remind <anime_name> <time_in_minutes>")
        return
    
    anime_name = context.args[0]
    try:
        remind_in = int(context.args[1])
    except ValueError:
        await update.message.reply_text("Please provide a valid time in minutes.")
        return
    
    remind_time = (datetime.now() + timedelta(minutes=remind_in)).isoformat()
    add_reminder(user_id, anime_name, remind_time)
    await update.message.reply_text(f"Reminder set for '{anime_name}' in {remind_in} minutes.")

# Add other handler functions (show_reminders_command, remove_reminder_command, etc.) here
