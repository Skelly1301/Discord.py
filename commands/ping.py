import os
from discord.ext import commands
import discord

@bot.command()
async def ping(ctx):
    await ctx.reply("pong!")
