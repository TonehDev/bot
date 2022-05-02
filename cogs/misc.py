import nextcord 
from nextcord.ext import commands 
from nextcord import Interaction, SlashOption 
from nextcord.ui import Button, View
import random
from norium.api import latency

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client 

    guild_ids = 946310802250530846

    @nextcord.slash_command(description = "Sends your discriminator")
    async def tag(self, interaction : Interaction, member : nextcord.Member = SlashOption(description = "The member you want to view the tag of", required=False)):
      if member == None:
        member = interaction.user

      embed = nextcord.Embed(
        description = f"{member.mention}'s current discriminator is **#{member.discriminator}**",
        color = nextcord.Color.red()
      )
      await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(description = "Sends some information about Norium")
    async def about(self, interaction : Interaction):
        embed = nextcord.Embed(
            title = "About Norium Bot",
            description = "Norium Bot is a multi-purpose Discord Bot focusing on giving the user the best possible experience.",
            color = nextcord.Color.blurple()
        )

        embed.set_image(
            url = "https://cdn.discordapp.com/attachments/950784001478623263/956578139599941742/unknown.png"
        )

        await interaction.response.send_message(
            embed=embed
        )

    @nextcord.slash_command(description = "Shows the current bot & API latency")
    async def ping(self, interaction : Interaction):
      embed = nextcord.Embed(
        title = "Pong! :ping_pong:",
        description = "**[Norium Status](https://noriumbot.com/status)**",
        color = nextcord.Color.blurple()
      )
      embed.add_field(name = "Client", value = f"{round(self.client.latency * 1000)} ms", inline = False)
      embed.add_field(name = "API", value=f"{norium.api_ping(round(self.api.latency * 1000))} ms", inline = False)

      await interaction.response.send_message(
            embed=embed
      )

    @nextcord.slash_command(description = "Shows the amount of commands Norium has to offer")
    async def commands(self, interaction : Interaction):
        embed = nextcord.Embed(
            title = "Current Command Count",
            color = nextcord.Color.blurple()
        )
        
        embed.add_field(
            name = "Total",
            value = "44 commands"
        )

        await interaction.response.send_message(
            embed=embed
        )

    @nextcord.slash_command(description = "Shows the amount of servers Norium is in")
    async def servers(self, interaction : Interaction):
        embed = nextcord.Embed(
            title = "Servers",
            description = f"Norium is in **{len(self.client.guilds)}** servers!",
            color = nextcord.Color.blurple()
        )

        await interaction.response.send_message(
            embed=embed
        )

    @nextcord.slash_command(description = "Sends the invite link for Norium Bot")
    async def invite(self, interaction : Interaction):
        support = Button(
            label = "Support Server",
            url = "https://discord.gg/2xzfZtAKMf"
        )

        invite = Button(
            label = "Invite Norium",
            url = "https://discord.com/api/oauth2/authorize?client_id=871454184212410408&scope=applications.commands"
        )

        view = View()
        view.add_item(support)
        view.add_item(invite)

        embed = nextcord.Embed(
            title = "Invite",
            description = "Invite Norium\n[Click here](https://discord.com/api/oauth2/authorize?client_id=871454184212410408&scope=applications.commands)",
            color = nextcord.Color.blurple()
        )

        await interaction.response.send_message(
            embed=embed,
            view=view
        )

    @nextcord.slash_command(description = "Sends all Norium-related links")
    async def links(self, interaction : Interaction):
        embed = nextcord.Embed(
            title = "All Norium-related links",
            description = "[Support Server](https://discord.gg/2xzfZtAKMf)\n[Top.gg Page](https://top.gg/bot/871454184212410408)\n[Vote](https://top.gg/bot/871454184212410408/vote)\n[Invite](https://discord.com/api/oauth2/authorize?client_id=871454184212410408&scope=applications.commands)\n[Website](https://noriumbot.com/)",
            color = nextcord.Color.blurple()
        )

        await interaction.response.send_message(
            embed=embed
        )

    @nextcord.slash_command(description = "Lookup a minecraft user")
    async def minecraft(self, interaction : Interaction, *, player = SlashOption(description="Minecraft player you want to look up", required=True)):
        url = "https://tr.namemc.com/profile/{}".format(player)

        embed = nextcord.Embed(
            title = f"Minecraft Profile for {player}",
            description = f"[NameMC Profile]({url})",
            color = nextcord.Color.gold()
        )

        embed.add_field(
            name = "Skull Command (1.13+)",
            value = '``/give @p minecraft:player_head{p1}SkullOwner:"{name}"{p2}'.format(p1="{",name=player,p2="}``"),
            inline = False
        )

        embed.add_field(
            name = "Skull Command (1.13-)",
            value = '``/give @p minecraft:skull 1 3 {p1}SkullOwner:"{name}"{p2}'.format(p1="{",name=player,p2="}``"),
            inline = False
        )

        await interaction.response.send_message(
            embed=embed
        )

    @nextcord.slash_command(description = "Displays the current bot version")
    async def version(self, interaction : Interaction):
        self.version = "v1.2"

        embed = nextcord.Embed(
            title = "Version",
            description = f"Norium Bot is currently on version **{self.version}**",
            color = nextcord.Color.blurple()
        )

        await interaction.response.send_message(
            embed=embed
        )

    @nextcord.slash_command(description = "Sends the vote link for Norium Bot")
    async def vote(self, interaction : Interaction):
        vote = Button(
            label = "Vote for Norium Bot", 
            url = "https://top.gg/bot/871454184212410408/vote"
        )

        view = View()

        view.add_item(
            vote
        )

        embed = nextcord.Embed(
            title = "Vote for Norium Bot",
            description = "Vote for us on Top.gg\n[Vote for Norium Bot here](https://top.gg/bot/871454184212410408/vote)\n\n",
            color = nextcord.Color.blurple()
        )

        await interaction.response.send_message(
            embed=embed, 
            view=view
        )

def setup(client):
    client.add_cog(Misc(client))
