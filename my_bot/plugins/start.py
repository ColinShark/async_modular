from pyrogram import Filters, Message, Emoji
# Import the Filters, Message and Emoji modules of Pyrogram

from ..my_bot import My_Bot
# Import our bot we set up


# Filter for all messages that are the command /running
# and were sent by ourselfs
@My_Bot.on_message(Filters.command("running") & Filters.me)
async def start(app: My_Bot, message: Message):
    await message.edit("Bot is running " + Emoji.THUMBS_UP)
    # Edit the message we are handling
