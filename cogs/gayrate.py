import nextcord
from nextcord.ext import commands
import random

class GayRate(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  @commands.cooldown(1, 10, commands.cooldowns.BucketType.user)
  async def gayrate(self, ctx, *, member : nextcord.Member = None):
    if member == None:
      member = ctx.author
    embed = nextcord.Embed(
      title = f"Gay Rate",
      description = f"{member.mention} is **{random.randint(1, 100)}%** gay!",
      color = nextcord.Color.random()
    )
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/948235933709373470/948606707926462484/images.png")
    await ctx.send(embed=embed)
    
  @gayrate.error
  async def gayrate_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      embed = nextcord.Embed(
        description = "<:error:956942321633591316> You need to wait ``{:.2f}s`` before re-using ``gayrate``".format(error.retry_after),
        color = nextcord.Color.red()
      )
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(GayRate(client))
