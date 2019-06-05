import discord
import time
import asyncio
import os
from discord.ext import commands

# Server informations
# index 0=server_id, 1=token, 2=client_secret, 3=client_id
server = []

with open("server.txt", "rt") as myfile:
    for myline in myfile:
        server.append(myline.rstrip("\n"))

serverID = int(server[0])
token = server[1]


bot = commands.Bot(command_prefix = '*')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(token)
