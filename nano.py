from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import subprocess

# Set your bot token here
TOKEN = '6206599982:AAG374J4c9eb0v2-3cbDMq4yjj97PuMIyB0'

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your own API credentials
API_ID = '16743442'
API_HASH = '12bbd720f4097ba7713c5e40a11dfd2a'

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)


import requests

# Replace 'YOUR_PIXABAY_API_KEY' with your own Pixabay API key
PIXABAY_API_KEY = '37055792-a3457117bfde7b1012045092b'

@app.on_message(filters.command("start"))
def start_command(client, message):
    # Fetch a random image from the Pixabay API
    url = f'https://pixabay.com/api/?key={PIXABAY_API_KEY}&per_page=100'
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        if 'hits' in json_data:
            hits = json_data['hits']
            if hits:
                random_image = random.choice(hits)
                if 'webformatURL' in random_image:
                    image_url = random_image['webformatURL']
                    # Send the fetched image as a photo message
                    client.send_photo(
                        chat_id=message.chat.id,
                        photo=image_url,
                        caption='Welcome to the About Nano Bot !\nTry /help'
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

    inline_keyboard = [
        [InlineKeyboardButton("Instagram", url="https://www.instagram.com/itz_kunu_g")],
        [InlineKeyboardButton("WhatsApp", url="https://wa.me/15614040726")],
        [InlineKeyboardButton("Telegram", url="https://t.me/Anime_Krew")],
        [InlineKeyboardButton("GitHub", url="https://github.com/Soon")]
    ]

    reply_markup = InlineKeyboardMarkup(inline_keyboard)

    client.send_message(chat_id=message.chat.id, text=help_text, reply_markup=reply_markup)


@app.on_message(filters.command("echo"))
def echo_command(client, message):
    # Remove the command from the message text
    text = message.text.replace("/echo", "").strip()
    if text:
        client.send_message(chat_id=message.chat.id, text=text)
    else:
        client.send_message(chat_id=message.chat.id, text="Please provide some text to echo.")


@app.on_message(filters.command("gitpull"))
def gitpull_command(client, message):
    repository_url = "https://github.com/PyroUserBot/Nano"

    # Run git pull command
    result = subprocess.run(['git', 'pull', repository_url], capture_output=True, text=True)
    output = result.stdout.strip() if result.stdout else result.stderr.strip()

    if result.returncode == 0:
        success_message = "Git pull successful. Repository is up to date."
        client.send_message(chat_id=message.chat.id, text=success_message)
    else:
        error_message = f"Git pull failed. Error message: {output}"
        client.send_message(chat_id=message.chat.id, text=error_message)

    # Install required packages
    subprocess.run(['pip3', 'install', '-r', 'requirements.txt'])

    # Run python3 nano.py
    subprocess.run(['python3', 'nano.py'])


 #━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("random"))
def random_number_command(client, message):
    # Remove the command from the message text
    text = message.text.replace("/random", "").strip()
    if text:
        try:
            min_value, max_value = map(int, text.split())
            if min_value < max_value:
                random_num = random.randint(min_value, max_value)
                client.send_message(chat_id=message.chat.id, text=f"Random number: {random_num}")
            else:
                client.send_message(chat_id=message.chat.id, text="Invalid input. Please provide a valid range.")
        except ValueError:
            client.send_message(chat_id=message.chat.id, text="Invalid input. Please provide a valid range.")
    else:
        client.send_message(chat_id=message.chat.id, text="Please provide a range of numbers.")

#━━━━━━━━━━━━━━━━━━━━━━━
        
        
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
        client.send_message(chat_id=message.chat.id, text="You clicked button 1")
    elif data == "btn2":
        client.send_message(chat_id=message.chat.id, text="You clicked button 2")
    elif data == "btn3":
        client.send_message(chat_id=message.chat.id, text="You clicked button 3")
    elif data == "btn4":
        client.send_message(chat_id=message.chat.id, text="You clicked button 4")


        
app.run()
print("bot started....")
idle()
       
    
