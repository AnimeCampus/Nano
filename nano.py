import random
import os
import openai
from pyrogram import Client, filters, idle

# Set up your OpenAI API credentials
openai.api_key = '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'

# Set up your Telegram Bot API credentials
bot_token = '6206599982:AAEtRoU2jV7heQn8t0Zkwh1L6khiC8EXfcM'

# Set up your Pyrogram API credentials
api_id = '16743442'
api_hash = '12bbd720f4097ba7713c5e40a11dfd2a'

# Create the bot instance
bot = Client('my_bot', bot_token=bot_token, api_id=api_id, api_hash=api_hash)

# Define the command handlers
@bot.on_message(filters.command("ask", prefixes="/"))
def ask_command(client, message):
    # Get the user's query from the message text
    query = message.text.split(maxsplit=1)[1]

    # Call the OpenAI API to get the AI's response
    try:
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
    except Exception as e:
        bot.send_message(chat_id=message.chat.id, text=f"An error occurred: {str(e)}")

@bot.on_message(filters.command("code", prefixes="/"))
def code_command(client, message):
    # Get the user's code from the message text
    code = message.text.split(maxsplit=1)[1]

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
bot.start()
idle()
