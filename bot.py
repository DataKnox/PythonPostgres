import os
from dotenv import load_dotenv
import discord
import time
import random
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
from sqlalchemy import create_engine

db_name = 'postgres'
db_user = 'postgres'
db_pass =  os.getenv('DBPASS')
db_host = 'db'
db_port = '5432'

# Connecto to the database
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
client.run(TOKEN)
