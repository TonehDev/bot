import nextcord
from nextcord.ext import commands

class Avatar(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["av"])
  @commands.cooldown(1, 10, commands.cooldowns.BucketType.user)
  async def avatar(self, ctx, *, member : nextcord.Member = None):
    if member == None:
      member = ctx.author
    embed = nextcord.Embed(
      title = f"Avatar for {member}", 
      description = f"{member}'s avatar", 
      color = nextcord.Color.blurple()
    )
    embed.set_image(url = member.avatar.url)
    await ctx.send(embed=embed)

  @avatar.error
  async def avatar_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      embed = nextcord.Embed(
        description = "<:error:956942321633591316> You need to wait ``{:.2f}s`` before re-using ``avatar``".format(error.retry_after),
        color = nextcord.Color.red()
      )
      await ctx.send(embed=embed)
    
    
def setup(client):
  client.add_cog(Avatar(client))
