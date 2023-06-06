import requests
from pyrogram import Client, filters, idle

# Pyrogram Configuration
api_id = 16743442
api_hash = '12bbd720f4097ba7713c5e40a11dfd2a'
bot_token = '6206599982:AAEtRoU2jV7heQn8t0Zkwh1L6khiC8EXfcM'

# Create a Pyrogram Client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("news"))
def news(_, message):
    url = 'https://newsapi.org/v2/top-headlines?country=IN&apiKey=6b32967165ca4a68a88fe7eef9160092'
    response = requests.get(url).json()
    headlines = [article['title'] for article in response['articles']]
    message.reply_text('\n'.join(headlines))

# Start the Pyrogram Client
app.start()
idle()

