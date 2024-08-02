import discord
from discord.ext import commands, tasks
from config import BOT_TOKEN, ITEMS_URL, CHECK_INTERVAL
from utils.updater import check_for_updates
import asyncio
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, handlers=[
    logging.FileHandler('web/logs.txt', 'a', 'utf-8'),
    logging.StreamHandler(sys.stdout)
])

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@tasks.loop(seconds=CHECK_INTERVAL)
async def check_updates():
    updated = await check_for_updates('items.php', ITEMS_URL)
    if updated:
        logging.info("Items.php has been updated.")
        # Reload the extensions to refresh the item data
        await bot.reload_extension('commands.find')
        await bot.reload_extension('commands.list')

async def load_extensions():
    await bot.load_extension('commands.find')
    await bot.load_extension('commands.list')
    await bot.load_extension('commands.update')

@bot.event
async def on_ready():
    await bot.tree.sync()
    logging.info(f'Logged in as {bot.user}')
    check_updates.start()

async def main():
    await load_extensions()
    await bot.start(BOT_TOKEN)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot is shutting down...")
