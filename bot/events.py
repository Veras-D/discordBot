import discord
import os

SERVER_ID = int(os.getenv("SERVER_ID"))

def register(bot):
    @bot.event
    async def on_ready():
        await bot.tree.sync(guild=discord.Object(id=SERVER_ID))
        print(f"✅ Bot is online as {bot.user} and synced with server {SERVER_ID}")

    @bot.event
    async def on_member_join(member):
        # Change these names as needed for your server
        welcome_channel = discord.utils.get(member.guild.text_channels, name="general")
        rules_channel = discord.utils.get(member.guild.text_channels, name="RULES")

        if not welcome_channel:
            print("⚠️ Welcome channel 'general' not found.")
            return

        embed = discord.Embed(
            title="🎉 Welcome to the Server!",
            description=(
                f"Hey {member.mention}, welcome to **WastedServices**!\n"
                f"Don't forget to read the rules here: {rules_channel.mention if rules_channel else '#RULES'}"
            ),
            color=0x00ff00,
        )

        await welcome_channel.send(embed=embed)

