import discord
from discord.ext import commands
import subprocess

TOKEN = 'NTM2OTY3NzEyMTExNTkxNDMz.Dzykmw.J1nBswy-HqDTBu9yafoOUdAo_MU'

description = '''SquidBot in Python'''
bot = commands.Bot(command_prefix=':', description=description)

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print("ID : " + bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='being a bot'))


@bot.command()
async def hello():
    """Says world"""
    await bot.say("world !")
    
    
@bot.command(pass_context=True)
async def reboot(ctx):
    """Reboot bot"""
    if ctx.message.author.id == '263670024391229440':
        await bot.say("Redemarrage en cours")
        await bot.say("{} , mon maître adore.".format(ctx.message.author.mention))
        print("Redémarrage en cours")
        subprocess.call("./start.sh", shell=True)
        #sys.exit()
    else:
        await bot.say("Vous n'avez pas les droits")
        

bot.run(TOKEN)
