import discord
import random
from discord import app_commands, Interaction, Object
import os

SERVER_ID = int(os.getenv("SERVER_ID"))

class DiceRollerView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180.0)

    async def roll_dice(self, interaction: discord.Interaction, dice_type: str):
        dice_max = int(dice_type[1:])
        result = random.randint(1, dice_max)

        embed = discord.Embed(
            title=f"🎲 {interaction.user.global_name} rolled a {dice_type}!",
            description=f"**Result**: `{result}`",
            color=discord.Color.purple()
        )
        embed.set_footer(text="Good luck on your next roll!")
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(label="Roll D20", style=discord.ButtonStyle.green)
    async def roll_d20(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.roll_dice(interaction, "D20")

    @discord.ui.button(label="Roll D10", style=discord.ButtonStyle.blurple)
    async def roll_d10(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.roll_dice(interaction, "D10")

    @discord.ui.button(label="Roll D8", style=discord.ButtonStyle.primary)
    async def roll_d8(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.roll_dice(interaction, "D8")

    @discord.ui.button(label="Roll D6", style=discord.ButtonStyle.secondary)
    async def roll_d6(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.roll_dice(interaction, "D6")


def register(tree: app_commands.CommandTree):
    @tree.command(guild=Object(id=SERVER_ID), name="roll", description="Roll a dice with buttons")
    async def roll(interaction: Interaction):
        await interaction.response.send_message("Choose a dice to roll:", view=DiceRollerView())

