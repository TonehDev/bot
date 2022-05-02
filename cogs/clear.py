import nextcord
from nextcord.ext import commands

class Clear(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["purge"])
  @commands.cooldown(1, 10, commands.cooldowns.BucketType.user)
  @commands.has_permissions(manage_messages = True)
  async def clear(self, ctx, amount=2):
    await ctx.message.delete()
    await ctx.channel.purge(limit = amount)

  # Error Handling

  @clear.error
  async def clear_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(
          title = "Invalid Syntax",
          description = "``<> Required, [] Optional``",
          color = nextcord.Color.red()
      )
      embed.add_field(name = "Usage", value = "``-clear <msg_amount>``", inline = False)
      embed.add_field(name = "Example", value = "``-clear 5``", inline = False)
      await ctx.send(embed=embed) #credit: lucas
    
    elif isinstance(error, commands.CommandOnCooldown):
      embed = nextcord.Embed(
        description = "<:error:956942321633591316> You need to wait ``{:.2f}s`` before re-using ``clear``".format(error.retry_after),
        color = nextcord.Color.red()
      )
      await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Clear(client))
