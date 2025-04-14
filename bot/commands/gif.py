from discord import app_commands, Interaction, Object
from bot.utils.giphy import get_gif
import os

SERVER_ID = int(os.getenv("SERVER_ID"))

def register(tree: app_commands.CommandTree):
    @tree.command(guild=Object(id=SERVER_ID), name='fail', description="Send a funny 'fail' GIF")
    async def fail(interaction: Interaction):
        gif_url = await get_gif("fail")
        await interaction.response.send_message(gif_url or "Couldn't find a GIF.")

    @tree.command(guild=Object(id=SERVER_ID), name='cat', description="Send a funny 'cat' GIF")
    async def cat(interaction: Interaction):
        gif_url = await get_gif("cat")
        await interaction.response.send_message(gif_url or "Couldn't find a GIF.")

