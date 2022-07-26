import discord
from discord.ext import commands
from better_profanity import profanity


TOKEN = "MTAwMDk0MDczNDkwMTQwNzgzNA.GvebtP.enuJXQmxUHuwRtZLmEjHMtscz57unLy9TvrCqw"
client = commands.Bot(command_prefix = '~', intents = discord.Intents().all())

@client.event
async def on_ready():
    print("bot is ready")


@client.event
async def on_member_join(member):
    for guild in client.guilds:
        for channel in guild.text_channels:
            if channel.name == "welcome":
                temp = await channel.send("Hey " + member.mention + ", welcome to The Chatrooms! Please press the ✅ to get started.")
                await temp.add_reaction("✅")

@client.event
async def on_reaction_add(reaction, user):
    if (not user.bot and reaction.message.author.bot):
        if(reaction.emoji == "✅"):
            if user in reaction.message.mentions and reaction.message.channel.name == "welcome":
                await user.create_dm()
                await user.dm_channel.send("Nice to meet you " + user.name + "! I am the Mental Rest bot.")
                embed = discord.Embed(title="Which community or communities would you like to explore?",
                description = "1️⃣ = Anorexia\n2️⃣ = Bulimia\n3️⃣ = Pica\n4️⃣ = Prader Willi Syndrome\n" +
                                      "5️⃣ = Borderline Personality Disorder\n6️⃣ = Schizophrenia\n7️⃣ = Alien Hand Syndrome\n"
                                      + "8️⃣ = Dissociative Amnesia\n9️⃣ = Depersonalisation Disorder\n🔟 = Dissociative Identity Disorder")
                temp = await user.dm_channel.send(embed=embed)
                await temp.add_reaction("1️⃣")
                await temp.add_reaction("2️⃣")
                await temp.add_reaction("3️⃣")
                await temp.add_reaction("4️⃣")
                await temp.add_reaction("5️⃣")
                await temp.add_reaction("6️⃣")
                await temp.add_reaction("7️⃣")
                await temp.add_reaction("8️⃣")
                await temp.add_reaction("9️⃣")
                await temp.add_reaction("🔟")
        elif reaction.message.channel == user.dm_channel:
            if reaction.emoji == "1️⃣":
                for guild in client.guilds:
                    for channel in guild.text_channels:
                        if channel.name == "anorexia-chat":
                            member = await guild.fetch_member(user.id)
                            if member in channel.members:
                                await reaction.remove(user)
                                return
                            var = discord.utils.get(guild.roles, name="Anorexia Member")
                            await member.add_roles(var)
                            await reaction.message.channel.send("You are now part of the Mental Rest Anorexia community! Please remember to follow the rules stated in the rules channel.")
                            await channel.send("Welcome " + member.mention + " to Mental Rest's Anorexia community!")
            elif reaction.emoji == "2️⃣":
                for guild in client.guilds:
                    for channel in guild.text_channels:
                        if channel.name == "bulimia-chat":
                            member = await guild.fetch_member(user.id)
                            if member in channel.members:
                                await reaction.remove(user)
                                return
                            var = discord.utils.get(guild.roles, name="Bulimia Member")
                            await member.add_roles(var)
                            await reaction.message.channel.send("You are now part of the Mental Rest Bulimia community! Please remember to follow the rules stated in the rules channel.")
                            await channel.send("Welcome " + member.mention + " to Mental Rest's Bulimia community!")
            elif reaction.emoji == "3️⃣":
                for guild in client.guilds:
                    for channel in guild.text_channels:
                        if channel.name == "pica-chat":
                            member = await guild.fetch_member(user.id)
                            if member in channel.members:
                                await reaction.remove(user)
                                return
                            var = discord.utils.get(guild.roles, name="Pica Member")
                            await member.add_roles(var)
                            await reaction.message.channel.send("You are now part of the Mental Rest Pica community! Please remember to follow the rules stated in the rules channel.")
                            await channel.send("Welcome " + member.mention + " to Mental Rest's Pica community!")
            elif reaction.emoji == "4️⃣":
                for guild in client.guilds:
                    for channel in guild.text_channels:
                        if channel.name == "pws-chat":
                            member = await guild.fetch_member(user.id)
                            if member in channel.members:
                                await reaction.remove(user)
                                return
                            var = discord.utils.get(guild.roles, name="Prader Willi Syndrome Member")
                            await member.add_roles(var)
                            await reaction.message.channel.send("You are now part of the Mental Rest Prader Willi Syndrome community! Please remember to follow the rules stated in the rules channel.")
                            await channel.send("Welcome " + member.mention + " to Mental Rest's Prader Willi Syndrome community!")
            elif reaction.emoji == "5️⃣":
                for guild in client.guilds:
                    for channel in guild.text_channels:
                        if channel.name == "bpd-chat":
                            member = await guild.fetch_member(user.id)
                            if member in channel.members:
                                await reaction.remove(user)
                                return
                            var = discord.utils.get(guild.roles, name="Borderline Personality Disorder Member")
                            await member.add_roles(var)
                            await reaction.message.channel.send("You are now part of the Mental Rest Borderline Personality Disorder community! Please remember to follow the rules stated in the rules channel.")
                            await channel.send("Welcome " + member.mention + " to Mental Rest's Borderline Personality Disorder community!")
            elif reaction.emoji == "6️⃣":
                for guild in client.guilds:
                    for channel in guild.text_channels:
                        if channel.name == "schizophrenia-chat":
                            member = await guild.fetch_member(user.id)
                            if member in channel.members:
                                await reaction.remove(user)
                                return
                            var = discord.utils.get(guild.roles, name="Schizophrenia Member")
                            await member.add_roles(var)
                            await reaction.message.channel.send("You are now part of the Mental Rest Schizophrenia community! Please remember to follow the rules stated in the rules channel.")
                            await channel.send("Welcome " + member.mention + " to Mental Rest's Schizophrenia community!")
            elif reaction.emoji == "7️⃣":
                for guild in client.guilds:
                    for channel in guild.text_channels:
                        if channel.name == "ahs-chat":
                            member = await guild.fetch_member(user.id)
                            if member in channel.members:
                                await reaction.remove(user)
                                return
                            var = discord.utils.get(guild.roles, name="Alien Hand Syndrome Member")
                            await member.add_roles(var)
                            await reaction.message.channel.send("You are now part of the Mental Rest Alien Hand Syndrome community! Please remember to follow the rules stated in the rules channel.")
                            await channel.send("Welcome " + member.mention + " to Mental Rest's Alien Hand Syndrome community!")
            elif reaction.emoji == "8️⃣":
                for guild in client.guilds:
                    for channel in guild.text_channels:
                        if channel.name == "da-chat":
                            member = await guild.fetch_member(user.id)
                            if member in channel.members:
                                await reaction.remove(user)
                                return
                            var = discord.utils.get(guild.roles, name="Dissociative Amnesia Member")
                            await member.add_roles(var)
                            await reaction.message.channel.send("You are now part of the Mental Rest Dissociative Amnesia community! Please remember to follow the rules stated in the rules channel.")
                            await channel.send("Welcome " + member.mention + " to Mental Rest's Dissociative Amnesia community!")
            elif reaction.emoji == "9️⃣":
                for guild in client.guilds:
                    for channel in guild.text_channels:
                        if channel.name == "dpd-chat":
                            member = await guild.fetch_member(user.id)
                            if member in channel.members:
                                await reaction.remove(user)
                                return
                            var = discord.utils.get(guild.roles, name="Depersonalisation Disorder Member")
                            await member.add_roles(var)
                            await reaction.message.channel.send("You are now part of the Mental Rest Depersonalisation Disorder community! Please remember to follow the rules stated in the rules channel.")
                            await channel.send("Welcome " + member.mention + " to Mental Rest's Depersonalisation Disorder community!")
            elif reaction.emoji == "🔟":
                for guild in client.guilds:
                    for channel in guild.text_channels:
                        if channel.name == "did-chat":
                            member = await guild.fetch_member(user.id)
                            if member in channel.members:
                                await reaction.remove(user)
                                return
                            var = discord.utils.get(guild.roles, name="Dissociative Identity Disorder Member")
                            await member.add_roles(var)
                            await reaction.message.channel.send("You are now part of the Mental Rest Dissociative Identity Disorder community! Please remember to follow the rules stated in the rules channel.")
                            await channel.send("Welcome " + member.mention + " to Mental Rest's Dissociative Identity Disorder community!")
