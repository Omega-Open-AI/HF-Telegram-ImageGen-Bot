"""
Asynchronous Telegram bot command handlers.
This module uses python-telegram-bot v20+ asynchronous methods.
"""

from telegram import Update
from telegram.ext import ContextTypes
from models import generate_image_flux, generate_image_stable
import asyncio

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Send a welcome message and instructions when the /start command is issued.
    """
    welcome_message = (
        "Welcome to the Async ImageGen Bot!\n\n"
        "Use /flux <prompt> to generate an image using the FLUX model.\n"
        "Use /stable <prompt> to generate an image using the Stable Diffusion model.\n"
        "Use /both <prompt> to generate images concurrently using both models.\n"
    )
    await update.message.reply_text(welcome_message)

async def generate_flux(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle /flux command to generate an image using the FLUX model.
    """
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("Please provide a text prompt after /flux.")
        return

    await update.message.reply_text("Generating image using the FLUX model. Please wait...")
    result = await generate_image_flux(prompt)
    if "error" in result:
        await update.message.reply_text(f"Error: {result['error']}")
    else:
        await update.message.reply_text("Image generated using the FLUX model!")
        await update.message.reply_text(str(result))

async def generate_stable(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle /stable command to generate an image using the Stable Diffusion model.
    """
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("Please provide a text prompt after /stable.")
        return

    await update.message.reply_text("Generating image using the Stable Diffusion model. Please wait...")
    result = await generate_image_stable(prompt)
    if "error" in result:
        await update.message.reply_text(f"Error: {result['error']}")
    else:
        await update.message.reply_text("Image generated using the Stable Diffusion model!")
        await update.message.reply_text(str(result))

async def generate_both(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle /both command to generate images concurrently using both models.
    """
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("Please provide a text prompt after /both.")
        return

    await update.message.reply_text("Generating images using both models concurrently. Please wait...")
    # Run both API calls concurrently
    try:
        flux_future = generate_image_flux(prompt)
        stable_future = generate_image_stable(prompt)
        result_flux, result_stable = await asyncio.gather(flux_future, stable_future)
    except Exception as e:
        await update.message.reply_text("An error occurred while processing your request.")
        return

    message = "Results:\n\nFLUX Model:\n"
    message += f"{result_flux if 'error' not in result_flux else 'Error: ' + result_flux['error']}\n\n"
    message += "Stable Diffusion Model:\n"
    message += f"{result_stable if 'error' not in result_stable else 'Error: ' + result_stable['error']}"
    await update.message.reply_text(message)

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Reply to unknown commands.
    """
    await update.message.reply_text("Sorry, I didn't understand that command.")