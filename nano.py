import os

import requests

from pyrogram import Client, filters, idle

# Initialize the Pyrogram client

api_id = "16743442"

api_hash = "12bbd720f4097ba7713c5e40a11dfd2a"

bot_token = "6206599982:AAEtRoU2jV7heQn8t0Zkwh1L6khiC8EXfcM"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Handler for the /start command

@app.on_message(filters.command("start"))

def start(client, message):

    client.send_message(chat_id=message.chat.id, text="Hello! Send me a keyword to search for a GIF.")

# Handler for text messages

@app.on_message(filters.private & filters.text)

def handle_message(client, message):

    keyword = message.text

    gif_url = search_gif(keyword)

    client.send_animation(chat_id=message.chat.id, animation=gif_url)

# Search for a GIF using the Giphy API

def search_gif(keyword):

    giphy_api_key = "WBJ2Bzj0srZLaewLYf5ulkhBTjPJAYYU"

    url = f"https://api.giphy.com/v1/gifs/random?api_key={giphy_api_key}&tag={keyword}"

    response = requests.get(url)

    data = response.json()

    gif_url = data["data"].get("image_original_url", "Default URL")

    return gif_url

# Start the bot

app.run()
idle()
