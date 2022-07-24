# bot.py
import os
import random
from aiohttp.http import RESPONSES
import discord
from discord import message
from discord.ext import commands
from discord.utils import resolve_template
from dotenv import load_dotenv
from mcrcon import MCRcon as r
import datetime
import socket
import time
import subprocess



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix=';')

MC_PORT=25565
MC_SERVER_IP="127.0.0.1"
MC_RCON_PASSWD="beepboop"

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following guilds:\n'
        f'{guild.name}(id: {guild.id})'
    )
    member = await bot.fetch_user('176784920465768448')
    response=f'Brei-bot 2 has come online at {str(datetime.datetime.now())}\n'
    response=response+f'{bot.user} is connected to the following guilds:\n'
    response=response+f'{guild.name}(id: {guild.id})'
    channel = bot.get_channel(737408433015226422)
    await channel.send("```"+response+"```")
    print (response)


#*******************************************************************************
#COMMANDS
#*******************************************************************************

#===============================================================================
#ENTRY POINT
#RETURNS THE STATUS OF THE CURRENT RUNNING MC-SERVER
#===============================================================================
@bot.command(name='mc-server')
async def on_message(message, arg1):

    if arg1 == "status":
        
        if isServerUp() == 0:
            await message.send(issueCmd ("/list"))
        else:
            await message.send("The Minecraft Server is not currently active")
        
        return
    elif arg1 == "start":
        await message.send("Starting Minecraft Server...")

        if isServerUp() == 0:
            await message.send("Error: There is already a server running")
            return
        
        os.chdir("/server")
        args = ['/usr/bin/java', "-Xmx1024M", "-Xms1024M", "-jar", "server.jar", "nogui"]
        process = subprocess.Popen(args, stdin=subprocess.PIPE)

        return
    elif arg1 == "stop":
        await message.send("Shutting Down the Minecraft Server...")
        
        issueCmd("/stop")
        while isServerUp() == 0:
            time.sleep(5)

        await message.send("The Minecraft Server has stopped")

        
        return
    else:
        await message.send("Error command not found")


#===============================================================================

#END****************************************************************************



#*******************************************************************************
#FUNCTIONS
#*******************************************************************************

#===============================================================================
#isServerUp
#Return Codes: 
#   0 = server runnin
#   1 = server down
#===============================================================================
def isServerUp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((MC_SERVER_IP,MC_PORT))
    
    if result == 0:
        print ("CODE:",result,": SERVER IS RUNNING")
        return 0
    else:
        print ("CODE:",result,": SERVER IS NOT RUNNING")
        return 1
    sock.close()
#===============================================================================

#===============================================================================
#issueCmd
#===============================================================================
def issueCmd(cmd):
    with r(MC_SERVER_IP,MC_RCON_PASSWD) as mcr:
        resp = mcr.command(cmd)
        return resp
#===============================================================================




#===============================================================================
#UNDEFIED ERROR HANDLER
#===============================================================================
bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
#===============================================================================

#END****************************************************************************



bot.run(TOKEN)