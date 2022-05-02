import nextcord
from nextcord.ext import commands
import os
from nextcord.ui import Button, View
import urllib
import json
from psutil import Process, virtual_memory
import datetime
from datetime import timedelta
import time
import asyncio
import random
from nextcord import Interaction, SlashOption
from config import *
import keep_alive

intents = nextcord.Intents().all()
intents.members = True
client = commands.Bot(command_prefix=BOT_PREFIX, case_insensitive = True, intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    global startTime
    startTime = time.time()
    await client.change_presence(activity = nextcord.Game(name = f"{len(client.guilds)} servers | /help"))
    print("Ready.")
    

@client.slash_command(description = "Sends CPU, Memory Usage")
async def stats(interaction : Interaction):
    await interaction.response.send_message(":warning: **This command has been globally disabled for a short amount of time.**\nConfused on this decision? [Check out our newest article explaining this issue and why it needs to be fixed immediately](https://noriumbot.com/articles/newest-05_01_22)")

@client.command()
async def stats(ctx):
    website = Button(label="Article", url="https://noriumbot.com/articles/newest-05_01_22")

    view = View()
    view.add_item(website)
    await ctx.send(":warning: **This command has been globally disabled for a short amount of time.**\nConfused on this decision? Click the button below.", view=view)
    

@client.group(invoke_without_command=True)
@commands.is_owner()
async def setstatus(ctx, *, statusArg):
    embed = nextcord.Embed(
        title = "Options",
        description = "``playing, watching, listening, streaming``",
        color = nextcord.Color.red()
    )
    await ctx.send(embed=embed)

@setstatus.command()
@commands.is_owner()
async def playing(ctx, *, statusArg):
    embed = nextcord.Embed(
        title = f"Playing ``{statusArg}``",
        description = f"Status has been changed for Norium.\n\n**Playing** {statusArg}",
        color = nextcord.Color.red()
    )
    await ctx.send(embed=embed)

    await client.change_presence(activity=nextcord.Game(name = f"{statusArg}"))

@setstatus.error 
async def setstatus_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        embed = nextcord.Embed(
            title = "Owner only",
            description = "You're not the owner of this Bot!",
            color = nextcord.Color.red()
        )
        await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    embed = nextcord.Embed(description=f"Loaded ``{extension}.py``",
                           color=nextcord.Color.blurple())
    await ctx.send(embed=embed)


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    embed = nextcord.Embed(description=f"Unloaded ``{extension}.py``",
                           color=nextcord.Color.blurple())
    await ctx.send(embed=embed)


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    embed = nextcord.Embed(description=f"Reloaded ``{extension}.py``",
                           color=nextcord.Color.blurple())
    await ctx.send(embed=embed)

@load.error 
async def load_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        embed = nextcord.Embed(
            title = "Owner only",
            description = "Only the owner of this bot can perform this command!",
            color = nextcord.Color.red()
        )
        await ctx.send(embed=embed)

@unload.error 
async def unload_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        embed = nextcord.Embed(
            title = "Owner only",
            description = "Only the owner of this bot can perform this command!",
            color = nextcord.Color.red()
        )
        await ctx.send(embed=embed)

@reload.error 
async def reload_error(ctx, error):
    if isinstance(error, commands.Guil):
        embed = nextcord.Embed(
            title = "Owner only",
            description = "Only the owner of this bot can perform this command!",
            color = nextcord.Color.red()
        )
        await ctx.send(embed=embed)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# help command
    
class HelpDrop(nextcord.ui.Select):
    def __init__(self):
        selectOptions = [
            nextcord.SelectOption(label = "Moderation", description = "Displays all moderation features", emoji = "🛠️"),
            nextcord.SelectOption(label = "Fun", description = "Displays all fun features", emoji = "🎮"),
            nextcord.SelectOption(label = "Misc", description = "Displays all miscellaneous features", emoji = "✨"),
            nextcord.SelectOption(label = "Utility", description = "Displays all utility features", emoji = "🔨"),
            nextcord.SelectOption(label = "Marriage", description = "Displays all marriage features", emoji = "💍")
        ]
        super().__init__(placeholder='Select a category', min_values=1, max_values=1, options=selectOptions)

    async def callback(self, interaction : Interaction):
        if self.values[0] == 'Moderation':
          embed = nextcord.Embed(title="<:bars:956962805788082206> Moderation Plugin",
                                 description="``<> Required``\n``[] Optional``",
                                 color=nextcord.Color.blurple())
          embed.add_field(name="``/warn @<member> [reason]``", value="Warn a member")
          embed.add_field(name="``/mute @<member> [reason]``", value="Mute a member")
          embed.add_field(name="``/lock <reason>``",
                          value="Lock the current channel in which you are in")
          embed.add_field(name="``/ban @<member> [reason]``",
                          value="Ban a member from your server")
          embed.add_field(name="``/kick @<member> [reason]``",
                          value="Kick a member from your server")
          embed.add_field(
              name="``/unmute @<member>``",
              value="Unmute a member that was timed out",
                )
          embed.add_field(name="``/clear <msg_amount>``",
                          value="Clear several messages at once")
          embed.add_field(name="``/unlock``", value="Unlock a channel")
          embed.add_field(name="``/moderate @<member>``",
                          value="Moderate a member's nickname")
          embed.add_field(name="``/setnick @<member>``", value="Set a member's nick")
          await interaction.edit(embed=embed)


        if self.values[0] == 'Utility':
            embed = nextcord.Embed(title="<:bars:956962805788082206> Utility Plugin",
                           color=nextcord.Color.blurple())
            embed.add_field(name="``/poll <option_1> <option_2> <topic> (note)``",
                    value="Send a voting message")
            embed.add_field(name="``/servers``",
                    value="Shows the amount of servers Norium Bot is in")
            embed.add_field(name="``/embed <text>``",
                    value="Send a custom embed message")
            embed.add_field(name="``/profile @[member]``",
                    value="Your's or another user's profile")
            embed.add_field(name="``/avatar @[member]``",
                    value="Displays your avatar or another member's avatar")
            embed.add_field(name="``/commands``", value="Overall command count")
            embed.add_field(
                name="``/stats``",
                value="Displays Norium Bot's CPU, Memory Usage etc.")
            embed.add_field(
                name="``/grename``",
                value="Rename your server")
            embed.add_field(
                name="``/slowmode``",
                value="Set the slowmode for a specific channel")
            await interaction.edit(embed=embed)

        if self.values[0] == 'Fun':
                embed = nextcord.Embed(title="<:bars:956962805788082206> Fun Plugin",
                           description="``<> Required``\n``[] Optional``",
                           color=nextcord.Color.blurple())
                embed.add_field(name="``/bunger``", value="Bunger :hamburger:")
                embed.add_field(name="``/ask <question>``",
                    value="Ask the almighty 8ball a question")
                embed.add_field(name="``/sus @[member]``", value="Sus-O-Meter :flushed:")
                embed.add_field(name="``/pp @[member]``", value="PP-O-Meter")
                embed.add_field(name="``/gayrate @[member]``",
                    value="See how gay you are or another member is")
                embed.add_field(name="``/kill @<member>``", value="Make someone unalive")
                embed.add_field(name="``/cat``", value="Sends random cat images")
                embed.add_field(
                  name="``/simprate``",
                  value="See how much of a simp you are or another member is")
                embed.add_field(name="``/coinflip``", value="Flip a coin")
                embed.add_field(name="``/minecraft``",
                    value="Get a minecraft player's profile")
                embed.add_field(name="``/meme``", value="Sends a random meme")
                embed.add_field(name="``/eggcat``", value="Egg cat")
                await interaction.edit(embed=embed)

        if self.values[0] == 'Misc':
          embed = nextcord.Embed(title="<:bars:956962805788082206> Misc Plugin",
                                 description="``<> Required``\n``[] Optional``",
                                 color=nextcord.Color.blurple())
          embed.add_field(name="``/ping``", value="Shows client latency")
          embed.add_field(name="``/about``", value="Information about Norium Bot")
          embed.add_field(name="``/serverinfo``",
                          value="Information about the current guild")
          embed.add_field(name="``/links``", value="All Norium Bot related links")
          embed.add_field(name="``/version``",
                          value="The current version Norium Bot is on")
          embed.add_field(name="``/invite``", value="Invite Norium Bot")
          embed.add_field(name="``/vote``", value="Returns a vote link for Norium")
          embed.add_field(name="``/tag``", value="Displays your current tag, e.g. #1298")
          await interaction.edit(embed=embed)

        if self.values[0] == 'Marriage':
          embed = nextcord.Embed(title="<:bars:956962805788082206> Marriage Plugin",
                                 description="``<> Required``\n``[] Optional``",
                                 color=nextcord.Color.blurple())
          embed.add_field(name="``/propose @<member>``",
                          value="Propose to somebody")
          embed.add_field(
              name="``/maccept @<member>``",
              value=
              "Accept somebody's marriage"
          )
          embed.add_field(name="``/mdecline @<member>``", value="Decline somebody's marriage")
          embed.add_field(name="``/mdivorce @<member>``", value="Divorce someone")
          await interaction.edit(embed=embed)

class HelpDropView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(HelpDrop())

@client.slash_command(description = "A quick overview of all commands")
async def help(interaction : Interaction):
    support = Button(label="Support Server",
                     url="https://discord.gg/2xzfZtAKMf")
    website = Button(label="Website", url="https://noriumbot.com/")

    view = HelpDropView()
    view.add_item(support)
    view.add_item(website)

    embed = nextcord.Embed(title="<:bars:956962805788082206> Slash Commands Help",  description = "__**Announcement**__ *[04/29/2022]*\n\n:warning: Moderation slash commands are temporarily disabled as multiple vulnerabilities have been found in the code. We will notify you once we have implemented a fix for this major bug. It is **strongly** recommended you use moderation commands that start with a prefix (`-` in this case)",color=nextcord.Color.blurple())
    embed.add_field(name="**Slash**", value="Choose something from the dropdown below.")
    embed.add_field(name="Links", value="[Invite Me!](https://noriumbot.com/invite) | [Support](https://noriumbot.com/support) | [Check out our website](https://noriumbot.com)")
    await interaction.response.send_message(embed=embed, view=view)    
    
    
    

class HelpDropdown(nextcord.ui.Select):
    def __init__(self):
        selectOptions = [
            nextcord.SelectOption(label = "Moderation", description = "Displays all moderation features", emoji = "🛠️"),
            nextcord.SelectOption(label = "Fun", description = "Displays all fun features", emoji = "🎮"),
            nextcord.SelectOption(label = "Misc", description = "Displays all miscellaneous features", emoji = "✨"),
            nextcord.SelectOption(label = "Utility", description = "Displays all utility features", emoji = "🔨"),
            nextcord.SelectOption(label = "Management", description = "Displays all server management features", emoji = "👨‍🔧"),
            nextcord.SelectOption(label = "Marriage", description = "Displays all marriage features", emoji = "💍")
        ]
        super().__init__(placeholder='Select a category', min_values=1, max_values=1, options=selectOptions)

    async def callback(self, ctx):
        if self.values[0] == 'Management':
          embed = nextcord.Embed(title="<:bars:956962805788082206> Server Management Plugin",
                                 description="``<> Required``\n``[] Optional``",
                                 color=nextcord.Color.blurple())
          embed.add_field(name="``-slowmode <value_in_seconds>``",
                          value="Set the slowmode in seconds (e.g. -slowmode 3600)")
          embed.add_field(
              name=":warning: ``-txtnuke``",
              value=
              "Deletes all text channels\n**We recommend you do NOT perform this command.**"
          )
          embed.add_field(name="``-grename <new_name>``", value="Renames the guild")
          embed.add_field(name="``-massunban``", value="Unbans all members at once")
          await ctx.message.edit(embed=embed)

        if self.values[0] == 'Marriage':
          embed = nextcord.Embed(title="<:bars:956962805788082206> Marriage Plugin",
                                 description="``<> Required``\n``[] Optional``",
                                 color=nextcord.Color.blurple())
          embed.add_field(name="``-propose @<member>``",
                          value="Propose to somebody")
          embed.add_field(
              name="``-maccept @<member>``",
              value=
              "Accept somebody's marriage"
          )
          embed.add_field(name="``-mdecline @<member>``", value="Decline somebody's marriage")
          embed.add_field(name="``-mdivorce @<member>``", value="Divorce someone")
          await ctx.message.edit(embed=embed)
      
        if self.values[0] == 'Moderation':
          embed = nextcord.Embed(title="<:bars:956962805788082206> Moderation Plugin",
                                 description="``<> Required``\n``[] Optional``",
                                 color=nextcord.Color.blurple())
          embed.add_field(name="``-warn @<member> [reason]``", value="Warn a member")
          embed.add_field(name="``-mute @<member> [reason]``", value="Mute a member")
          embed.add_field(name="``-lock <reason>``",
                          value="Lock the current channel in which you are in")
          embed.add_field(name="``-ban @<member> [reason]``",
                          value="Ban a member from your server")
          embed.add_field(name="``-kick @<member> [reason]``",
                          value="Kick a member from your server")
          embed.add_field(
              name="``-unmute @<member>``",
              value="Unmute a member that was timed out",
                )
          embed.add_field(name="``-clear <msg_amount>``",
                          value="Clear several messages at once")
          embed.add_field(name="``-unban <user>#<discriminator>``",
                          value="Unban a member from your server")
          embed.add_field(name="``-unlock``", value="Unlock a channel")
          embed.add_field(name="``-moderate @<member>``",
                          value="Moderate a member's nickname")
          await ctx.message.edit(embed=embed)


        if self.values[0] == 'Utility':
            embed = nextcord.Embed(title="<:bars:956962805788082206> Utility Plugin",
                           color=nextcord.Color.blurple())
            embed.add_field(name="``-poll <option_1> <option_2> <topic>``",
                    value="Send a voting message")
            embed.add_field(name="``-guildcount``",
                    value="Shows the amount of servers Norium Bot is in")
            embed.add_field(
                name="``-template``",
                value=
                "A basic rule template in case you don't have rules already or don't know what rules you should put"
            )
            embed.add_field(name="``-embed <text>``",
                    value="Send a custom embed message")
            embed.add_field(name="``-profile @[member]``",
                    value="Your's or another user's profile")
            embed.add_field(name="``-avatar @[member]``",
                    value="Displays your avatar or another member's avatar")
            embed.add_field(name="``-commandcount``", value="Overall command count")
            embed.add_field(
                name="``-stats``",
                value="Displays Norium Bot's CPU, Memory Usage etc.")
            embed.add_field(name="``-error [code]``", value="Look up some bot errors")
            embed.add_field(name="``-giveaway <duration> <prize>``",
                    value="Create a giveaway")
            await ctx.message.edit(embed=embed)

        if self.values[0] == 'Fun':
                embed = nextcord.Embed(title="<:bars:956962805788082206> Fun Plugin",
                           description="``<> Required``\n``[] Optional``",
                           color=nextcord.Color.blurple())
                embed.add_field(name="``-bunger``", value="Bunger :hamburger:")
                embed.add_field(name="``-8ball <question>``",
                    value="Ask the almighty 8ball a question")
                embed.add_field(name="``-sus @[member]``", value="Sus-O-Meter :flushed:")
                embed.add_field(name="``-pp @[member]``", value="PP-O-Meter")
                embed.add_field(name="``-gayrate @[member]``",
                    value="See how gay you are or another member is")
                embed.add_field(name="``-kill @<member>``", value="Make someone unalive")
                embed.add_field(name="``-cat``", value="Sends random cat images")
                embed.add_field(name="``-dog``", value="Sends random dog images")
                embed.add_field(
                  name="``-simprate``",
                  value="See how much of a simp you are or another member is")
                embed.add_field(name="``-coinflip``", value="Flip a coin")
                embed.add_field(name="``-minecraft``",
                    value="Get a minecraft player's profile")
                embed.add_field(name="``-meme``", value="Sends a random meme")
                embed.add_field(name="``-egg``", value="Egg cat")
                await ctx.message.edit(embed=embed)

        if self.values[0] == 'Misc':
          embed = nextcord.Embed(title="<:bars:956962805788082206> Misc Plugin",
                                 description="``<> Required``\n``[] Optional``",
                                 color=nextcord.Color.blurple())
          embed.add_field(name="``-ping``", value="Shows client latency")
          embed.add_field(name="``-about``", value="Information about Norium Bot")
          embed.add_field(name="``-serverinfo``",
                          value="Information about the current guild")
          embed.add_field(name="``-links``", value="All Norium Bot related links")
          embed.add_field(name="``-version``",
                          value="The current version Norium Bot is on")
          embed.add_field(name="``-invite``", value="Invite Norium Bot")
          embed.add_field(name="``-vote``", value="Returns a vote link for Norium")
          embed.add_field(name = "``-tag``", value="Displays your discriminator, e.g. #1298")
          await ctx.message.edit(embed=embed)

class HelpDropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(HelpDropdown())

@client.group(invoke_without_command=True)
async def help(ctx):
    support = Button(label="Support Server",
                     url="https://discord.gg/2xzfZtAKMf")
    website = Button(label="Website", url="https://noriumbot.com/")

    view = HelpDropdownView()
    view.add_item(support)
    view.add_item(website)

    embed = nextcord.Embed(title="<:bars:956962805788082206> Help Menu", description = "__**Announcement**__ *[04/29/2022]*\n\n:warning: Moderation slash commands are temporarily disabled as multiple vulnerabilities have been found in the code. We will notify you once we have implemented a fix for this major bug. It is **strongly** recommended you use moderation commands that start with a prefix (`-` in this case)", color=nextcord.Color.blurple())
    embed.add_field(name="Moderation", value="``-help moderation``")
    embed.add_field(name="Misc", value="``-help misc``")
    embed.add_field(name="Utility", value="``-help utility``")
    embed.add_field(name="Fun", value="``-help fun``")
    embed.add_field(name="Server Management", value="``-help management``")
    embed.add_field(name = "Marriage", value = "``-help marriage``")
    embed.add_field(name="Links", value="[Invite Me!](https://noriumbot.com/invite) | [Support](https://noriumbot.com/support) | [Check out our website](https://noriumbot.com)")
    await ctx.send(embed=embed, view=view)


@help.command()
async def moderation(ctx):
    embed = nextcord.Embed(title="<:bars:956962805788082206> Moderation Plugin",
                           description="``<> Required``\n``[] Optional``",
                           color=nextcord.Color.blurple())
    embed.add_field(name="``-warn @<member> [reason]``", value="Warn a member")
    embed.add_field(name="``-mute @<member> [reason]``", value="Mute a member")
    embed.add_field(name="``-lock <reason>``",
                    value="Lock the current channel in which you are in")
    embed.add_field(name="``-ban @<member> [reason]``",
                    value="Ban a member from your server")
    embed.add_field(name="``-kick @<member> [reason]``",
                    value="Kick a member from your server")
    embed.add_field(
        name="``-unmute @<member>``",
        value="Unmute a member that was timed out",
    )
    embed.add_field(name="``-clear <msg_amount>``",
                    value="Clear several messages at once")
    embed.add_field(name="``-unban <user>#<discriminator>``",
                    value="Unban a member from your server")
    embed.add_field(name="``-unlock``", value="Unlock a channel")
    embed.add_field(name="``-moderate @<member>``",
                    value="Moderate a member's nickname")
    await ctx.send(embed=embed)


@help.command()
async def misc(ctx):
    embed = nextcord.Embed(title="<:bars:956962805788082206> Misc Plugin",
                           description="``<> Required``\n``[] Optional``",
                           color=nextcord.Color.blurple())
    embed.add_field(name="``-ping``", value="Shows client latency")
    embed.add_field(name="``-about``", value="Information about Norium Bot")
    embed.add_field(name="``-serverinfo``",
                    value="Information about the current guild")
    embed.add_field(name="``-links``", value="All Norium Bot related links")
    embed.add_field(name="``-version``",
                    value="The current version Norium Bot is on")
    embed.add_field(name = "``-vote``", value="Returns the vote link for Norium")
    embed.add_field(name = "``-invite``", value="Returns the invite")
    embed.add_field(name="``-tag``", value="Allows you to view people's tag")
    await ctx.send(embed=embed)


@help.command()
async def fun(ctx):
    embed = nextcord.Embed(title="<:bars:956962805788082206> Fun Plugin",
                           description="``<> Required``\n``[] Optional``",
                           color=nextcord.Color.blurple())
    embed.add_field(name="``-bunger``", value="Bunger :hamburger:")
    embed.add_field(name="``-8ball <question>``",
                    value="Ask the almighty 8ball a question")
    embed.add_field(name="``-sus @[member]``", value="Sus-O-Meter :flushed:")
    embed.add_field(name="``-pp @[member]``", value="PP-O-Meter")
    embed.add_field(name="``-gayrate @[member]``",
                    value="See how gay you are or another member is")
    embed.add_field(name="``-kill @<member>``", value="Make someone unalive")
    embed.add_field(name="``-cat``", value="Sends random cat images")
    embed.add_field(name="``-dog``", value="Sends random dog images")
    embed.add_field(
        name="``-simprate``",
        value="See how much of a simp you are or another member is")
    embed.add_field(name="``-coinflip``", value="Flip a coin")
    embed.add_field(name="``-minecraft``",
                    value="Get a minecraft player's profile")
    embed.add_field(name="``-meme``", value="Sends a random meme")
    embed.add_field(name="``-egg``", value="Egg cat")
    await ctx.send(embed=embed)


@help.command()
async def management(ctx):
    embed = nextcord.Embed(title="<:bars:956962805788082206> Server Management Plugin",
                           description="``<> Required``\n``[] Optional``",
                           color=nextcord.Color.blurple())
    embed.add_field(name="``-slowmode <value_in_seconds>``",
                    value="Set the slowmode in seconds (e.g. .slowmode 3600)")
    embed.add_field(
        name=":warning: ``-txtnuke``",
        value=
        "Deletes all text channels\n**We recommend you do NOT perform this command.**"
    )
    embed.add_field(name="``-grename <new_name>``", value="Renames the guild")
    embed.add_field(name="``-massunban``", value="Unbans all members at once")
    await ctx.send(embed=embed)

@help.command()
async def marriage(ctx):
          embed = nextcord.Embed(title="<:bars:956962805788082206> Marriage Plugin",
                                 description="``<> Required``\n``[] Optional``",
                                 color=nextcord.Color.blurple())
          embed.add_field(name="``-propose @<member>``",
                          value="Propose to somebody")
          embed.add_field(
              name="``-maccept @<member>``",
              value=
              "Accept somebody's marriage"
          )
          embed.add_field(name="``-mdecline @<member>``", value="Decline somebody's marriage")
          embed.add_field(name="``-mdivorce @<member>``", value="Divorce someone")
          await ctx.message.edit(embed=embed)


@help.command()
async def utility(ctx):
    embed = nextcord.Embed(title="<:bars:956962805788082206> Utility Plugin",
                           color=nextcord.Color.blurple())
    embed.add_field(name="``-poll <option_1> <option_2> <topic>``",
                    value="Send a voting message")
    embed.add_field(name="``-guildcount``",
                    value="Shows the amount of servers Norium Bot is in")
    embed.add_field(
        name="``-template``",
        value=
        "A basic rule template in case you don't have rules already or don't know what rules you should put"
    )
    embed.add_field(name="``-embed <text>``",
                    value="Send a custom embed message")
    embed.add_field(name="``-profile @[member]``",
                    value="Your's or another user's profile")
    embed.add_field(name="``-avatar @[member]``",
                    value="Displays your avatar or another member's avatar")
    embed.add_field(name="``-commandcount``", value="Overall command count")
    embed.add_field(
        name="``-stats``",
        value="Displays Norium Bot's CPU Time, Memory Usage and Uptime")
    embed.add_field(name="``-error [code]``", value="Look up some bot errors")
    embed.add_field(name="``-giveaway <duration> <prize>``",
                    value="Create a giveaway")
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_channels=True)
async def txtnuke(ctx):
    embed = nextcord.Embed(
        title=":warning: Are you sure?",
        description=
        "All changes are irreversible, we are not responsible for any damage done to your server.",
        color=nextcord.Color.red())

    view = Confirm()
    await ctx.send(embed=embed, view=view)

    await view.wait()

    if view.value == True:
        for c in ctx.guild.channels:
            await c.delete()


