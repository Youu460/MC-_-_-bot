from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

@Client.on_message(filters.private & filters.command("deltime"))
async def deltime_handler(client: Client, message: Message):
    args = message.text.split()
    if len(args) != 2 or not args[1].isdigit():
        return await message.reply("Usage: `/deltime <seconds>`", quote=True)

    delay = int(args[1])
    sent = await message.reply("This message will self-destruct in {} seconds.".format(delay))
    await asyncio.sleep(delay)
    try:
        await sent.delete()
        await message.delete()
    except Exception as e:
        print(f"Failed to delete messages: {e}")
