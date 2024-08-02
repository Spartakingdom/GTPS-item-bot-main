# commands/update.py

import discord
from discord import app_commands
from discord.ext import commands
from utils.updater import check_for_updates
from config import ITEMS_URL, DEVELOPER_ID

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="check_update", description="Manually check for items.php update")
    async def check_update(self, interaction: discord.Interaction):
        if str(interaction.user.id) != DEVELOPER_ID:
            await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
            return

        await interaction.response.defer(ephemeral=True)  # Defer the response to give more time

        updated = await check_for_updates('items.php', ITEMS_URL)
        if updated:
            await self.bot.reload_extension('commands.find')
            await self.bot.reload_extension('commands.list')
            await interaction.followup.send("Items.php has been updated and extensions reloaded.", ephemeral=True)
        else:
            await interaction.followup.send("No update found for items.php.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Update(bot))
