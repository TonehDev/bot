import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, View

class Start(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_message(self, message):
    support = Button(label="Support Server",
                     url="https://discord.gg/2xzfZtAKMf")
    invite = Button(label="Invite Norium",
                  url="https://discord.com/api/oauth2/authorize?client_id=871454184212410408&scope=applications.commands")

    view = View()
    view.add_item(support)
    view.add_item(invite)

    bot = f'<@!{self.client.user.id}>'
    if message.content == bot:
      embed = nextcord.Embed(
        title = "Norium Bot",
        description = "Norium Bot is a multi-purpose Discord Bot which has many features for everyone to access.\nStart improving your server by typing ``;help``.",
        color = nextcord.Color.blurple()
      )
      await message.channel.send(embed=embed, view=view)
       
    else:
      return

def setup(client):
  client.add_cog(Start(client))
