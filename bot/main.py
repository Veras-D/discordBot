import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

from bot import events
from bot.commands import gif, roll, temp_channels

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
SERVER_ID = int(os.getenv("SERVER_ID"))

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=SERVER_ID))
    print(f"Bot connected as {bot.user}")

# Register event handlers
events.register(bot)

# Register commands
gif.register(tree)
roll.register(tree)
temp_channels.register(tree)

bot.run(TOKEN)

