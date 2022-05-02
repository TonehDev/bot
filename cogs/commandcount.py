import nextcord
from nextcord.ext import commands

class CommandCount(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["count", "commands", "cmd"])
  async def commandcount(self, ctx):
    embed = nextcord.Embed(
      title = "Command Count",
      color = nextcord.Color.blurple()
    )
    embed.add_field(name = "Total Commands", value = "55", inline = False)
    embed.add_field(name = "Excluding Help Commands", value = "49", inline = False)
    embed.add_field(name = "Excluding This Command and Help Commands", value = "48", inline = False)
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(CommandCount(client))