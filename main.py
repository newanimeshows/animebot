import os
import logging
from telegram.ext import Application
from config import TOKEN
from handlers import (
    start, help_command, owner_command, weekly, trending, top, search,
    show_favorites, remove_favanime, remind_me, show_reminders_command,
    remove_reminder_command, add_favorite_handler, remove_favorite_handler,
    button
)
from scheduler import setup_scheduler

def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    application = Application.builder().token(TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('owner', owner_command))
    application.add_handler(CommandHandler('weekly', weekly))
    application.add_handler(CommandHandler('trending', trending))
    application.add_handler(CommandHandler('top', top))
    application.add_handler(CommandHandler('search', search))
    application.add_handler(CommandHandler('showfav', show_favorites))
    application.add_handler(CommandHandler('removefavanime', remove_favanime))
    application.add_handler(CommandHandler('remind', remind_me))
    application.add_handler(CommandHandler('showreminders', show_reminders_command))
    application.add_handler(CommandHandler('removereminder', remove_reminder_command))

    # Callback query handlers
    application.add_handler(CallbackQueryHandler(button))

    # Set up scheduler
    setup_scheduler(application)

    application.run_polling()

if __name__ == '__main__':
    main()
