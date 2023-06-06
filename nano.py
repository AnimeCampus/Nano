import requests
from pyrogram import Client, filters, idle

# Pyrogram Configuration
api_id = 16743442
api_hash = '12bbd720f4097ba7713c5e40a11dfd2a'
bot_token = '6206599982:AAEtRoU2jV7heQn8t0Zkwh1L6khiC8EXfcM'

# Create a Pyrogram Client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Fetch headlines from the News API
def fetch_headlines():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'IN',
        'apiKey': '6b32967165ca4a68a88fe7eef9160092'  # Replace with your News API key
    }
    response = requests.get(url, params=params).json()
    articles = response.get('articles', [])
    headlines = [article['title'] for article in articles]
    return headlines

# Send headlines one by one
def send_headlines(chat_id, headlines):
    for headline in headlines:
        message = f"📰 {headline}"
        app.send_message(chat_id, message)

# Command handler for /news
@app.on_message(filters.command("news"))
def handle_news_command(_, message):
    chat_id = message.chat.id
    headlines = fetch_headlines()
    send_headlines(chat_id, headlines)

# Start the Pyrogram Client
app.start()
idle()

import requests
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Pyrogram Configuration
api_id = 16743442
api_hash = '12bbd720f4097ba7713c5e40a11dfd2a'
bot_token = '6206599982:AAEtRoU2jV7heQn8t0Zkwh1L6khiC8EXfcM'

# Create a Pyrogram Client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Fetch headlines from the News API
def fetch_headlines():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'IN',
        'apiKey': '6b32967165ca4a68a88fe7eef9160092'  # Replace with your News API key
    }
    response = requests.get(url, params=params).json()
    articles = response.get('articles', [])
    headlines = [article['title'] for article in articles]
    return headlines

# Send headlines with a button for changing the news
def send_headlines(chat_id, headlines):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Change News", callback_data="change_news")]
        ]
    )
    for headline in headlines:
        message = f"📰 {headline}"
        app.send_message(chat_id, message, reply_markup=keyboard)

# Command handler for /news
@app.on_message(filters.command("news"))
def handle_news_command(_, message):
    chat_id = message.chat.id
    headlines = fetch_headlines()
    send_headlines(chat_id, headlines)

# Callback handler for the "Change News" button
@app.on_callback_query(filters.regex("change_news"))
def handle_change_news(_, callback_query):
    chat_id = callback_query.message.chat.id
    headlines = fetch_headlines()
    send_headlines(chat_id, headlines)

# Start the Pyrogram Client
app.start()
idle()
