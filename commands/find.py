# commands/find.py

import discord
from discord import app_commands
from discord.ext import commands
from utils.extract_items import load_items
from utils.paginator import Paginator

items = load_items('items.php')

class FindPaginator(Paginator):
    def __init__(self, items, per_page=10):
        super().__init__(items, per_page, title="Search Results", color=discord.Color.green())

class Find(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="find", description="Find items by name")
    async def find(self, interaction: discord.Interaction, name: str):
        name_lower = name.lower()
        matching_items = [(item_id, name) for name, item_id in items.items() if name_lower in name]
        if matching_items:
            view = FindPaginator(matching_items)
            await view.send_initial_message(interaction)
        else:
            await interaction.response.send_message(f"Item '{name}' not found.")

async def setup(bot):
    await bot.add_cog(Find(bot))
