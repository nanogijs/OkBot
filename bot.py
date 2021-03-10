import discord
from yahoo_fin import stock_info as si
client = discord.Client()
import random
import time
stockprice = None
masked_link_embed = discord.Embed(
    title="Heared you guys talking about my friend Rick",
    description='[He is awesome, just see this!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)',
    color=discord.Colour.teal()
)
masked_gme = discord.Embed(
    title="Can\'t stop, Won\'t stop, Gamestop",
    description='Current GME price is $' + str(round(si.get_live_price("gme"),2)),
    color=discord.Colour.teal()
)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'ok':
        await message.channel.send('Ok')
        n = random.randint(0, 100)
        if n <= 4:
            await message.channel.send('Ok rage mode activated!')
            for x in range(0, 10):
                await message.channel.send('Ok')
                time.sleep(1)

    if message.content.lower() == 'cyka':
        await message.channel.send('blyat')
    if message.content.lower() == 'blyat':
        await message.channel.send('kiska')
    if message.content.lower() == 'sander':
        await message.channel.send('Sander is kast')
    if message.content.lower() == 'kast':
        await message.channel.send('kast? Ahhh, You mean Sander!')
    if message.content.lower() == 'hotel':
        await message.channel.send('Trivago')
    if message.content.lower() == 'hentai':
        await message.channel.send('Yes Senpai')
    if "rick" in message.content.lower():
        await message.channel.send(embed=masked_link_embed)
    if message.content.lower() == 'oke':
        await message.channel.send('Oke')
    if 'ninja' in message.content.lower():
        await message.channel.send('You kiss your mother with that fucking mouth? ')
    if message.content.lower() == 'yes or no':
        await message.channel.send('Let me start from the beginning, when I was a boy in Bulgaria...')
    if "gamestop" in message.content.lower():
        await message.channel.send(embed=masked_gme)
    if message.content.lower() == 'gme':
        await message.channel.send(embed=masked_gme)
    if message.content.startswith('$'):
        stockprice = (message.content.upper())
        stockprice = stockprice.replace('$',"")
        masked_price = discord.Embed(
    title="Here is your requested stock!",
    description='Current ' + stockprice + ' price is $' + str(round(si.get_live_price(str(stockprice)),2)),
    color=discord.Colour.teal()
)
        await message.channel.send(embed=masked_price)
        

client.run('Insert your token here')