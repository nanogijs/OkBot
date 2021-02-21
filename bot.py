import discord
client = discord.Client()
import random
import time


masked_link_embed = discord.Embed(
    title = "Heared you guys talking about my friend Rick",
    description='[He is awesome, just see this!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)',
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
                n = random.randint(0,100)
                print(n)
                if n <= 4:
                 await message.channel.send('Ok rage mode activated!')
                 for x in range(0, 10):
                   await message.channel.send('Ok')
                   time.sleep(0.5)

    if message.content.lower() == "cyka":
            await message.channel.send('blyat')
            print('blyat send!')
        
    if message.content.lower()== 'blyat':
            await message.channel.send('kiska')
            print('blyat send!')
    
    if message.content.lower()== 'sander':
            await message.channel.send('Sander is kast')
            print('Sander send!') 
    if message.content.lower()== 'kast':
            await message.channel.send('kast? Ahhh, You mean Sander!')
            print('kast send!')   
    if message.content.lower() == 'hotel':
            await message.channel.send('Trivago')
            print('hotel send!')   
    if message.content.lower() == 'hentai':
            await message.channel.send('Yes Senpai')
            print('hentai send!')
    if "rick" in message.content.lower():
            await message.channel.send(embed=masked_link_embed)
    if message.content.lower() == 'oke':
           await message.channel.send('Oke')
    
    #N word filters Line 57 to 93
    if 'nigger' in message.content.lower():
            await message.delete()
            print("n word deleted")
    if 'nigg3r' in message.content.lower():
            await message.delete()
            print("n word deleted")         
    if 'niger' in message.content.lower():
            await message.delete()
            print("n word deleted")   
    if 'nig3r' in message.content.lower():
            await message.delete()
            print("n word deleted")   
    if 'niggar' in message.content.lower():
            await message.delete()
            print("n word deleted")   
    if 'nigar' in message.content.lower():
            await message.delete()
            print("n word deleted")   
    if 'nigga' in message.content.lower():
            await message.delete()
            print("n word deleted")
    if 'niga' in message.content.lower():
            await message.delete()
            print("n word deleted")   
    if 'n1gg3r' in message.content.lower():
            await message.delete()
            print("n word deleted")   
    if 'n1gga' in message.content.lower():
            await message.delete()
            print("n word deleted")   
    if 'n1gg3r' in message.content.lower():
            await message.delete()
            print("n word deleted")   
    if 'n1ga' in message.content.lower():
            await message.delete()
            print("n word deleted")


            
            


client.run('#insert your own token here')