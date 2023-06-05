from pyrogram import Client
from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Set your bot token here
TOKEN = '6206599982:AAG374J4c9eb0v2-3cbDMq4yjj97PuMIyB0'

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your own API credentials
API_ID = '16743442'
API_HASH = '12bbd720f4097ba7713c5e40a11dfd2a'

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN) 
    


@app.on_message(filters.command("start"))
def start_command(client, message):
    client.send_message(chat_id=message.chat.id, text='Welcome to the Telegram Bot!\n try /help ')


@app.on_message(filters.command("help"))
def help_command(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Instagram", url="https://www.instagram.com/itz_kunu_g"),
                InlineKeyboardButton("GitHub", url="https://github.com/?")
            ],
            [
                InlineKeyboardButton("WhatsApp", url="https://wa.me/+15614040726"),
                InlineKeyboardButton("Telegram", url="https://t.me/SexyNano")
            ]
        ]
    )
    client.send_message(chat_id=message.chat.id, text="This is my some social media acc", reply_markup=keyboard)


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


app.run()
idle()
