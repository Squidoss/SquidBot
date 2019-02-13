#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import subprocess
import os
import sys

file=open('../token.txt', 'r')
TOKEN = file.read().rstrip("\n")

description = '''SquidBot in Python'''
bot_prefix = (".",";",":","!")
bot = commands.Bot(command_prefix=bot_prefix, description=description)
bot.remove_command('help')

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print("ID : " + bot.user.id)
    print("Token : " + TOKEN)
    print('------')
    print('Servers connected to:')
    for server in bot.servers:
        print(server.name)
    print('------')
    await bot.change_presence(game=discord.Game(name='humans...', type=3))
    
@bot.event
async def on_member_join(member):
    await bot.send_message(member, "Hello")
    
@bot.event
async def on_member_leave(member):
    await bot.send_message(member, "Bye")

    
#Commands

@bot.command()
async def help():
    embed=discord.Embed(title="List of all commands", description="Type .help to show this message", color=0x00ff00)
    embed.set_author(name="SquidBot")
    embed.add_field(name="--------------------" , value="--------------------", inline=False)
    embed.add_field(name=".help", value="Returns this message", inline=False)
    embed.add_field(name=".hello", value="Replies world !", inline=False)
    embed.add_field(name=".info", value="Give information and IDs about this server", inline=False)
    embed.add_field(name=".github", value="Give the github's link of SquidBot", inline=False)
    embed.set_footer(text="SquidBot, the best half-squid half-robot bot.")
    await bot.say(embed=embed)
    
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
     
@bot.command(pass_context=True)
async def stop(ctx):
    """Turn bot off"""
    if ctx.message.author.id == '263670024391229440':
        await bot.say("Turning off...")
        print("Turning off...")
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
    
@bot.command(pass_context=True)
async def info(ctx):
    """Give server's infos"""
    server = ctx.message.author.server
    server_name = server.name
    server_id = server.id
    server_owner = server.owner.name
    server_owner_id = server.owner.id
    server_roles = server.roles
    roles_list = ''
    
    for role in server.roles:
        roles_list += "{} : <{}> \n".format(role.name, role.id)        
        
    await bot.say(
        "```Markdown\n"
        "Server name : {}\n"
        "Server ID : <{}>\n"
        "Server owner : {} <{}>\n\n"
        "Server roles : \n {} \n"
        "```"
        .format(server_name, server_id, server_owner, server_owner_id, roles_list))
    
    
    
    
    
#Voice commands

@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)

@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()
    

bot.run(TOKEN)
