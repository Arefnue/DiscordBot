import discord
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, client):

        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("General bot is ready...")
    

    #Commands
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"Pong! Your ping is {round(self.client.latency*1000)} ms!")
        


def setup(client):
    print("General is online")
    client.add_cog(General(client))
