from methods import *
from pyrogram import Client, emoji, filters
from pyrogram import enums

@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("I am Alive and Running...", quote = True)

@Client.on_message(filters.command("greet"))
async def greet(client, message):
    user = await get_target_user(message, client)
    if not user:
        user = await client.get_chat(message.from_user.id) #always prefer get_chat over get_users because it has more attributes and works for bots, channels, groups
    GREET = f"Hello [{user.first_name}](tg://user?id={user.id})"
    await message.reply(GREET, quote = True)

@Client.on_message(filters.command("help"))
async def help(client, message):
    commands = await convert_json("commands.json")
    help = []
    for command in commands:
        format = f"**--{command}:--**\nUsage: `{commands[command]['usage']}`\nDescription: {commands[command]['description']}"
        help.append(format)
    await message.reply("\n\n".join(help), quote = True, parse_mode = enums.ParseMode.MARKDOWN)

@Client.on_message(filters.command("info"))
async def info(client, message):
    user = await get_target_user(message, client)
    if not user:
        await message.reply("Provide a valid User" , quote = True)
    else:
        type = await process_user_type(user)
        info = ["**Info:**"]
        if user.first_name:
                info.append(f"**First Name:** {user.first_name}")
        if user.last_name:
                info.append(f"**Last Name:** {user.last_name}")
        if user.title:
                info.append(f"**Title:** {user.title}")
        info.extend([f"**ID**: `{user.id}`", f"**Username**: @{user.username}", f"**DC**: {user.dc_id}", f"**Type**: `{type}`", f"**User Link**: [link](tg://user?id={user.id})"])
        await message.reply("\n".join(info), quote = True, parse_mode = enums.ParseMode.MARKDOWN)

@Client.on_message(filters.command("purge"))
async def purge(client, message):
    chat_id = message.chat.id
    ...
    # will continue with this 