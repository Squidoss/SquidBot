#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import os
import sys

#Import token from file
with open('../token.txt', 'r') as file:
    TOKEN = file.read().rstrip("\n")

description = '''SquidBot in Python, by Squidoss'''
client_prefix = (".", "/")
client = commands.Bot(command_prefix=client_prefix, description=description)
client.remove_command('help')

@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print("ID : " + client.user.id)
    print("Token : " + TOKEN)
    print('------')
    print('Servers connected to:')
    for server in client.servers:
        print(server.name)
    print('------')
    await client.change_presence(game=discord.Game(name='humans...', type=3))

    initModules()

@client.event
async def on_member_join(member):
    await client.send_message(member, "Welcome to the server !")

@client.event
async def on_member_leave(member):
    await client.send_message(member, "Bye")

@client.event
async def on_message(message):
    await client.process_commands(message)
    for mention in message.mentions:
        if mention.id == client.user.id:
            await client.send_message(message.channel,
            "In order to get any help, type .help. For further informations, ask @Squidoss or any other programmer.")

# @client.event
# async def on_error(event, *args, **kwargs):
#     print('ERRRRROOOOOOOOOOOOORRRRRRRRRRRRRR!!!!!!!!!!!!!!')
#     error_channel = client.get_channel('555445252375183380')
#     await client.send_message(error_channel, 'Event : {}\nArgs : {}\nKwargs : {}'.format(event, args, kwargs))
#     print(event)
#     print(args)
#     print(kwargs)
# 
# @client.event
# async def on_command_error(ctx, error):
#     print('ERRRRROOOOOOOOOOOOORRRRRRRRRRRRRR!!!!!!!!!!!!!!')
#     error_channel = client.get_channel('555445252375183380')
#     await client.send_message(error_channel, 'ctx : {}\nError : {}'.format(ctx, error))
#     print(ctx)
#     print(error.__class__.__name__)

@client.command()
async def error():
    """Creates error"""
    error = 5/0

#Commands

@client.command(pass_context=True)
async def help(ctx, *args):
    """General help"""
    if 'all' in args or len(args)==0:
        embed=discord.Embed(title="List of general commands", description=
        "Type .help all to show help about every active module, or type help [module] to show further information",
        color=0x00ff00)
        embed.add_field(name="--------------------" , value="--------------------", inline=False)
        embed.add_field(name=".help", value="Returns this message", inline=False)
        embed.add_field(name=".hello", value="Replies world !", inline=False)
        embed.add_field(name=".info", value="Give information and IDs about this server", inline=False)
        embed.add_field(name=".github", value="Give the github's link of SquidBot", inline=False)
        embed.set_footer(text="SquidBot, the best half-squid half-robot bot in the universe.")

        await client.say(embed=embed)

@client.command()
async def hello():
    """Says world"""
    await client.say("world !")

@client.command()
async def github():
    """Give github's link"""
    await client.say("https://github.com/Squidoss/SquidBot")

@client.command(pass_context=True)
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

    await client.say(
        "```Markdown\n"
        "Server name : {}\n"
        "Server ID : <{}>\n"
        "Server owner : {} <{}>\n\n"
        "Server roles : \n {} \n"
        "```"
        .format(server_name, server_id, server_owner, server_owner_id, roles_list))

@client.command(pass_context=True)
async def poll(ctx, *args):
    """Poll commands"""
    length = len(args)
    if length == 0:
        await client.say("Insert arguments, type .help for further informations")
    elif args[0] == "create":
        poll_msg = await client.say("**Poll :** *{} {} vs {} {}*".format(args[1], args[2], args[3], args[4]))
        await client.add_reaction(poll_msg, args[2])
        await client.add_reaction(poll_msg, args[4])

        end_msg = await client.wait_for_message(author=ctx.message.author, content=".poll stop")
        poll_msg = await client.get_message(ctx.message.channel, poll_msg.id)
        choice1 = 0
        choice2 = 0
        for reaction in poll_msg.reactions:
            if reaction.emoji == args[2]:
                choice1 = reaction.count
            else:
                choice2 = reaction.count
        if choice1 > choice2:
            await client.say(args[2])
        elif choice2 > choice1:
            await client.say(args[4])
        else:
            await client.say("Égalité")

@client.command()
async def load(extension):
    """Load extension"""
    try:
        print('Loaded {}'.format(extension))
        client.load_extension(extension)
    except Extension as error:
        print('Extension {} cannot be loaded. [{}]'.format(extension, error))
        client.say('Extension {} cannot be loaded. [{}]'.format(extension, error))

@client.command()
async def unload(extension):
    """Unload extension"""
    try:
        print('Unloaded {}'.format(extension))
        client.unload_extension(extension)
    except Extension as error:
        print('Extension {} cannot be unloaded. [{}]'.format(extension, error))
        client.say('Extension {} cannot be unloaded. [{}]'.format(extension, error))



def initModules():
    """Initialize modules"""
    modulesList = []
    sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'modules'))
    for module in os.listdir('./modules'):
        if module.endswith('.py'):
            module = module.replace(".py", "")
            module = ''.join(('modules.', module))
            modulesList.append(module)

    if __name__ == '__main__':
        for extension in modulesList:
            try:
                client.load_extension(extension)
                print("{} loaded.".format(extension))
            except extension as error:
                print('Extension {} cannot be loaded. [{}]'.format(extension, error))

client.run(TOKEN)
