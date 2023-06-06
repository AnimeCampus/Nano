import requests
from pyrogram import Client, filters, idle

# Create a Pyrogram Client
app = Client("6206599982:AAEtRoU2jV7heQn8t0Zkwh1L6khiC8EXfcM")

@app.on_message(filters.command("news"))
def news(_, message):
    url = 'https://newsapi.org/v2/top-headlines?country=IN&apiKey=6b32967165ca4a68a88fe7eef9160092'
    response = requests.get(url).json()
    headlines = [article['title'] for article in response['articles']]
    message.reply_text('\n'.join(headlines))

# Start the Pyrogram Client
app.run()
idle()
