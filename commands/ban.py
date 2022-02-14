import os
from discord.ext import commands
import discord

@bot.command(brief="Bans a server member",
             description="b!ban <member> [reason]")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.reply(f'User {member} has been banned.')
    except:
        await ctx.reply(
            "The bot has missing permissions\n\nMake sure the Bot's top-most role is above the member's top-most role (the member who you are going to ban)"
        )
