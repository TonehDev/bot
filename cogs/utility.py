import nextcord 
from nextcord.ext import commands 
from nextcord import Interaction, SlashOption

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client 
    
    guild_ids = 946310802250530846

    @nextcord.slash_command(description = "Returns your profile picture")
    async def avatar(self, interaction : Interaction, member : nextcord.Member = SlashOption(description = "A member you want to view the avatar of", required=False)):
        if member == None:
            member = interaction.user

            embed = nextcord.Embed(
                title = f"Avatar for {member.name}#{member.discriminator}", 
                description = f"{member.name}#{member.discriminator}'s avatar", 
                color = nextcord.Color.blurple()
            )

            embed.set_image(
                url = member.avatar.url
            )

            await interaction.response.send_message(
                embed=embed
            )

    @nextcord.slash_command(description = "Sends an embed containing your message")
    async def embed(self, interaction : Interaction, embed: str = SlashOption(description = "The message you want to be displayed in the embed", required=True)):
        embed = nextcord.Embed(
            description = f"{embed}",
            color = nextcord.Color.random()
        )
        
        await interaction.response.send_message(
            embed=embed
        )

    @nextcord.slash_command(description = "Rename the guild")
    async def grename(self, interaction : Interaction, *, name: str = SlashOption(description = "New guild name", required=True)):
        await interaction.response.send_message(":warning: Moderation commands are temporarily locked due to multiple vulnerabilities found in the code.")

    @nextcord.slash_command(description = "Locks a channel")
    async def lock(self, interaction : Interaction, *, reason="No reason provided."):
        await interaction.response.send_message(":warning: Moderation commands are temporarily locked due to multiple vulnerabilities found in the code.")

    @nextcord.slash_command(description = "Locks a channel")
    async def unlock(self, interaction : Interaction, *, reason="No reason provided."):
        await interaction.response.send_message(":warning: Moderation commands are temporarily locked due to multiple vulnerabilities found in the code.")

    @nextcord.slash_command(description = "Send a voting message")
    async def poll(self, interaction : Interaction, choice1, choice2, topic, *, note = SlashOption(description = "A note you'd like to leave", required=False)):

        embed = nextcord.Embed(
            title = topic,
            description = f":one: {choice1}\n:two: {choice2}",
            color = nextcord.Color.random()
        )

        embed.add_field(
            name = "Notes",
            value = f"{note}"
        )

        embed.set_footer(text = f"Asked by {interaction.user.name}#{interaction.user.discriminator}")

        await interaction.response.send_message(
            embed=embed
        )

        msg = await interaction.original_message()

        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")

    @nextcord.slash_command(description = "Sends your or another user's user profile")
    async def profile(self, interaction : Interaction, member : nextcord.Member = SlashOption(description = "The member you want to view the profile of", required=False)):
        if member == None:
            member = interaction.user 

        roles = [role for role in member.roles]

        embed = nextcord.Embed(
            title = f"{member.name}#{member.discriminator}'s Profile",
            color = member.color
        )

        embed.set_thumbnail(
            url = member.avatar.url
        )

        embed.add_field(
            name = "ID", 
            value = member.id
        )

        embed.add_field(
            name = "Nickname", 
            value = member.display_name
        )

        embed.add_field(
            name = "Created at", 
            value = member.created_at.strftime("%a, %#d, %B %Y, %I:%M %p UTC")
        )

        embed.add_field(
            name = "Joined at", 
            value = member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
        )

        embed.add_field(
            name = f"Roles ({len(roles)})", 
            value = " ".join([role.mention for role in roles])
        )

        embed.add_field(
            name = "Top Role", 
            value = member.top_role.mention
        )

        embed.add_field(
            name = "Is Bot", 
            value = member.bot
        )

        embed.add_field(
            name = "Avatar URL", 
            value = f"[Click Here]({member.avatar.url})"
        )

        await interaction.response.send_message(
            embed=embed
        )

    @nextcord.slash_command(description = "Sends some information about the current server")
    async def serverinfo(self, interaction : Interaction):
        role_count = len(interaction.guild.roles)
        bots = [bot.mention for bot in interaction.guild.members if bot.bot]

        embed = nextcord.Embed(
            title = f"Server Information for **{interaction.guild.name}**", 
            color = nextcord.Color.blurple()
        )

        embed.add_field(
            name = "Guild Name",
            value = f"``{interaction.guild.name}``"
        )

        embed.add_field(
            name = "Members", 
            value = f"``{interaction.guild.member_count}``"
        )

        embed.add_field(
            name = "Verification Level", 
            value = f"``{str(interaction.guild.verification_level)}``"
        )

        embed.add_field(
            name = "Highest Role", 
            value = f"``{interaction.guild.roles[-2]}``"
        )

        embed.add_field(
            name = "Role Count", 
            value = f"``{str(role_count)}``"
        )

        embed.add_field(
            name = "Bots", 
            value = ', '.join(bots)
        )

        await interaction.response.send_message(
            embed=embed
        )

    @nextcord.slash_command(description = "Sets the slowmode")
    async def slowmode(self, interaction : Interaction, arg : int = SlashOption(description = "Slowmode seconds", required=True)):
        await interaction.response.send_message(":warning: Moderation commands are temporarily locked due to multiple vulnerabilities found in the code.")


def setup(client):
    client.add_cog(Utility(client))