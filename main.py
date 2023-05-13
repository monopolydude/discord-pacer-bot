import pytesseract
import PIL.Image
import discord
import requests
from io import BytesIO
import mysql.connector
from mysql.connector import Error

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
                text = text.split('\n')
                indices = [i for i, s in enumerate(text) if 'distance' in s]
                if (len(indices) != 0):
                    print(text[indices[0]])
                    print(text[indices[0] + 1])
                guild = message.guild.id
                try:
                    connection = mysql.connector.connect(host='localhost',
                                                         database='pacer_bot',
                                                         user='root',
                                                         password='root')
                    createTable = """CREATE TABLE DB_""" + str(guild) + """(
                                User varchar(250) NOT NULL,
                                RunDate datetime NOT NULL,
                                Distance DECIMAL(10,2) NOT NULL,
                                Time int NOT NULL,
                                Primary Key (User, RunDate))"""


                    cursor = connection.cursor()
                    result = cursor.execute(createTable)
                    print("Guild (" + str(guild) + ") Table created successfully")
                except mysql.connector.Error as error:
                    print("Failed to create table in MySQL: {}" .format(error))
                if (len(indices) != 0):
                    await message.channel.send(text[indices[0] + 1])

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

client = MyClient(intents=intents)
client.run("TOKEN HERE")
