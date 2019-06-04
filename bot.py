import discord
import time
import asyncio

token = open("token.txt", "r").read()

client = discord.Client()

joined = 0
messages = 0


async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(
                    f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

            messages = 0
            joined = 0

            await asyncio.sleep(10)
        except Exception as e:
            print(e)
            await asyncio.sleep(10)


@client.event  
async def on_ready():  
    print(f'We have logged in as {client.user}')
    
    
   

@client.event
async def on_message(message):  
    global messages
    messages += 1

    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    id = client.get_guild(501078304745586699)

    channels = ["japoçlar"]
    valid_users = ["Tim#9298"]  # Only users in this list can use commands

    if str(message.channel) in channels and str(message.author) in valid_users:
    
        if "!hello" in message.content.lower():
            await message.channel.send("HI!")
        elif message.content == "!users":
            await message.channel.send(f"""Members: {id.member_count}""")

    # Deleting bad words
    bad_words = ["bad", "stop", "45"]
    for word in bad_words:
        if message.content.count(word) > 0:
            print("A bad word was said")
            await message.channel.purge(limit=1)

    #Helping
    if message.content == "!help":
        embed = discord.Embed(title="Help on BOT", description="Some useful commands")
        embed.add_field(name="!hello", value="Greets the user")
        embed.add_field(name="!users", value="Prints number of users")
        await message.channel.send(content=None, embed=embed)
        
@client.event
async def on_member_join(member):

    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""NDNG ailesine hoş geldin {member.mention}!""")


@client.event  # This event runs whenever a user updates: status, game playing, avatar, nickname or role
async def on_member_update(before, after):
    n = after.nick
    if n:  # Check if they updated their username
        if n.lower().count("bot") > 0:  # If username contains tim
            last = before.nick
            if last:  # If they had a usernae before change it back to that
                await after.edit(nick=last)
            else:  # Otherwise set it to "NO STOP THAT"
                await after.edit(nick="NO STOP THAT")

client.loop.create_task(update_stats())
client.run(token) 
