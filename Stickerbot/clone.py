import os
import shutil
import logging
from pyrogram import Client, filters

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up Pyrogram client
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define the command handler
@app.on_message(filters.command(["clone"], prefixes=".") & filters.private)
async def clone_pack(client, message):
    # Prompt the user for the pack name and ID
    pack_name = await client.ask(message.chat.id, "What is the name of the sticker pack you want to clone?")
    pack_id = await client.ask(message.chat.id, "What is the ID of the sticker pack you want to clone?")

    # Create the pack directory if it doesn't exist
    if not os.path.exists(pack_name):
        os.mkdir(pack_name)

    # Copy the pack file and thumbnail to the new directory
    pack_file = f"{pack_id}.webp"
    pack_thumb = f"{pack_id}.tgs"
    shutil.copyfile(f"stickers/{pack_file}", f"{pack_name}/{pack_file}")
    shutil.copyfile(f"stickers/{pack_thumb}", f"{pack_name}/{pack_thumb}")

    # Inform the user that the pack has been cloned
    await message.reply_text(f"The {pack_name} sticker pack has been cloned!")

# Start the client
app.run()
