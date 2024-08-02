# commands/list.py

import discord
from discord import app_commands
from discord.ext import commands
from utils.extract_items import load_items
from utils.paginator import Paginator

items = load_items('items.php')
items_list = [(item_id, name) for name, item_id in items.items()]

class ListPaginator(Paginator):
    def __init__(self, items, per_page=10):
        super().__init__(items, per_page)

class List(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="list", description="List all items")
    async def list(self, interaction: discord.Interaction):
        view = ListPaginator(items_list)
        await view.send_initial_message(interaction)

async def setup(bot):
    await bot.add_cog(List(bot))