class Confirm(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label="Confirm", style=nextcord.ButtonStyle.danger)
    async def confirm(self, button: nextcord.ui.Button,
                      interaction: nextcord.Interaction):
        await interaction.response.send_message("Deleting channels...",
                                                ephemeral=True)
        self.value = True
        self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.blurple)
    async def cancel(self, button: nextcord.ui.Button,
                     interaction: nextcord.Interaction):
        embed = nextcord.Embed(title="Cancelling...",
                               description="Process cancelled.",
                               color=nextcord.Color.green())
        await interaction.response.send_message(embed=embed, ephemeral=True)
        self.value = False
        self.stop()


@txtnuke.error
async def txtnuke_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = nextcord.Embed(
            title="No Permissions",
            description="You are missing the ``MANAGE_CHANNELS`` permission.",
            color=nextcord.Color.red())
        await ctx.send(embed=embed)


@client.command(aliases=["botinfo", "norium", "noriumbot", "info", "ab"])
async def about(ctx):
    embed = nextcord.Embed(
        title="About Norium Bot",
        description=
        "[Invite](https://discord.com/api/oauth2/authorize?client_id=871454184212410408&scope=applications.commands) | [Docs](https://noriumbot.com/docs) | [Vote](https://top.gg/bot/871454184212410408/vote)\n\nNorium Bot is a multi-purpose Discord Bot focusing on giving the user the best possible experience.",
        color=nextcord.Color.blurple())
    embed.set_image(
        url=
        "https://cdn.discordapp.com/attachments/809692926833459221/956572804919226408/logo.pmng.png"
    )
    await ctx.send(embed=embed)


