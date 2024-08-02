# utils/paginator.py

import discord

class Paginator(discord.ui.View):
    def __init__(self, items, per_page=10, title="Item List", color=discord.Color.blue()):
        super().__init__()
        self.items = items
        self.per_page = per_page
        self.current_page = 0
        self.title = title
        self.color = color

    async def send_initial_message(self, interaction: discord.Interaction):
        embed = self.get_embed()
        await interaction.response.send_message(embed=embed, view=self)

    def get_embed(self):
        embed = discord.Embed(title=self.title, color=self.color)
        start = self.current_page * self.per_page
        end = start + self.per_page
        for item_id, item_name in self.items[start:end]:
            embed.add_field(name=f"Item ID: {item_id}", value=f"Name: {item_name}", inline=False)
        embed.set_footer(text=f"Page {self.current_page + 1} of {len(self.items) // self.per_page + 1}")
        return embed

    @discord.ui.button(label='Previous', style=discord.ButtonStyle.primary)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_page > 0:
            self.current_page -= 1
            embed = self.get_embed()
            await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label='Next', style=discord.ButtonStyle.primary)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        if (self.current_page + 1) * self.per_page < len(self.items):
            self.current_page += 1
            embed = self.get_embed()
            await interaction.response.edit_message(embed=embed, view=self)
