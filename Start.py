import requests
import time
import sys
import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

with open('token.txt', 'r') as file:
    token = file.read()
print(token)
os.system("cls")
#Colors
red = "\u001b[31;1m"
blue = "\u001b[34;1m"
green = "\u001b[32;1m"
res = "\u001b[0m"
purple = "\u001b[45;1m"

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
        messageoutput = blue + '[' + res + '{0.guild}'.format(message) + blue + ' | ' + res + '{0.author}'.format(message) + blue + ']: ' + res + '{0.content}'.format(message)
        print(messageoutput)
        if message.author != client.user:
            return

        if message.content.startswith('.playdate'):
            a_file = open("playdatelyrics.txt")

            lines = a_file.readlines()
            for line in lines:
                print(line)
                await message.channel.send(line)

@client.event
async def on_message_delete(message):
        messagedelete = red + '[' + res + '{0.guild}'.format(message) + red + ' | ' + res + '{0.author}'.format(message) + red + ']: ' + res + '{0.content}'.format(message)
        print(messagedelete)
	

client.run(token, bot=False)

