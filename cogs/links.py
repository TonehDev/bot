import nextcord
from nextcord.ext import commands

class Links(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def links(self, ctx):
    embed = nextcord.Embed(
      title = "Links",
      description = f"[Support Server](https://discord.gg/2xzfZtAKMf)\n[Top.gg Page](https://top.gg/bot/871454184212410408)\n[Vote](https://top.gg/bot/871454184212410408/vote)\n[Invite](https://discord.com/api/oauth2/authorize?client_id=871454184212410408&scope=applications.commands)\n[Website](https://noriumbot.com/)",
      color = nextcord.Color.blurple()
    )
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Links(client))
