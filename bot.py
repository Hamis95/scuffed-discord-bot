import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
from discord.ext import commands
import os
client = commands.Bot(command_prefix = '.')



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Hentai Sniper'))
    print('botti valmis.')


@client.command()
async def onnistuu(ctx):
    await ctx.send(file=discord.File('/home/pi/Desktop/bottifile/onnistuu.jpg'))

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
        await voice.move_to(channel)
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
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()




@client.command(pass_context=True)
async def play(ctx, url):
    server = server.message.server
    voice_client =client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

















client.run('Njc2OTIwMzAxNjg2MDk1ODky.XkMtKA.djS8fqMagBMgt-qzXpZd_Vawthk')
