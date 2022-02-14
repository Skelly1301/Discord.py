import os
from discord.ext import commands
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
client = discord.Client()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all()) #You can change the prefix to your desired one here

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord')
    await bot.change_presence(status=discord.Status.online)
    
@bot.command()
async def ping(ctx):
    await ctx.send("pong!")
