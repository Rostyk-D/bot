import discord
import asyncio
import random
from discord.ext import commands

YOUTUBE_KEY: str = "AIzaSyCgH_5zldxDE37EAAdVaLE-DbAe7Aey8R0"
BOT_TOKEN: str = "MTE5MDc0NjY2ODkzMzU5MTI0MQ.G_-mRO.2zyyS4cQo-1y4S8n2AsP8IaMQjCiJDVBDjRF2s"
SPOTIFY_ID: str = "ae13ba4a7a0544bba890e98392526b80"
SPOTIFY_SECRET: str = "d1238f0790694e1987ad3206f17fdd67"

BOT_PREFIX = "."
INTENTS = discord.Intents.all()
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=INTENTS)

