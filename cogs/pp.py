import nextcord
from nextcord.ext import commands
import random

class ppRate(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.cooldown(1, 10, commands.cooldowns.BucketType.user)
  async def pp(self, ctx, *, member : nextcord.Member = None):
    if member == None:
      member = ctx.author
    pp = [
      "8D",
      "8=D",
      "8==D",
      "8===D",
      "8====D",
      "8=====D",
      "8======D",
      "8=======D",
      "8========D",
      "8=========D",
      "8==========D",
      "8===========D",
      "8============D",
      "8=============D",
      "8==============D",
      "8===============D",
      "8================D",
      "8=================D",
      "8==================D",
      "8===================D",
      "8====================D",
      "8=====================D",
      "8======================D",
      "8=======================D",
      "8========================D",
      "8=========================D",
      "8==========================D"
    ]
    embed = nextcord.Embed(
      title = f"PP-O-Meter",
      description = f"{member.mention}'s PP Size\n{random.choice(pp)}",
      color = nextcord.Color.random()
    )
    await ctx.send(embed=embed)

  @pp.error
  async def pp_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      embed = nextcord.Embed(
        description = "<:error:956942321633591316> You need to wait ``{:.2f}s`` before re-using ``pp``".format(error.retry_after),
        color = nextcord.Color.red()
      )
      await ctx.send(embed=embed)
  

def setup(client):
  client.add_cog(ppRate(client))
