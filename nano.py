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
    # Fetch a random item (image, video, or gif) based on the 'anime' category from the Pixabay API
    url = f'https://pixabay.com/api/?key={PIXABAY_API_KEY}&q=anime&per_page=100'
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        if 'hits' in json_data:
            hits = json_data['hits']
            if hits:
                random_item = random.choice(hits)
                if 'webformatURL' in random_item:
                    item_url = random_item['webformatURL']
                    item_type = random_item['type']
                    if item_type == 'video':
                        # Send the fetched video as a video message
                        client.send_video(
                            chat_id=message.chat.id,
                            video=item_url,
                            caption="""➖➖➖➖➖➖➖➖➖➖➖➖
🟢ɴᴀᴍᴇ : Nano 
🟢ᴜꜱᴇʀɴᴀᴍᴇ : @SexyNano 
🟢ᴜꜱᴇʀ ɪᴅ : 6198858059 
🟢ʙᴅᴀy : 𝟶𝟹 ᴊᴜɴᴇ 
🟢ᴀɢᴇ :  18+
🟢ꜰʀᴏᴍ : ᴍᴀʜᴀʀᴀsʜᴛʀᴀ 
➖➖➖➖➖➖➖➖➖➖➖➖
ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ᴄʟɪᴄᴋ ʜᴇʀᴇ /help"""
                        )
                    elif item_type == 'gif':
                        # Send the fetched gif as an animation message
                        client.send_animation(
                            chat_id=message.chat.id,
                            animation=item_url,
                            caption="""➖➖➖➖➖➖➖➖➖➖➖➖
🟢ɴᴀᴍᴇ : Nano 
🟢ᴜꜱᴇʀɴᴀᴍᴇ : @SexyNano 
🟢ᴜꜱᴇʀ ɪᴅ : 6198858059 
🟢ʙᴅᴀy : 𝟶𝟹 ᴊᴜɴᴇ 
🟢ᴀɢᴇ :  18+
🟢ꜰʀᴏᴍ : ᴍᴀʜᴀʀᴀsʜᴛʀᴀ 
➖➖➖➖➖➖➖➖➖➖➖➖
ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ᴄʟɪᴄᴋ ʜᴇʀᴇ /help"""
                        )
                    else:
                        # Send the fetched image as a photo message
                        client.send_photo(
                            chat_id=message.chat.id,
                            photo=item_url,
                            caption="""➖➖➖➖➖➖➖➖➖➖➖➖
🟢ɴᴀᴍᴇ : Nano 
🟢ᴜꜱᴇʀɴᴀᴍᴇ : @SexyNano 
🟢ᴜꜱᴇʀ ɪᴅ : 6198858059 
🟢ʙᴅᴀy : 𝟶𝟹 ᴊᴜɴᴇ 
🟢ᴀɢᴇ :  18+
🟢ꜰʀᴏᴍ : ᴍᴀʜᴀʀᴀsʜᴛʀᴀ 
➖➖➖➖➖➖➖➖➖➖➖➖
ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ᴄʟɪᴄᴋ ʜᴇʀᴇ /help"""
                        )
                    

@app.on_message(filters.command("help"))
def help_command(client, message):
    help_text = "Available commands:\n\n" \
                "/start - Start the bot\n" \
                "/help - Display this help message\n" \
                "/echo [text] - Echo back the provided text\n" \
                "/caps [text] - Capitalize the provided text\n" \
                "/mybots - Show an my bots\n" \
                "/random - Gen random number\n" \
                "/img [text] - Gen image through api\n" \
                "✧━━━━━▣✧❅✦❅✧▣━━━━━✧"

    inline_keyboard = [
        [InlineKeyboardButton("Instagram", url="https://www.instagram.com/itz_kunu_g")],
        [InlineKeyboardButton("WhatsApp", url="https://wa.me/15614040726")],
        [InlineKeyboardButton("Telegram", url="https://t.me/Anime_Krew")],
        [InlineKeyboardButton("GitHub", url="https://github.com/")]
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


@app.on_message(filters.command("mybots"))
def inline_command(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Ken Kaneki", callback_data="btn1"),
                InlineKeyboardButton("Komi", callback_data="btn2")
            ],
            [
                InlineKeyboardButton("Ego", callback_data="btn3"),
                InlineKeyboardButton("Server", callback_data="btn4")
            ]
        ]
    )
    client.send_message(chat_id=message.chat.id, text="My All Bot List More Bot Coming Soon:", reply_markup=keyboard)


@app.on_callback_query()
def handle_callback(client, callback_query):
    data = callback_query.data
    message = callback_query.message
    if data == "btn1":
        client.send_message(chat_id=message.chat.id, text="ᴛʜᴇ ᴍᴏsᴛ ᴩᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴩ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs. ʙᴏᴛ : @Ken_Kaneki_ProBot")
    elif data == "btn2":
        client.send_message(chat_id=message.chat.id, text="ᴛʜᴇ ᴍᴏsᴛ ᴩᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴩ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs. ʙᴏᴛ : @TheKomi_Bot")
    elif data == "btn3":
        client.send_message(chat_id=message.chat.id, text="ᴀ sɪᴍᴘʟᴇ ғɪʟᴇ ʀᴇɴᴀᴍᴇ + ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ ᴄᴏɴᴠᴇʀᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ & ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ sᴜᴘᴘᴏʀᴛ : @JinpachiEgo_RenameBot")
    elif data == "btn4":
        client.send_message(chat_id=message.chat.id, text="I deployed All bots in vps Or 24/7 working bots")

        
import requests
import urllib.parse

@app.on_message(filters.command("img"))
def send_image(client, message):
    # Get the query from the command arguments
    command_args = message.command[1:]  # Exclude the command itself
    query = ' '.join(command_args) if command_args else 'random'

    # Fetch an image based on the user's query from the Pixabay API
    encoded_query = urllib.parse.quote(query)
    url = f'https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={encoded_query}&image_type=photo&per_page=100'
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
                        caption=f'Here is an image for "{query}"'
                    )








# Handler for new chat members
@app.on_message(filters.new_chat_members)
def welcome_new_members(client, message):
    chat_id = message.chat.id
    welcome_image_url = "https://graph.org/file/5150888e4063675f2a0c7.jpg"

    # Download the welcome image
    response = requests.get(welcome_image_url)
    if response.status_code == 200:
        with open("https://graph.org/file/5150888e4063675f2a0c7.jpg", "wb") as file:
            file.write(response.content)
    else:
        print("Failed to download the welcome image")

    # Send the welcome message with the image
    sent_message = client.send_photo(
        chat_id=chat_id,
        photo="https://graph.org/file/5150888e4063675f2a0c7.jpg",
        caption="Welcome to the group!"
    )
    # Reply to the new members' message with the welcome message
    client.reply_to_message(
        chat_id=chat_id,
        message_id=message.message_id,
        reply_to_message_id=sent_message.message_id
    )



        
app.run()
print("bot started....")
idle()
       
    
