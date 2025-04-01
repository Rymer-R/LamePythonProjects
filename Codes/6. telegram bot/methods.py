from pyrogram import Client, emoji, filters
from pyrogram.enums import ChatType
from pyrogram import errors
import json
import aiofiles

#define some contants

CHAT_TYPES = {
    ChatType.CHANNEL: "Channel",
    ChatType.GROUP: "Group",
    ChatType.SUPERGROUP: "Supergroup",
    ChatType.BOT: "Bot",
    ChatType.PRIVATE: "User"
}


async def get_target_user(message, client): #returns user or NoneType
    """
    Returns the user who was mentioned or replied while using the command.

    :param message: Message recieved from the client.
    :param client: Pass the client parameter passed in the function.
    """
    try:    
        if len(message.command) > 1: #checks if it contains username or id (no type casting required luckily)
            user = await client.get_chat(message.command[1])
        elif message.reply_to_message: #checks if the user has replied any message
            user = await client.get_chat(message.reply_to_message.from_user.id) # get id => use get_chat() for additional attributes
        else:
            user = None
    except Exception as e:
        print(e)
        return None
    else:
        return user

async def process_user_type(user) -> str:
    """
    Returns a usable string corresponding to CHAT_TYPES dictionary.

    :param user: User of the type User in pyrogram.
    """
    type = CHAT_TYPES[user.type] #only works if we use client.get_chat(), client.get_users() doesn't have the type attribute
    return type

async def convert_json(path : str) -> dict:
    """
    Converts a json file to dictionary using the json module in python.

    :param path: Path of the json file.
    """
    async with aiofiles.open(path, "r") as file:
        file_contents = await file.read()
    contents = json.loads(file_contents)
    return contents
