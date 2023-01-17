import os
import json
import requests
from sqlalchemy import create_engine
from dotenv import load_dotenv
from time import sleep

load_dotenv()

db_name = 'initdb'
db_user = os.getenv('DBUSER')
db_pass = os.getenv('DBPASS')
db_host = 'db'
db_port = '5432'
matrica_key = os.getenv('MATRICAKEY')
# Connecto to the database
db_string = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
db = create_engine(db_string)

while True:
    response = requests.get(
        f"https://api.matrica.io/v1/snapshot/role/936808864798617620?apiKey={matrica_key}").json()
    for r in response:
        print(f"wallet is {r['id']}")
        for n in r['nfts']:
            print(n['id'])
    sleep(10)
