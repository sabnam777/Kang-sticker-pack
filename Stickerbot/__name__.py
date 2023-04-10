
import asyncio

import importlib

import sys

import os

from pyrogram import Client

from pyrogram.types import Message

import kang

import clone

bot = Client("my_bot", bot_token=os.environ["BOT_TOKEN"], api_id=os.environ["API_ID"], api_hash=os.environ["API_HASH"])

@bot.on_message(filters.private)

async def ask_pack_id(client: Client, message: Message):

    if message.text.startswith("/clone"):

        pack_name = await message.reply_text("Please enter the name of the sticker pack you want to clone:")

        pack_id = await bot.ask(message.chat.id, "Please enter the ID of the sticker pack you want to clone:")

        await clone.clone_pack(pack_name.text, pack_id.text, message.chat.id)

async def main():

    await bot.start()

    kang.bot = bot

    await kang.init()

    for all_module in kang.ALL_MODULES:

        importlib.import_module("kang.modules" + all_module)

    await bot.idle()

if __name__ == "__main__":

    asyncio.get_event_loop().run_until_complete(main())
    
