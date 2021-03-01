import discord
from discord.ext import commands
from discord import Embed
import random
from discord.utils import get
import youtube_dl as ytdl
import nacl.secret
import nacl.utils
import nacl.pwhash
import asyncio
import os
import sqlite3

client = commands.Bot(command_prefix = '#')

@client.event
async def on_ready():
    activity = discord.Game(name="Type #slavipomosht")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Slavi e gotov za robstvo')

@client.command()
async def slavipomosht(ctx):
    embedVar = Embed(title="Zdraveite priqteli", description="dnes shte obqvqvame drug voinata vurhu cvetnokojite", color=0xe0cd88)
    embedVar.add_field(name="#slavi", value="tova sum az", inline=False)
    embedVar.add_field(name="#bonus", value="poluchavate malko bonusche ot men =)", inline=False)
    await ctx.send(embed=embedVar)

@client.command()
async def bonus(ctx):
    await ctx.send("v guza ti ima konus")
    kur = discord.Embed()
    kur.set_image(url="https://i.ytimg.com/vi/lIGIypj9KPk/maxresdefault.jpg")
    await ctx.send(embed=kur)

@client.command()
async def slavi(ctx):
    db = sqlite3.connect("slavi.sqlite")
    cur = db.cursor()
    i = random.randint(1, 43)
    i = str(i)
    cur.execute(f"SELECT slavi.url FROM slavi WHERE slavi._id = {i}")
    snimka = cur.fetchall()
    snimka = snimka[0]
    snimka = snimka[0]
    cur.close()
    slav40 = discord.Embed()
    slav40.set_image(url=snimka)
    await ctx.send(embed=slav40)
    
@client.command(pass_context=True)
async def zdraveite(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    
    await ctx.send(f"zdraveite '{channel}'")
    voice.play(discord.FFmpegPCMAudio("slavi.mp3"))

@client.command(pass_context=True)
async def chao(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients)
    voice.play(discord.FFmpegPCMAudio("chao.mp3"))
    await asyncio.sleep(2)
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f"chao '{channel}'")
    else:
        print("ne sum vuv voicechannel retard")
        await ctx.send("ne sum vuv voice channel retard")

client.run('ODE1NzEwMjIwNTQ1Njg3NjMy.YDwXVw.3RV5zUuRkYjxdf3Wt2v0hV0nV6c')
