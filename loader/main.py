import os
import json
import requests
from sqlalchemy import create_engine, exc
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
role_id = os.getenv('ROLE_ID')
while True:
    print("was true")
    try:
        con = db.connect()
        response = requests.get(
            f"https://api.matrica.io/v1/snapshot/role/{role_id}?apiKey={matrica_key}").json()
        for r in response:
            wallet = r['id']
            for n in r['nfts']:
                nft_id = n['id']
                sql = f"INSERT INTO hhsnap (wallet,token) VALUES ('{wallet}','{nft_id}')"
                print(sql)
                try:
                    con.execute(sql)
                except (Exception, exc.DatabaseError) as error:
                    print(error)
    except (Exception, exc.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()
    sleep(10)
