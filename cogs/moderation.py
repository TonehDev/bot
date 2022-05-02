import nextcord 
from nextcord.ext import commands 
from nextcord import SlashOption, Interaction 
import datetime
import humanfriendly

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client 

    guild_ids = 946310802250530846

    @nextcord.slash_command(description = "Clears a specific amount of messages")
    async def clear(self, interaction : Interaction, amount : int = SlashOption(description = "Amount of messages to clear", required=True)):
        await interaction.response.send_message(":warning: Moderation commands are temporarily locked due to multiple vulnerabilities found in the code.")

    @nextcord.slash_command(description = "Change a member's nickname manually")
    async def setnick(self, interaction : Interaction, member : nextcord.Member = SlashOption(description = "The member you'd like to change the nickname of", required=True), *, nick = SlashOption(description="New nick", required=True)):
        await interaction.response.send_message(":warning: Moderation commands are temporarily locked due to multiple vulnerabilities found in the code.")

    @nextcord.slash_command(description = "Changes a member's nickname")
    async def moderate(self, interaction : Interaction, member : nextcord.Member = SlashOption(description = "The member you'd like to moderate the nickname of", required=True)):
        await interaction.response.send_message(":warning: Moderation commands are temporarily locked due to multiple vulnerabilities found in the code.")

    @nextcord.slash_command(description = "Warns a member")
    async def warn(self, interaction : Interaction, member: nextcord.Member, *, reason="No reason provided."):
        await interaction.response.send_message(":warning: Moderation commands are temporarily locked due to multiple vulnerabilities found in the code.")
        
    @nextcord.slash_command(description = "Bans a member")
    async def ban(self, interaction : Interaction, member : nextcord.Member = SlashOption(description = "The member you'd like to ban", required=True), *, reason = SlashOption(description = "Reason for banning that member", required=False)):
        await interaction.response.send_message(":warning: Moderation commands are temporarily locked due to multiple vulnerabilities found in the code.")
        
    @nextcord.slash_command(description = "Kicks a member")
    async def kick(self, interaction : Interaction, member : nextcord.Member = SlashOption(description = "The member you'd like to kick", required=True), *, reason = SlashOption(description = "Reason for kicking that member", required=False)):
        await interaction.response.send_message(":warning: Moderation commands are temporarily locked due to multiple vulnerabilities found in the code.")
        
    @nextcord.slash_command(description = "Mutes a member")
    async def mute(self, interaction : Interaction, time = SlashOption(description = "Duration of the timeout", required=True), member : nextcord.Member = SlashOption(description = "The member you'd like to mute", required=True), *, reason = SlashOption(description = "Reason for muting that member", required=False)):
        await interaction.response.send_message(":warning: Moderation commands are temporarily locked due to multiple vulnerabilities found in the code.")
        
    @nextcord.slash_command(description = "Unmutes a member")
    async def unmute(self, interaction : Interaction, member : nextcord.Member = SlashOption(description = "The member you'd like to unmute", required=True), *, reason = SlashOption(description = "Reason for unmuting that member", required=False)):
        await interaction.response.send_message(":warning: Moderation commands are temporarily locked due to multiple vulnerabilities found in the code.")
        

def setup(client):
    client.add_cog(Moderation(client))
