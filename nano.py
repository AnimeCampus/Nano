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

    
  
import os

import sys

from os import environ, execle, system

from git import Repo

from git.exc import InvalidGitRepositoryError

from pyrogram import Client, filters

from pyrogram.types import Message

# Initialize your Pyrogram client

app = Client("my_bot")

# Replace 'YOUR_ADMINS_LIST' with a list of user IDs of the bot admins

ADMINS = [6198858059]

UPSTREAM_REPO = "https://github.com/PyroUserBot/Nano"

def gen_chlog(repo, diff):

    upstream_repo_url = Repo().remotes[0].config_reader.get("url").replace(".git", "")

    ac_br = repo.active_branch.name

    ch_log = ""

    tldr_log = ""

    ch = f"<b>updates for <a href={upstream_repo_url}/tree/{ac_br}>[{ac_br}]</a>:</b>"

    ch_tl = f"updates for {ac_br}:"

    d_form = "%d/%m/%y || %H:%M"

    for c in repo.iter_commits(diff):

        ch_log += (

            f"\n\n💬 <b>{c.count()}</b> 🗓 <b>[{c.committed_datetime.strftime(d_form)}]</b>\n<b>"

            f"<a href={upstream_repo_url.rstrip('/')}/commit/{c}>[{c.summary}]</a></b> 👨‍💻 <code>{c.author}</code>"

        )

        tldr_log += f"\n\n💬 {c.count()} 🗓 [{c.committed_datetime.strftime(d_form)}]\n[{c.summary}] 👨‍💻 {c.author}"

    if ch_log:

        return str(ch + ch_log), str(ch_tl + tldr_log)

    return ch_log, tldr_log
def updater():
    try:
        repo = Repo()

    except InvalidGitRepositoryError:

        repo = Repo.init()
        origin = repo.create_remote("upstream", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    ac_br = repo.active_branch.name
    if "upstream" in repo.remotes:
        ups_rem = repo.remote("upstream")
    else:
        ups_rem = repo.create_remote("upstream", UPSTREAM_REPO)
    ups_rem.fetch(ac_br)
    changelog, tl_chnglog = gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    return bool(changelog)
@app.on_message(filters.command("update") & filters.user(ADMINS))
async def update_bot(_, message: Message):
    chat_id = message.chat.id
    msg = await message.reply_text("Checking updates...")
    update_avail = updater()
    if update_avail:
        await msg.edit("✅ Update finished!")
        system("git pull -f && pip3 install --no-cache-dir -r requirements.txt")
        execle(sys.executable, sys.executable, "main.py", environ)
        return
    await msg.edit(
        f"Bot is **up-to-date** with branch [master]({UPSTREAM_REPO}/tree/master)",
        disable_web_page_preview=True,
    )
@app.on_message(filters.command("restart") & filters.user(ADMINS))
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply_text("`Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!") 

  
    

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

@app.on_callback_query()
def handle_callback(client, callback_query):
    data = callback_query.data
    message = callback_query.message
    if data == "btn2":
        client.send_message(chat_id=message.chat.id, text="You clicked button 2") 

        
@app.on_callback_query()
def handle_callback(client, callback_query):
    data = callback_query.data
    message = callback_query.message
    if data == "btn3":
        client.send_message(chat_id=message.chat.id, text="You clicked button 3") 
     
@app.on_callback_query()
def handle_callback(client, callback_query):
    data = callback_query.data
    message = callback_query.message
    if data == "btn4":
        client.send_message(chat_id=message.chat.id, text="You clicked button 4") 
        
app.run()
idle()
       
    
