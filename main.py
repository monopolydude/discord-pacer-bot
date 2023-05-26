import pytesseract
import PIL.Image
import discord
import requests
from io import BytesIO
import mysql.connector
from mysql.connector import Error
from databaseCalls import *

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.author == client.user:
            return
        if (len(message.attachments) == 1):
            if(message.attachments[0].size > 0):
                url = message.attachments[0].url
                response = requests.get(url)
                text = pytesseract.image_to_string(PIL.Image.open(BytesIO(response.content))).lower()
                #remove empty from list
                text = text.split('\n')
                text = list(filter(None, text))
                indices = [i for i, s in enumerate(text) if 'distance' in s]
                if (len(indices) != 0):
                    print(text)
                    print(text[indices[0]])
                    print(text[indices[0] + 1])
                guild = message.guild.id
                if (not(tableExists(guild))):
                    createRunnersTable(guild)




                if (len(indices) != 0):
                    await message.channel.send(text[indices[0] + 1])

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

client = MyClient(intents=intents)
client.run("MTEwNTY3ODU3MDY0MDExMzc4NA.Gic_mB.ITQk5aDQHDjQtsYl1dfmGSC1eR1bw7FMQ9X09Q")
#test
