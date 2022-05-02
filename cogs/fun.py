import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import urllib 
import json
import random
import aiohttp
import json
import asyncio

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client 

    guild_ids = 946310802250530846

    @nextcord.slash_command(description = "Flip the coin")
    async def coinflip(self, interaction : Interaction):
        sides = [
            "Heads",
            "Tails"
        ]

        embed = nextcord.Embed(
            title = "Coin flipped",
            description = "The coin was flipped and landed on **{random.choice(sides)}**!",
            color = nextcord.Color.random()
        )

        await interaction.response.send_message(
            embed=embed
        )

    @nextcord.slash_command(description = "Sends a random meme")
    async def meme(self, interaction : Interaction):
        memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')

        memeData = json.load(memeAPI)

        memeURL = memeData['url']
        memeName = memeData['title']
        memePost = memeData['author']
        memeSub = memeData['subreddit']
        memeLink = memeData['postLink']

        embed = nextcord.Embed(
            title=f"{memeName}",
            url = f"{memeLink}",
            color=nextcord.Color.blurple()
        )

        embed.set_image(
            url=memeURL
        )

        embed.set_footer(
            text=f"r/{memeSub}"
        )

        await interaction.response.send_message(
            embed=embed
        )
    

    @nextcord.slash_command(description = "Ask the magical 8ball a question")
    async def ask(self, interaction : Interaction, question):
        responses = [
            "It is certain.", "It is decidedly so.", "Without a doubt.",
            "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
            "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
            "Reply hazy, try again.", "Ask again later.",
            "Better not tell you now.", "Cannot predict now.",
            "Concentrate and ask again.", "Don't count on it.",
            "My reply is no.", "My sources say no.", "Outlook not so good.",
            "Very doubtful."
        ]

        embed = nextcord.Embed(
            title="🎱 8ball says...",
            color=nextcord.Color.random()
        )

        embed.add_field(
            name="Question", 
            value=f"{question}", 
            inline="false"
        )

        embed.add_field(name="Answer",
                        value=f"{random.choice(responses)}",
                        inline="false"
        )

        embed.set_thumbnail(
            url = "https://cdn.discordapp.com/attachments/948235933709373470/948606008937312336/Webp.png"
        )

        await interaction.response.send_message(
            embed=embed
        )

    @nextcord.slash_command(description = "Bunger")
    async def bunger(self, interaction : Interaction):
        embed = nextcord.Embed(
            title = "Bunger :hamburger:",
            description = "Bunger :hamburger:",
            color = nextcord.Color.gold()
        )
        
        embed.set_image(
            url = "https://cdn.discordapp.com/attachments/853196607548555285/875999967838343198/tenor.gif"
        )

        await interaction.response.send_message(
            embed=embed
        )
        
    @nextcord.slash_command(description = "Egg.")
    async def eggcat(self, interaction : Interaction):
        embed = nextcord.Embed(
            title = "Oh the misery...",
            description = "Egg cat :egg:",
            color = nextcord.Color.light_grey()
        )
        
        embed.set_image(
            url = "https://media.discordapp.net/attachments/936115643835629639/964603292132982784/oh-the-misery-eggcat.gif?width=380&height=547"
        )

        await interaction.response.send_message(
            embed=embed
        )
    
    @nextcord.slash_command(description = "Sends a random cat image")
    async def cat(self, interaction : Interaction):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://aws.random.cat/meow") as r:
                data = await r.json()

            embed = nextcord.Embed(
                title = "🐱 Meowww...",
                color = nextcord.Color.random()
            )

            embed.set_image(
                url = data['file']
            )

            await interaction.response.send_message(
                embed=embed
            )

    @nextcord.slash_command(description = "See how gay you are or how gay another member is")
    async def gayrate(self, interaction : Interaction, member : nextcord.Member = SlashOption(description = "Member you want to see how gay they are", required=False)):
        if member == None:
            member = interaction.user

        embed = nextcord.Embed(
            title = "Gayrate",
            description = f"{member.mention} is **{random.randint(1, 100)}%** gay!",
            color = nextcord.Color.random()
        )

        embed.set_thumbnail(
            url = "https://cdn.discordapp.com/attachments/948235933709373470/948606707926462484/images.png"
        )

        await interaction.response.send_message(
            embed=embed
        )

    @nextcord.slash_command(description = "Make somebody unalive")
    async def kill(self, interaction : Interaction, *, member : nextcord.Member = SlashOption(description = "The member you want to make unalive", required=True)):
        if member == interaction.user:
            await interaction.response.send_message(
                "No! You can't kill yourself, this isn't how you're supposed to play the game!"
            )
        else:
            way = [
                f"hugged {member.mention} to death",
                f"poisoned {member.mention}",
                f"pushed {member.mention} off a cliff",
                f"spawned a zombie which killed {member.mention}",
                f"pushed {member.mention} on a railway",
                f"set {member.mention} on fire",
                f"held {member.mention}'s underwater for 10 days straight",
                f"threw a bunch of knives at {member.mention}",
                f"boxed {member.mention} to death",
                f"sent too much cringe posts until {member.mention} died",
                f"removed {member.mention}'s brain",
                f"destroyed {member.mention}'s braincells",
                f"slapped {member.mention} to South Africa",
                f"kept {member.mention} in their basement for 50 years",
                f"sent Gordon Ramsay to {member.mention} so he can insult them to death",
                f"acquired the Infinity Gauntlet and snapped {member.mention} away",
                f"sent the Man behind the slaughter to {member.mention}",
                f"was too cringe for {member.mention}",
                f"just gave an electric shock to {member.mention}",
                f"punched {member.mention} using their crocs",
                f"literally fed plastic to {member.mention}",
                f"cancelled {member.mention}",
                f"killed {member.mention} using a turtle",
                f"reported {member.mention} to the FBI"
            ]
            
            embed = nextcord.Embed(
                title = "Killed",
                description = f"{interaction.user.mention} {random.choice(way)}",
                color = nextcord.Color.blurple()
            )

            await interaction.response.send_message(
                embed=embed
            )


    @nextcord.slash_command(description = "Sends your PP Size")
    async def pp(self, interaction : Interaction, *, member : nextcord.Member = SlashOption(description = "The member you'd like to view the PP size of", required=False)):
        if member == None:
            member = interaction.user

        pp = [
            "8D",
            "8=D",
            "8==D",
            "8===D",
            "8====D",
            "8=====D",
            "8======D",
            "8=======D",
            "8========D",
            "8=========D",
            "8==========D",
            "8===========D",
            "8============D",
            "8=============D",
            "8==============D",
            "8===============D",
            "8================D",
            "8=================D",
            "8==================D",
            "8===================D",
            "8====================D",
            "8=====================D",
            "8======================D",
            "8=======================D",
            "8========================D",
            "8=========================D",
            "8==========================D"
        ]

        embed = nextcord.Embed(
            title = f"PP-O-Meter",
            description = f"{member.mention}'s PP Size\n{random.choice(pp)}",
            color = nextcord.Color.random()
        )

        await interaction.response.send_message(
            embed=embed
        )

    @nextcord.slash_command(description = "Rolls the dice")
    async def rolldice(self, interaction : Interaction):
        embed = nextcord.Embed(
            title = "Rolled the dice",
            description = f"The dice was rolled and landed on **{random.randint(1, 6)}**!",
            color = nextcord.Color.random()
        )

        await interaction.response.send_message(
            embed=embed
        )

    @nextcord.slash_command(description = "Shows how much of a simp you are or another member is")
    async def simprate(self, interaction : Interaction, *, member : nextcord.Member = SlashOption(description = "The member you'd like to see how much of a simp they are", required=False)):
        if member == None:
            member = interaction.user

        embed = nextcord.Embed(
            title = f"Simp-O-Meter",
            description = f"{member.mention} is **{random.randint(1, 100)}%** a simp!",
            color = nextcord.Color.random()
        )

        await interaction.response.send_message(
            embed=embed
        )

    @nextcord.slash_command(description = "Shows how sus you are or another member is")
    async def sus(self, interaction : Interaction, *, member : nextcord.Member = SlashOption(description = "The member you'd like to see how sus they are", required=False)):
        if member == None:
            member = interaction.user

        embed = nextcord.Embed(
            title = f"Sus-O-Meter",
            description = f"{member.mention} is **{random.randint(1, 100)}%** sus!",
            color = nextcord.Color.random()
        )

        await interaction.response.send_message(
            embed=embed
        )



def setup(client):
    client.add_cog(Fun(client))