@client.group(invoke_without_command=True, aliases=["errorcode", "ec", "code"])
async def error(ctx):
    embed = nextcord.Embed(title="Errors", color=nextcord.Color.red())
    embed.add_field(name="No Permissions",
                    value="``-error permissions``",
                    inline=False)
    embed.add_field(name="Invalid Syntax",
                    value="``-error syntax``",
                    inline=False)
    embed.add_field(name="Member Not Found",
                    value="``-error member``",
                    inline=False)
    await ctx.send(embed=embed)

@error.command()
async def permissions(ctx):
    embed = nextcord.Embed(
        title="No Permissions",
        description="A command which you do not have permissions for.",
        color=nextcord.Color.red())
    await ctx.send(embed=embed)


@error.command()
async def syntax(ctx):
    embed = nextcord.Embed(
        title="Invalid Syntax",
        description=
        "A command in which you did not include a required argument.",
        color=nextcord.Color.red())
    await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def reboot(ctx):
  embed = nextcord.Embed(
    description = "Rebooting, this may take a while as it is loading all cogs.",
    color = nextcord.Color.red()
  )
  await client.close()

@error.command()
async def member(ctx):
    embed = nextcord.Embed(
        title="Member Not Found",
        description="The member you mentioned doesn't exist.",
        color=nextcord.Color.red())
    await ctx.send(embed=embed)

@client.command()
async def meme(ctx):
    memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')

    memeData = json.load(memeAPI)

    memeURL = memeData['url']
    memeName = memeData['title']
    memePost = memeData['author']
    memeSub = memeData['subreddit']
    memeLink = memeData['postLink']

    embed = nextcord.Embed(title=f"{memeName}",
                           color=nextcord.Color.blurple(),
                           url=f"{memeURL}")
    embed.set_image(url=memeURL)
    embed.set_footer(text=f"r/{memeSub}")
    await ctx.send(embed=embed) #credit: glowstik

keep_alive.keep_alive()
client.run(BOT_TOKEN)
