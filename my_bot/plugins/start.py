from pyrogram import Filters, Message, Emoji

from ..my_bot import My_Bot


@My_Bot.on_message(Filters.command("running") & Filters.me)
async def start(app: My_Bot, message: Message):
    await message.edit("Bot is running " + Emoji.THUMBS_UP)
