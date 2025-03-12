'''6th Project for LamePythonProjects'''
# A simple telegram bot which I will call essentials bot for now
# Installed some mayuri pyrofork which is fork of pyrogram according to my friend

from pyrogram import Client, emoji, filters
from pyrogram.errors import RPCError
from pyrogram.enums import ChatType

chat_types = {
    ChatType.CHANNEL: "Channel",
    ChatType.GROUP: "Group",
    ChatType.SUPERGROUP: "Supergroup",
    ChatType.BOT: "Bot",
    ChatType.PRIVATE: "User"
}

# copied minimal app from pyrofork docs
# --from here--
api_id =
api_hash = ""
bot_token = ""

app = Client("my_account", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

'''This is the minimal code I copied for start command'''


@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Bot is running...", quote=True)


# --to here--


# Main commands
# I think i will make a greet command just to understand how all this pyrogram thing works
@app.on_message(filters.command("greet"))
async def greet(client, message):
    user = None
    error_message = None
    # so the command can be used either by replying someone or just mentioning someone by their usename
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        user = await app.get_users(user_id)  # Lol had errors for about half an hour, forgot to add "await"
    elif len(
            message.command) > 1:  # didn't find any suitable way of getting arguments, this looks odd but documenation had only this method
        try:
            arg = message.command[1] if message.command[1].startswith("@") else int(message.command[1])
            user = await app.get_users(arg)
        except ValueError:
            error_message = "Please provide a valid username or user ID"
        except Exception as e:
            if "USERNAME_NOT_OCCUPIED" in str(e) or "USERNAME_INVALID" in str(e):
                error_message = "No account exists with that username"
            elif "USER_ID_INVALID" in str(e) or "PEER_ID_INVALID" in str(e):
                error_message = "Invalid user ID"  # user_id_invalid and peer_id_invalid looks like the same error but as far as this is working I think I will not change it for now
            else:
                error_message = f"Error: {e}"  # handling other errors clearly
    else:
        user_id = message.from_user.id
        user = await app.get_users(user_id)
    if user:
        await message.reply(
            f"Hello [{user.first_name}](tg://user?id={user.id})")  # looked up some formating and used [text](link) formatting in this line
    elif error_message:
        await message.reply(error_message)

    # -----NOTES FOR ME for the future for /greet command-----
    # okay so, what we did in the greet method is quite to the point,
    # at the end of the code we just need a "user" which we will greet, either we get user or we get error
    # I summed up some errors like USER_ID_INVALID into except blocks,
    # errors are quite long and not proper strings** but these are the keywords which should work for handling errors


# A help command T-T, something easy finally
@app.on_message(filters.command("help"))
async def help_command(client, message):
    help_commands = ("Here are a list of commands:\n\n"
                     "/start - checks if the bot is running\n"
                     "/greet - greets the user or the replied user\n"
                     "/help - get a list of commands\n"
                     "/essentials - things essential can do or configure essentials(soon)\n")
    # I surely imagined so many commands right now,but don't even know if I will be able to make all of them T-T
    await message.reply(help_commands)


# something semething reserved for later
@app.on_message(filters.command("essentials"))
async def essentials(client, message):
    await message.reply("Command will be made usable soon!")


# before making /info command, i should see how can I get my own info in the chat
@app.on_message(filters.command("me"))
async def me(client, message):
    user = await app.get_users(message.from_user.id)  # okay
    await message.reply(f"**Your info:**\n"
                        f"First Name: **{user.first_name}**\n"
                        f"Last Name: **{user.last_name}**\n"
                        f"User ID: `{user.id}`\n"
                        f"Username: @{user.username}\n"  # two more formating used **.** for bold and `.` for monospace
                        f"DC: **{user.dc_id}**\n"
                        f"Link: [Click](https://t.me/{user.username})"
                        , disable_web_page_preview=True  # to avoid the embed kind of thing
                        )


@app.on_message(filters.command("kick"))
async def kick(client, message):
    if message.chat.type not in (ChatType.SUPERGROUP, ChatType.GROUP):
        await message.reply(f"This command can't be used in private chats")
        return
    user_id = None
    # if the command is used with a reply
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    # if the command has arguments
    elif len(message.command) > 1:
        arg = message.command[1]
        if arg.startswith("@"):  # checking for username
            user_id = arg
        else:  # else id, will have to convert it to int
            try:
                user_id = int(arg)
            except ValueError:  # apparently this also handles the arguments without "@"
                await message.reply("Please provide a valid username or user ID.")
                return
    # handling the None type when user neither replies norr gives an argument
    if not user_id:
        await message.reply("Please reply to a user or provide a valid username/user ID.")
        return
    # handling if the user does not exist or (invalid id or username)
    try:
        # getting user
        user = await client.get_chat(user_id)
        # getting the type of user
        user_type = user.type
        chat_type = chat_types[user_type]
        if chat_type == "User":
            await app.ban_chat_member(message.chat.id, user.id)
            await app.unban_chat_member(message.chat.id, user.id)
            await message.reply(
                f"Kicked **{user.first_name}**"
            )
        else:
            await message.reply(f"Can't kick/ban a {chat_type.lower()}")
    except Exception as e:
        error_message = str(e).lower()
        if "peer id invalid" in error_message or \
                "peer_id_invalid" in error_message or \
                "python int too large to convert to sqlite integer":
            await message.reply("Invalid User ID.")
        elif "username not occupied" in error_message or "username_not_occupied" in error_message:
            await message.reply("No account exists with that username.")
        else:
            await message.reply(f"Error: {e}")


@app.on_message(filters.command("ban"))
async def ban(client, message):
    pass


@app.on_message(filters.command("unban"))
async def unban(client, message):
    pass


@app.on_message(filters.command("id"))
async def id_command(client, message):
    user_id = None
    # if the command is used with a reply
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    # if the command has arguments
    elif len(message.command) > 1:
        arg = message.command[1]
        if arg.startswith("@"):  # checking for username
            user_id = arg
        else:  # else id, will have to convert it to int
            try:
                user_id = int(arg)
            except ValueError:  # apparently this also handles the arguments without "@"
                await message.reply("Please provide a valid username or user ID.")
                return
    # handling the None type when user neither replies norr gives an argument
    if not user_id:
        await message.reply("Please reply to a user or provide a valid username/user ID.")
        return
    # handling if the user does not exist or (invalid id or username)
    try:
        # getting user
        user = await client.get_chat(user_id)
        user_type = user.type
        # getting the type of chat
        chat_type = chat_types[user_type]
        # the final info
        await message.reply(
            f"The {chat_type.lower()} {user.first_name if user.first_name else user.title} ID is `{user.id}`")
    except Exception as e:
        error_message = str(e).lower()
        if "peer id invalid" in error_message or "peer_id_invalid" in error_message:
            await message.reply("Invalid User ID.")
        elif "username not occupied" in error_message or "username_not_occupied" in error_message:
            await message.reply("No account exists with that username.")
        else:
            await message.reply(f"Error: {e}")


@app.on_message(filters.command("info"))
async def info(client, message):
    user_id = None
    # if the command is used with a reply
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    # if the command has arguments
    elif len(message.command) > 1:
        arg = message.command[1]
        if arg.startswith("@"):  # checking for username
            user_id = arg
        else:  # else id, will have to convert it to int
            try:
                user_id = int(arg)
            except ValueError:  # apparently this also handles the arguments without "@"
                await message.reply("Please provide a valid username or user ID.")
                return
    # handling the None type when user neither replies norr gives an argument
    if not user_id:
        await message.reply("Please reply to a user or provide a valid username/user ID.")
        return
    # handling if the user does not exist or (invalid id or username)
    try:
        # getting user
        user = await client.get_chat(user_id)
        # getting the type of user
        user_type = user.type
        chat_type = chat_types[user_type]
        # the final info
        user_link = f"[Click](https://t.me/{user.username})"
        await message.reply(
            f"**{chat_type} info:**\n"
            f"First Name: **{user.first_name if user.first_name else user.title}**\n"
            f"Last Name: **{user.last_name if user.last_name else 'N/A'}**\n"
            f"ID: `{user.id}`\n"
            f"Username: @{user.username}\n"
            f"DC: **{user.dc_id}**\n"
            f"Link: {user_link}"
            , disable_web_page_preview=True
        )
    except Exception as e:
        error_message = str(e).lower()
        if "peer id invalid" in error_message or \
                "peer_id_invalid" in error_message or \
                "python int too large to convert to sqlite integer":
            await message.reply("Invalid User ID.")
        elif "username not occupied" in error_message or "username_not_occupied" in error_message:
            await message.reply("No account exists with that username.")
        else:
            await message.reply(f"Error: {e}")


print("Bot is running")

app.run()
