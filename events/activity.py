@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord, lol')
    activity = discord.Activity(type=discord.ActivityType.watching,
                                name=str(len(bot.guilds)) + " servers! " +
                                " | b!help ")
    await bot.change_presence(status=discord.Status.online, activity=activity)
