import nextcord
from nextcord.ext import commands

class Bunger(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def bunger(self, ctx):
    embed = nextcord.Embed(
      title = "Bunger :hamburger:", 
      description = "Bunger :hamburger:", 
      color = nextcord.Color.gold()
    )
    embed.set_image(
      url = "https://cdn.discordapp.com/attachments/853196607548555285/875999967838343198/tenor.gif"
    )
    await ctx.send(embed=embed)

  @commands.command()
  async def egg(self, ctx):
    embed = nextcord.Embed(
      title = "Oh the misery...", 
      description = "Egg cat :egg:", 
      color = nextcord.Color.light_grey()
    )
    embed.set_image(
      url = "https://media.discordapp.net/attachments/936115643835629639/964603292132982784/oh-the-misery-eggcat.gif?width=380&height=547"
    )
    await ctx.send(embed=embed)
    
def setup(client):
  client.add_cog(Bunger(client))
