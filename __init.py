import itertools
from itertools import cycle
from random import randint
from itertools import filterfalse
from logging import BASIC_FORMAT
from typing import Text
import discord
from discord import reaction
from discord import message
from discord import channel
from discord import voice_client
from discord.ext import commands
from discord.ext.commands.core import has_permissions
from discord.message import convert_emoji_reaction
from discord.user import ClientUser
import random
from discord.utils import get
import os
import json
import random
import youtube_dl
from youtube_dl import *

TOKEN = '<REDACTED>'

client = commands.Bot(command_prefix=' ')


@client.event
async def on_ready():
    print('<put something here>')
    await client.change_presence(activity=discord.Game(
    name= "<put something here>"))


@client.command()
async def play(ctx, url):
    user = ctx.message.author
    channel = ctx.message.author.voice.channel
    voice_state = ctx.message.author.voice
    if voice_state is None:
        play_embed = discord.Embed(
            title=f"{user.name}, there was an error",
            description=
            f'You are not in a voice channel, therefore, you cannot invoke the `t.play` command',
            color=discord.Color.from_rgb(219, 54, 54))
        await ctx.reply(embed=play_embed, mention_author=True)
    else:
        play_embed = discord.Embed(title=f"{user.name}, playing music",
                                   description=f'Now playing:\n\n{url}',
                                   color=discord.Color.from_rgb(167, 241, 242))
        await ctx.reply(embed=play_embed, mention_author=True)
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        FMMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1',
            'options': '-vn'
        }
        YDL_OPTIONS = {'format': 'bestaudio'}
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(
                url2, **FMMPEG_OPTIONS)
            vc.play(source)


@client.command()
async def pause(ctx):
    user = ctx.message.author
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    try:
        if voice.is_playing():

            play_embed = discord.Embed(title=f"{user.name}, pausing",
                                       description=f'Pausing music',
                                       color=discord.Color.from_rgb(
                                           167, 241, 242))
            await ctx.reply(embed=play_embed, mention_author=False)
            voice.pause()
    except:
        play_embed = discord.Embed(
            title=f"{user.name}, there was an error",
            description=f'No audio is currently playing',
            color=discord.Color.from_rgb(219, 54, 54))
        await ctx.reply(embed=play_embed, mention_author=False)


@client.command()
async def resume(ctx):
    user = ctx.message.author
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    try:
        if voice.is_paused():

            play_embed = discord.Embed(title=f"{user.name}, resuming",
                                       description=f'Resuming music',
                                       color=discord.Color.from_rgb(
                                           167, 241, 242))
            await ctx.reply(embed=play_embed, mention_author=False)
            voice.resume()
    except:
        play_embed = discord.Embed(title=f"{user.name}, there was an error",
                                   description=f'Audio is not paused',
                                   color=discord.Color.from_rgb(219, 54, 54))
        await ctx.reply(embed=play_embed, mention_author=False)



@client.command()
async def stop(ctx):
    user = ctx.message.author
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    play_embed = discord.Embed(
          title = f'{user.name}, stoping', 
          description ='the audio has stoped playing',
          color=discord.Color.from_rgb(167, 241, 242)
        )
    await ctx.reply(embed= play_embed) 


        
@client.command()
async def leave(ctx):
    user = ctx.message.author
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
        play_embed = discord.Embed(
          title = f'{user.name}, leaving', 
          description ='i have left the VC',
          color=discord.Color.from_rgb(167, 241, 242)
        )
        await ctx.reply(embed= play_embed) 
     
        
        
        
 





client.run(TOKEN)

# main coder : @Teh llama#4638
# second coder/owner : @TR ASH#7081
# lol
