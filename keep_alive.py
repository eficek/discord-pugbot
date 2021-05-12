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
