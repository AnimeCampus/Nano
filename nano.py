import os
import requests
from pyrogram import Client, filters, idle
from telegram import Updater, CommandHandler, MessageHandler, Filters

# Initialize the Telegram bot
bot_token = "6206599982:AAEtRoU2jV7heQn8t0Zkwh1L6khiC8EXfcM"
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

# Initialize the Pyrogram client
api_id = "16743442"
api_hash = "12bbd720f4097ba7713c5e40a11dfd2a"
client = Client("my_bot", api_id, api_hash)


# Handler for the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Send me a keyword to search for a GIF.")


# Handler for text messages
def handle_message(update, context):
    keyword = update.message.text
    gif_url = search_gif(keyword)
    context.bot.send_animation(chat_id=update.effective_chat.id, animation=gif_url)


# Search for a GIF using the Giphy API
def search_gif(keyword):
    giphy_api_key = "WBJ2Bzj0srZLaewLYf5ulkhBTjPJAYYU"
    url = f"https://api.giphy.com/v1/gifs/random?api_key={giphy_api_key}&tag={keyword}"
    response = requests.get(url)
    data = response.json()
    gif_url = data["data"]["image_original_url"]
    return gif_url


# Register the handlers with the Telegram bot
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)


# Start the bot
updater.start_polling()


# Run the Pyrogram client
@client.on_message(filters.private)
def reply_private(client, message):
    keyword = message.text
    gif_url = search_gif(keyword)
    client.send_animation(chat_id=message.chat.id, animation=gif_url)


client.run()


# Stop the bot gracefully
idle() 
