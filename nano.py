from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

# Set your bot token here
TOKEN = '6206599982:AAG374J4c9eb0v2-3cbDMq4yjj97PuMIyB0'

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your own API credentials
API_ID = '16743442'
API_HASH = '12bbd720f4097ba7713c5e40a11dfd2a'

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)




greeting_images = [
    '360_F_87970620_Tdgw6WYdWnrZHn2uQwJpVDH4vr4PINScjpg',
    'https://graph.org/file/03e0a8175f7c66e56b8d9.jpg',
    'https://graph.org/file/8629469fb4e00f32d2a6f.jpg',
    # Add more image filenames here
]

@app.on_message(filters.command("start"))
def start_command(client, message):
    # Select a random greeting image
    random_image = random.choice(greeting_images)
    
    # Send the selected greeting image
    client.send_photo(
        chat_id=message.chat.id,
        photo=random_image,
        caption='Welcome to the Telegram Bot!\nTry /help'
    )

@app.on_message(filters.command("help"))
def help_command(client, message):
    help_text = "Available commands:\n\n" \
                "/start - Start the bot\n" \
                "/help - Display this help message\n" \
                "/instagram - Follow us on Instagram\n" \
                "/whatsapp - Contact us on WhatsApp\n" \
                "/telegram - Join our Telegram group\n" \
                "/github - Check out our GitHub repository\n" \
                "/echo [text] - Echo back the provided text\n" \
                "/caps [text] - Capitalize the provided text\n" \
                "/inline - Show an example of an inline keyboard"

    client.send_message(chat_id=message.chat.id, text=help_text)


@app.on_message(filters.command("instagram"))
def instagram_command(client, message):
    client.send_message(chat_id=message.chat.id, text="Follow us on Instagram: @your_instagram_account")


@app.on_message(filters.command("whatsapp"))
def whatsapp_command(client, message):
    client.send_message(chat_id=message.chat.id, text="Contact us on WhatsApp: +123456789")


@app.on_message(filters.command("telegram"))
def telegram_command(client, message):
    client.send_message(chat_id=message.chat.id, text="Join our Telegram group: t.me/your_group")


@app.on_message(filters.command("github"))
def github_command(client, message):
    client.send_message(chat_id=message.chat.id, text="Check out our GitHub repository: github.com/your_repository")


@app.on_message(filters.command("echo"))
def echo_command(client, message):
    # Remove the command from the message text
    text = message.text.replace("/echo", "").strip()
    if text:
        client.send_message(chat_id=message.chat.id, text=text)
    else:
        client.send_message(chat_id=message.chat.id, text="Please provide some text to echo.")


@app.on_message(filters.command("caps"))
def caps_command(client, message):
    # Remove the command from the message text
    text = message.text.replace("/caps", "").strip()
    if text:
        caps_text = text.upper()
        client.send_message(chat_id=message.chat.id, text=caps_text)
    else:
        client.send_message(chat_id=message.chat.id, text="Please provide some text to capitalize.")


@app.on_message(filters.command("inline"))
def inline_command(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Button 1", callback_data="btn1"),
                InlineKeyboardButton("Button 2", callback_data="btn2")
            ],
            [
                InlineKeyboardButton("Button 3", callback_data="btn3"),
                InlineKeyboardButton("Button 4", callback_data="btn4")
            ]
        ]
    )
    client.send_message(chat_id=message.chat.id, text="Inline Keyboard Example:", reply_markup=keyboard)


@app.on_callback_query()
def handle_callback(client, callback_query):
    data = callback_query.data
    message = callback_query.message
    if data == "btn1":
        client.send_message(chat_id=message.chat.id, text="You clicked Button button 1") 

app.run()
idle()
       
    
