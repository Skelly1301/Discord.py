# Tutorial 1 - Setting up your Discord Bot
**This tutorial is assuming you have already added your Discord bot to your server, if you haven't, then use this tutorial:** https://docs.discordbotstudio.org/setting-up-dbs/inviting-a-bot-to-your-server

### Pre-Setup

If you don't already have a discord bot, click [here](https://discordapp.com/developers/), accept any prompts then click "New Application" at the top right of the screen.  Enter the name of your bot then click accept.  Click on Bot from the panel from the left, then click "Add Bot."  When the prompt appears, click "Yes, do it!" 

![Left panel](https://i.imgur.com/hECJYWK.png)

Then, click copy under token to get your bot's token. Your bot's icon can also be changed by uploading an image.

![Bot token area](https://i.imgur.com/da0ktMC.png)

### Setup

Go to the https://replit.com and create a project in python.

In the secrets tab on the left, make a new token. Name the token 'TOKEN' and in the key paste your discord bot token.

Now, to start with, copy and paste this into `main.py`:

```python
import os
from keep_alive import keep_alive
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
```

When you hit run everything should startup fine.

This code means that if the user types !ping into the channel the bot will reply with pong!
