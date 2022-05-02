import nextcord
from nextcord.ext import commands 

class Discriminator(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["discriminator"])
  async def tag(self, ctx, member : nextcord.Member = None):
    if member == None:
      member = ctx.author
    
    embed = nextcord.Embed(
      description = f"{member.mention}'s discriminator is currently **#{member.discriminator}**",
      color = nextcord.Color.red()
    )
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Discriminator(client))