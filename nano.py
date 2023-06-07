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
def fetch_headlines(country='IN', category=None, source=None):
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': country,
        'apiKey': '6b32967165ca4a68a88fe7eef9160092'  # Replace with your News API key
    }
    if category:
        params['category'] = category
    if source:
        params['sources'] = source
    response = requests.get(url, params=params).json()
    articles = response.get('articles', [])
    headlines = [article['title'] for article in articles]
    return headlines

# Send a single headline with the "Change News" button
def send_headline(chat_id, headline):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Change News", callback_data="change_news")],
            [InlineKeyboardButton("Help", callback_data="help")]
        ]
    )
    message = f"📰 {headline}"
    app.send_message(chat_id, message, reply_markup=keyboard)

# Command handler for /start and /help
@app.on_message(filters.command(["start", "help"]))
def handle_help_command(_, message):
    chat_id = message.chat.id
    help_text = """
    Welcome to the News Bot! Here are the available commands:
    
    /news - Get the latest news headline
    /category - Select a news category
    /source - Select a news source
    /help - Show this help menu
    """
    app.send_message(chat_id, help_text)

# Command handler for /news
@app.on_message(filters.command("news"))
def handle_news_command(_, message):
    chat_id = message.chat.id
    headlines = fetch_headlines()
    if headlines:
        send_headline(chat_id, headlines[0])

# Command handler for /category
@app.on_message(filters.command("category"))
def handle_category_command(_, message):
    chat_id = message.chat.id
    categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(category.capitalize(), callback_data=f"category_{category}")
            ]
            for category in categories
        ]
    )
    message = "Select a category:"
    app.send_message(chat_id, message, reply_markup=keyboard)

# Callback handler for category buttons
@app.on_callback_query(filters.regex(r"category_(\w+)"))
def handle_category_callback(_, callback_query):
    chat_id = callback_query.message.chat.id
    category = callback_query.matches[0].group(1)
    headlines = fetch_headlines(category=category)
    if headlines:
        send_headline(chat_id, headlines[0])

# Command handler for /source
@app.on_message(filters.command("source"))
def handle_source_command(_, message):
    chat_id = message.chat.id
    sources = ['cnn', 'bbc-news', 'the-new-york-times', 'google-news', 'reuters']
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(source.capitalize(), callback_data=f"source_{source}")
            ]
            for source in sources
        ]
    )
    message = "Select a news source:"
    app.send_message(chat_id, message, reply_markup=keyboard)

# Callback handler for source buttons
@app.on_callback_query(filters.regex(r"source_(\w+)"))
def handle_source_callback(_, callback_query):
    chat_id = callback_query.message.chat.id
    source = callback_query.matches[0].group(1)
    headlines = fetch_headlines(source=source)
    if headlines:
        send_headline(chat_id, headlines[0])

# Callback handler for the "Change News" button
@app.on_callback_query(filters.regex("change_news"))
def handle_change_news(_, callback_query):
    chat_id = callback_query.message.chat.id
    headlines = fetch_headlines()
    if headlines:
        send_headline(chat_id, headlines[0])

# Callback handler for the "Help" button
@app.on_callback_query(filters.regex("help"))
def handle_help_callback(_, callback_query):
    chat_id = callback_query.message.chat.id
    help_text = """
    Welcome to the News Bot! Here are the available commands:
    
    /news - Get the latest news headline
    /category - Select a news category
    /source - Select a news source
    /help - Show this help menu
    """
    app.send_message(chat_id, help_text)

# Start the Pyrogram Client
app.start()
idle()
