import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random

class Lol(commands.Cog):

    def __init__(self, client):

        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Lol bot is ready...")

    #Commands
    @commands.command()
    async def getir(self, ctx):
        await ctx.send("Getiriliyor...")

        # Collect and parse 
        page = requests.get('https://leagueoflegends.fandom.com/wiki/Champion_skin/All_skins')
        soup = BeautifulSoup(page.content, 'html.parser')
        #Getting information
        div = soup.find("div", attrs={"id", "mw-content-text"})
        table = div.find("table")
        skins = table.find_all("td", attrs={"class", "skin-icon"})
        #Check skins
        allowed_skins = []
        for skin in skins:
            if not skin.text.startswith("Original") or skin.text.endswith("Edition"):
                allowed_skins.append(skin.text)

        skins_len = len(allowed_skins)
        #Troll
        troll = []
        troll += 100*["Yarrak"]+50*["Damarlı küçük yarrak"]+10*["Damarlı büyük yarrak"]+["Talay'ın Annesi"]
        troll_len = len(troll)
        allowed_skins.append(troll)
        random_skin = allowed_skins[random.randint(0,skins_len-1 + troll_len-1)]
        
        await ctx.send(f"""
            {skins_len} skin arasından sana çıkan şey:
            {random_skin}
        """)

def setup(client):
    print("Lol is online")
    client.add_cog(Lol(client))



