import discord
from discord.ext import commands
import subprocess

TOKEN = 'Insert Token Here'

description = '''SquidBot in Python'''
bot = commands.Bot(command_prefix='.', description=description)

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print("ID : " + bot.user.id)
    print('------')


@bot.command()
async def hello():
    """Says world"""
    await bot.say("world !")
    
async def is_owner(ctx):
    return ctx.author.id == 263670024391229440

@bot.command()
@commands.check(is_owner)
async def reboot():
    """Reboot bot"""
    await bot.say("Redémarrage en cours")
    print("Redémarrage en cours")
    subprocess.call("./start.sh", shell=True)

bot.run(TOKEN)
