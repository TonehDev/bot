import nextcord  
from nextcord.ext import commands
from nextcord.ui import Button, View

class Invite(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command(aliases=["inv"])
    @commands.cooldown(1, 10, commands.cooldowns.BucketType.user)
    async def invite(self, ctx):
        support = Button(label="Support Server",
                     url="https://discord.gg/2xzfZtAKMf")
        invite = Button(label="Invite Norium",
                  url="https://dsc.gg/noriumv3")

        view = View()
        view.add_item(support)
        view.add_item(invite)

        embed = nextcord.Embed(
            title = "Invite Norium Bot",
            description = "Invite Norium\n[Click here](https://discord.com/api/oauth2/authorize?client_id=871454184212410408&scope=applications.commands)\n\n",
            color = nextcord.Color.blurple()
        )
        await ctx.send(embed=embed, view=view)
        
    @invite.error
    async def invite_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = nextcord.Embed(
                description = "<:error:956942321633591316> You need to wait ``{:.2f}s`` before re-using ``invite``".format(error.retry_after),
                color = nextcord.Color.red()
            )
            await ctx.send(embed=embed)
   


def setup(client):
    client.add_cog(Invite(client))
