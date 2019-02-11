#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import subprocess
import os

file=open('/home/squidoss/token.txt', 'r')
TOKEN = file.read().rstrip("\n")

description = '''SquidBot in Python'''
bot = commands.Bot(command_prefix=':', description=description)

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print("ID : " + bot.user.id)
    print("Token : " + TOKEN)
    print('------')
    await bot.change_presence(game=discord.Game(name='being a bot', type=1))

    
#Commands
    
@bot.command(pass_context=True)
async def reboot(ctx):
    """Reboot bot"""
    if ctx.message.author.id == '263670024391229440':
        await bot.say("Reboot in process...")
        print("Reboot in process")
        subprocess.call("./start.sh", shell=True)
        sys.exit()
    else:
        await bot.say("Access denied")
        
@bot.command()
async def hello():
    """Says world"""
    await bot.say("world !")
    
@bot.command()
async def github():
    """Give github's link"""
    await bot.say("https://github.com/Squidoss/SquidBot")

bot.run(TOKEN)
