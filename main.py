import os
import discord
import music
#import extra
from discord.ext import commands

cogs = [music]

client = commands.Bot(command_prefix='$', intents= discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

@client.event
async def on_ready():
  print('{0.user} logged in.'.format(client))

client.run(os.environ['env'])
