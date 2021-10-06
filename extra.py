import discord
from discord import commands

class extra_cog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    msg = message.content

    if msg.startswith("shodoltong"):
      await message.channel.send("Tui shodoltong, tor nani shodoltong, tor 14 gushti shodoltong!!")

def setup(client):
  client.add_cog(extra_cog(client))
