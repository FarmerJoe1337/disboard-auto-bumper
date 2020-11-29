import time
import discord
from discord.ext import commands

client = commands.Bot(".", self_bot = True)

TOKEN = 'your tokens here'

@client.command()
async def start(ctx):
    await ctx.message.delete()
    while 1:
        try:
            await ctx.send('!d bump')
            await time.sleep(7220)
        except:
            break
            
client.run(TOKEN, bot = False)
