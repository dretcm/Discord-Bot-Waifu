import discord
from discord.ext import commands

import requests
from bs4 import BeautifulSoup
import json

bot = commands.Bot(command_prefix='+', description="This is a Helper Bot") # (command for calling you bot, description)

@bot.command()
async def say(ctx, *,  msg):
        await ctx.send(msg + ' pedo')

@bot.command()
async def waifu(ctx):
        link = 'https://mywaifulist.moe/random'
        html = requests.get(link).content
        soup = BeautifulSoup(html, 'html.parser')
        
        string = str(soup.find_all('script', attrs={"type":"application/ld+json"}))[36:-10] # filter
        data = json.loads(string)

        embed = discord.Embed(title=data['givenName'], color=discord.Color.blue())
        embed.set_image(url=data['image'])

        message = await ctx.send(embed=embed)

        with open('emojis.txt','r',encoding='utf-8') as f:
                for i in f.read()[:-1]:
                        await message.add_reaction(str(i))
                        
                        
print('Bot activate...')
bot.run('token')  # token or bot or key.





