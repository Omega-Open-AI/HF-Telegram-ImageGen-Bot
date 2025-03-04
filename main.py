"""
Main entry point for the asynchronous Telegram bot using python-telegram-bot v20+.
This sets up the application, command handlers, and runs the polling loop.
"""

import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from config import TELEGRAM_TOKEN
from commands import start, generate_flux, generate_stable, generate_both, unknown_command
from monitoring import log_error

async def error_handler(update, context):
    """
    Global error handler logs errors and notifies the user.
    """
    log_error("Update caused error", context.error)
    if update and update.message:
        await update.message.reply_text("An unexpected error occurred. Please try again later.")

async def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("flux", generate_flux))
    application.add_handler(CommandHandler("stable", generate_stable))
    application.add_handler(CommandHandler("both", generate_both))
    application.add_handler(MessageHandler(filters.COMMAND, unknown_command))
    application.add_error_handler(error_handler)

    # Run the bot until manually stopped.
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())