from threading import Thread

import discord
from flask import Flask

app = Flask('')

@app.route('/')
def home():
    return "hello world, i am abusing a free service"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

async def clear_testing_dms():
    client = discord.Client()
    messages_to_remove = 1000
    async for message in client.get_channel(829249725021814784).history(limit=messages_to_remove):
        if message.author.id == client.user.id:
            await message.delete()
