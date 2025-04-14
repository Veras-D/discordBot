import asyncio
from discord import app_commands, Interaction, Object
import discord
import os

SERVER_ID = int(os.getenv("SERVER_ID"))

def register(tree: app_commands.CommandTree):
    @tree.command(guild=Object(id=SERVER_ID), name='create_temp_voice_channel', description="Creates a temporary voice channel")
    async def create_temp_channel(interaction: Interaction, channel_name: str = "Temporary Channel"):
        if interaction.user != interaction.guild.owner:
            await interaction.response.send_message("Only the server owner can use this command.", ephemeral=True)
            return

        temp_channel = await interaction.guild.create_voice_channel(name=channel_name)
        await interaction.response.send_message(f"Voice channel '{channel_name}' created! Will be deleted in 10 minutes if empty.", ephemeral=True)

        await asyncio.sleep(600)

        if temp_channel and len(temp_channel.members) == 0:
            await temp_channel.delete()
            await interaction.followup.send(f"The voice channel '{channel_name}' has been deleted.", ephemeral=True)

    @tree.command(guild=Object(id=SERVER_ID), name='create_temp_text_channel', description="Creates a temporary text channel")
    async def create_temp_text_channel(interaction: Interaction, channel_name: str = "Temporary Text Channel"):
        if interaction.user != interaction.guild.owner:
            await interaction.response.send_message("Only the server owner can use this command.", ephemeral=True)
            return

        temp_channel = await interaction.guild.create_text_channel(name=channel_name)
        await interaction.response.send_message(f"Text channel '{channel_name}' created! Will be deleted in 10 minutes if no one speaks.", ephemeral=True)

        def check_message_in_channel(message):
            return message.channel == temp_channel

        try:
            await interaction.client.wait_for("message", check=check_message_in_channel, timeout=600)
        except asyncio.TimeoutError:
            if temp_channel:
                await temp_channel.delete()
                await interaction.followup.send(f"The text channel '{channel_name}' was deleted due to inactivity.", ephemeral=True)

