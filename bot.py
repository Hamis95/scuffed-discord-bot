import discord
from discord.ext import commands                    #I run this bot from a raspberry pi 4
from discord.utils import get
import youtube_dl
from discord.ext import commands
import os
client = commands.Bot(command_prefix = '.') #prefix is the symbol you put before every command. "#¤%&&//)))")¤()¤"_;_: you can choose pretty much anything.



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Hentai Sniper')) #Write here the game you want the bot to appear to be playing
    print('botti valmis.') #the message you get when the bot is ready and functional


@client.command()
async def onnistuu(ctx):
    await ctx.send(file=discord.File('/home/pi/Desktop/bottifile/onnistuu.jpg')) #The path to a file you want the bot to sent to your channel you can also use url

@client.command()
async def apustaja(ctx):
    await ctx.send(file=discord.File('/home/pi/Desktop/bottifile/apustaja.jpg'))

@client.command()
async def commands(ctx):
    await ctx.send('"onnistuu, apustaja, jumala, imppu, joulu, bang, hobby"')

@client.command()
async def jumala(ctx):
    await ctx.send(file=discord.File('/home/pi/Desktop/bottifile/jumala.jpg'))

@client.command()
async def imppu(ctx):
    await ctx.send(file=discord.File('/home/pi/Desktop/bottifile/petturi.jpg'))

@client.command()
async def joulu(ctx):
    await ctx.send(file=discord.File('/home/pi/Desktop/bottifile/joulu.jpg'))

@client.command()
async def bang(ctx):
    await ctx.send(file=discord.File('/home/pi/Desktop/bottifile/bang.jpg'))

@client.command()
async def hobby(ctx):
    await ctx.send(file=discord.File('/home/pi/Desktop/bottifile/hobby.jpg'))

@client.command(pass_context=True)
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)                                    #   <============= channel joining feature (no real usage with this code)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

@client.command(pass_context=True)
async def leave(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)                  # <===================== this is how you make the bot leave after you realise it does not play anything
    if voice.is_connected():
        await voice.disconnect()




@client.command(pass_context=True)
async def play(ctx, url):
    server = server.message.server
    voice_client =client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

















client.run('xXxxxXXXXXXXXxxxXxxxxXxxXXXxxxxxxXX')  # <============ put your bot token here and invite it to your channel