#cuss word filter
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    if(profanity.contains_profanity(user_message)):
        await message.delete()
    await client.process_commands(message)

@client.command()
async def info(channel):
    if channel.channel.name == "botcommands":
        embed = discord.Embed(
            title="Commands"
        )
        embed.add_field(name="~info", value="Displays all commands", inline=False)
        embed.add_field(name="~nearbyhelp", value="Displays nearby hospitals based on user's location", inline=False)
        embed.add_field(name="~talk", value="Bot starts a conversation with the user using NLP", inline=False)
        await channel.send(embed=embed)

@client.command()
async def nearbyhelp(ctx):
    await ctx.message.author.create_dm()
    await ctx.message.author.dm_channel.send("You've requested to seek nearby help. What is your address?")
    address = await client.wait_for("message")
    embed = discord.Embed(title = "Hospitals near " + str(address.content))
    file = discord.File("hospitals.PNG", filename="image.PNG")
    embed.set_image(url="attachment://image.PNG")
    await ctx.message.author.dm_channel.send(file = file, embed = embed)

@client.command()
async def talk(ctx):
    await ctx.message.author.create_dm()
    await ctx.message.author.dm_channel.send("Hi " + ctx.message.author.name + ", nice to meet you!")
    msg = await client.wait_for("message")
    await ctx.message.author.dm_channel.send("So I understand that you referred here by visiting the Mental Rest website because you've been feeling quite down recently.")
    msg = await client.wait_for("message")
    await ctx.message.author.dm_channel.send("So how long have you been feeling down altogether?")
    msg = await client.wait_for("message")
    await ctx.message.author.dm_channel.send("Okay, so it seems that it's gotten worse in these past months. So tell me, how are things at the moment?")
    mes = await client.wait_for("message")
    await ctx.message.author.dm_channel.send("Okay, so you said that you were feeling very down, sad, and not having any motivation. It looks like you've put quite a lot of pressure on yourself to feel quite a bit better.")

client.run(TOKEN)