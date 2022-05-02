import nextcord
from nextcord.ext import commands

class Version(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["v"])
  async def version(self, ctx):
    self.version = "v1.3"
    embed = nextcord.Embed(
      title = "Version",
      description = f"Norium Bot is currently on version **{self.version}**",
      color = nextcord.Color.blurple()
    )
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Version(client))
