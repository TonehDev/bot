import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, View

class Vote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 10, commands.cooldowns.BucketType.user)
    async def vote(self, ctx):
        vote = Button(label = "Vote for Norium Bot", url = "https://top.gg/bot/871454184212410408/vote")

        view = View()
        view.add_item(vote)

        embed = nextcord.Embed(
            title = "Vote for Norium Bot",
            description = "Vote for us on Top.gg\n[Vote for Norium Bot here](https://top.gg/bot/871454184212410408/vote)\n\n",
            color = nextcord.Color.blurple()
        )
        await ctx.send(embed=embed, view=view)
        
    @vote.error
    async def vote_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = nextcord.Embed(
                description = "<:error:956942321633591316> You need to wait ``{:.2f}s`` before re-using ``vote``".format(error.retry_after),
                color = nextcord.Color.red()
            )
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Vote(client))
