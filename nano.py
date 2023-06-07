import random

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

        'apiKey': '6b32967165ca4a68a88fe7eef9160092'

    }

    if category:

        params['category'] = category

    if source:

        params['sources'] = source

    try:

        response = requests.get(url, params=params)

        response.raise_for_status()  # Raise an exception for non-2xx responses

        articles = response.json().get('articles', [])

        if articles:

            headlines = [article['title'] for article in articles]

            return headlines, articles

    except requests.exceptions.RequestException as e:

        print("Error fetching headlines:", e)

    return [], []

# Send a single headline with the "Change News" button

def send_headline(chat_id, headline, article):

    if not headline:

        app.send_message(chat_id, "No headlines found. Please try again later.")

        return

    keyboard = InlineKeyboardMarkup(

        [

            [InlineKeyboardButton("Read More", url=article['url'])],

            [InlineKeyboardButton("Change News", callback_data="change_news")],

            [InlineKeyboardButton("Help", callback_data="help")]

        ]

    )

    message = f"📰 {headline}\n\n{article['description']}"

    app.send_message(chat_id, message, reply_markup=keyboard)

# Command handler for /start and /help

@app.on_message(filters.command(["start", "help"]))

def handle_help_command(_, message):

    chat_id = message.chat.id

    help_text = """

    Welcome to the News Bot! Here are the available commands:

    

    /news - Get the latest news headline

    /random - Get a random news headline

    /category - Select a news category

    /source - Select a news source

    /trending - Get trending news

    /search - Search news articles

    /bookmark - Bookmark a news article

    /bookmarks - View bookmarked articles

    /subscribe - Subscribe to news updates

    /unsubscribe - Unsubscribe from news updates

    /settings - Manage bot settings

    /about - Information about the bot

    /feedback - Provide feedback

    /help - Show this help menu

    """

    app.send_message(chat_id, help_text)

# Command handler for /news

@app.on_message(filters.command("news"))

def handle_news_command(_, message):

    chat_id = message.chat.id

    headlines, articles = fetch_headlines()

    if headlines:

        send_headline(chat_id, headlines[0], articles[0])

# Command handler for /random

@app.on_message(filters.command("random"))

def handle_random_command(_, message):

    chat_id = message.chat.id

    headlines, articles = fetch_headlines()

    if headlines:

        random_index = random.randint(0, len(headlines) - 1)

        send_headline(chat_id, headlines[random_index], articles[random_index])

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

    headlines, articles = fetch_headlines(category=category)

    if headlines:

        send_headline(chat_id, headlines[0], articles[0])

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

    headlines, articles = fetch_headlines(source=source)

    if headlines:

        send_headline(chat_id, headlines[0], articles[0])

# Command handler for /trending

@app.on_message(filters.command("trending"))

def handle_trending_command(_, message):

    chat_id = message.chat.id

    headlines, articles = fetch_headlines(category='general')

    if headlines:

        send_headline(chat_id, headlines[0], articles[0])

# Command handler for /search

@app.on_message(filters.command("search"))

def handle_search_command(_, message):

    chat_id = message.chat.id

    app.send_message(chat_id, "Please enter the keyword or topic you want to search for.")

# Command handler for /bookmark

@app.on_message(filters.command("bookmark"))

def handle_bookmark_command(_, message):

    chat_id = message.chat.id

    app.send_message(chat_id, "Please provide the article URL you want to bookmark.")

# Command handler for /bookmarks

@app.on_message(filters.command("bookmarks"))

def handle_bookmarks_command(_, message):

    chat_id = message.chat.id

    app.send_message(chat_id, "Here are your bookmarked articles:")

# Command handler for /subscribe

@app.on_message(filters.command("subscribe"))

def handle_subscribe_command(_, message):

    chat_id = message.chat.id

    app.send_message(chat_id, "Please select the category or source you want to subscribe to.")

# Command handler for /unsubscribe

@app.on_message(filters.command("unsubscribe"))

def handle_unsubscribe_command(_, message):

    chat_id = message.chat.id

    app.send_message(chat_id, "Please select the category or source you want to unsubscribe from.")

# Command handler for /settings

@app.on_message(filters.command("settings"))

def handle_settings_command(_, message):

    chat_id = message.chat.id

    app.send_message(chat_id, "Here are your bot settings:")

# Command handler for /about

@app.on_message(filters.command("about"))

def handle_about_command(_, message):

    chat_id = message.chat.id

    app.send_message(chat_id, "This is a news bot that provides the latest headlines and articles.")

# Command handler for /feedback

@app.on_message(filters.command("feedback"))

def handle_feedback_command(_, message):

    chat_id = message.chat.id

    app.send_message(chat_id, "Please provide your feedback or report any issues with the bot.")

# Callback handler for the "Change News" button

@app.on_callback_query(filters.regex("change_news"))

def handle_change_news(_, callback_query):

    chat_id = callback_query.message.chat.id

    headlines, articles = fetch_headlines()

    if headlines:

        send_headline(chat_id, headlines[0], articles[0])

# Callback handler for the "Help" button

@app.on_callback_query(filters.regex("help"))

def handle_help_callback(_, callback_query):

    chat_id = callback_query.message.chat.id

    help_text = """

    Welcome to the News Bot! Here are the available commands:

    

    /news - Get the latest news headline

    /random - Get a random news headline

    /category - Select a news category

    /source - Select a news source

    /trending - Get trending news

    /search - Search news articles

    /bookmark - Bookmark a news article

    /bookmarks - View bookmarked articles

    /subscribe - Subscribe to news updates

    /unsubscribe - Unsubscribe from news updates

    /settings - Manage bot settings

    /about - Information about the bot

    /feedback - Provide feedback

    /help - Show this help menu

    """

    app.send_message(chat_id, help_text)

# Start the Pyrogram Client

app.start()

idle()
