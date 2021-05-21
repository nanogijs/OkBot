import discord

from yahoo_fin import stock_info as si
import cryptocompare
from pymongo import MongoClient
import random
import time
#Connect to mongoDB
cluster = MongoClient('YOUR LINK HERE')
db = cluster["Discord"]
collection = db["Discord"]


client = discord.Client()
stockprice = None
discmessage = None

masked_link_embed = discord.Embed(
    title="Heared you guys talking about my friend Rick",
    description='[He is awesome, just see this!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)',
    color=discord.Colour.teal())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global discmessage
    discmessage = message
    if message.author == client.user:
        return

    if message.content.lower() == 'ok':
        await message.channel.send('Ok')
        n = random.randint(0, 100)
        if n <= 5:
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
        return await sendgme()
    if message.content.lower() == 'gme':
        return await sendgme()
    if message.content.startswith('$'):
        return await requeststock()
    if message.content.startswith('#'):
        return await sendcrypto()

async def sendgme():
    masked_gme = discord.Embed(
    title="Can\'t stop, Won\'t stop, Gamestop",
    description='Current GME price is $' + str(round(si.get_live_price("gme"),2)),
    color=discord.Colour.teal())
    await discmessage.channel.send(embed=masked_gme)

async def requeststock():
    stockprice = (discmessage.content.upper())
    stockprice = stockprice.replace('$',"")
    masked_price = discord.Embed(
    title="Here is your requested stock!",
    description='Current ' + stockprice + ' price is $' + str(round(si.get_live_price(str(stockprice)),2)),
    color=discord.Colour.teal())
    await discmessage.channel.send(embed=masked_price)

async def sendcrypto():
    crypto = (discmessage.content.upper())
    crypto = crypto.replace('#',"")
    masked_crypto = discord.Embed(
    title="Here is your requested Crypto!",
    description='Current ' + str(crypto) + ' price is $' + str(cryptocompare.get_price(str(crypto), currency='USD')).replace('{',"").replace('}',"").replace(crypto,"").replace('\'',"").replace('USD',"").replace(':',"").strip(),
    color=discord.Colour.teal())
    await discmessage.channel.send(embed=masked_crypto)        

client.run('INSERT TOKEN')