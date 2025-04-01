#No one will see this but...
#Spare me for the poor code i started coding just a month ago with only 4-5 days of experience 

from methods import *
from pyrogram import Client, emoji, filters
from pyrogram.enums import ChatType
import json

print("getting credentials...")
with open("cred.json", 'r') as file:
    credentials_json = file.read()
credentials = json.loads(credentials_json)

#Place API_ID, API_HASH, BOT_TOKEN in credentials.json

API_ID = credentials["API_ID"]
API_HASH = credentials["API_HASH"]
BOT_TOKEN = credentials["BOT_TOKEN"]

plugins = dict(root = "plugins")
app = Client("my_account", api_id = API_ID, api_hash = API_HASH, bot_token = BOT_TOKEN, plugins = plugins)

print("bot is running")
app.run()