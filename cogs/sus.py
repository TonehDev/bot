import nextcord
from nextcord.ext import commands
import random

class Sus(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  @commands.cooldown(1, 10, commands.cooldowns.BucketType.user)
  async def sus(self, ctx, *, member : nextcord.Member = None):
    if member == None:
      member = ctx.author
    embed = nextcord.Embed(
      title = "Sus-O-Meter",
      description = f"{member.mention} is **{random.randint(1, 100)}%** sus!",
      color = nextcord.Color.random()
    )
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/948235933709373470/948605021593940019/images-removebg-preview.png")
    await ctx.send(embed=embed)
    
  @sus.error
  async def sus_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      embed = nextcord.Embed(
        description = "<:error:956942321633591316> You need to wait ``{:.2f}s`` before re-using ``sus``".format(error.retry_after),
        color = nextcord.Color.red()
      )
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Sus(client))
