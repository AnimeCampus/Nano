import os

import re

import openai

from pyrogram import Client, filters, idle

# Set up your OpenAI API credentials

openai.api_key = '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'

# Set up your Telegram Bot API credentials

bot_token = '6206599982:AAEtRoU2jV7heQn8t0Zkwh1L6khiC8EXfcM'

bot = Client('my_bot', bot_token=bot_token)

# Define the command handlers

@bot.on_message(filters.command("ask", prefixes="/"))

def ask_command(client, message):

    # Get the user's query from the message text

    query = re.sub(r'/ask\s*', '', message.text, flags=re.IGNORECASE)

    # Call the OpenAI API to get the AI's response

    response = openai.Completion.create(

        engine='text-davinci-003',

        prompt=query,

        max_tokens=50,

        n=1,

        stop=None,

        temperature=0.7

    )

    # Send the AI's response back to the user

    bot.send_message(chat_id=message.chat.id, text=response.choices[0].text)

@bot.on_message(filters.command("code", prefixes="/"))

def code_command(client, message):

    # Get the user's code from the message text

    code = re.sub(r'/code\s*', '', message.text, flags=re.IGNORECASE)

    # Execute the user's code and capture the output

    try:

        output = eval(code)

    except Exception as e:

        output = str(e)

    # Send the output back to the user

    bot.send_message(chat_id=message.chat.id, text=str(output))

@bot.on_message(filters.command("fun", prefixes="/"))

def fun_command(client, message):

    # Define some fun responses

    responses = [

        "Sure, I'm always up for some fun!",

        "Let's have some fun together!",

        "I'm ready for some fun! What do you have in mind?"

    ]

    # Select a random fun response and send it back to the user

    response = random.choice(responses)

    bot.send_message(chat_id=message.chat.id, text=response)

# Start the bot

bot.run()
idle()
