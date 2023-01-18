import os
import requests
from sqlalchemy import create_engine, exc
from dotenv import load_dotenv
from time import sleep

load_dotenv()

db_name = os.getenv('DBNAME')
db_user = os.getenv('DBUSER')
db_pass = os.getenv('DBPASS')
db_host = os.getenv('DBHOST')
db_port = '5432'
matrica_key = os.getenv('MATRICAKEY')

db_string = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
db = create_engine(db_string)
role_id = os.getenv('ROLE_ID')
while True:
    try:
        con = db.connect()
        response = requests.get(
            f"https://api.matrica.io/v1/snapshot/role/{role_id}?apiKey={matrica_key}").json()
        for r in response:
            wallet = r['id']
            get_user = f"SELECT discordid FROM hhuser WHERE wallet='{wallet}'"
            try:
                if con.execute(get_user).first() == None:
                    user = requests.get(
                        f"https://api.matrica.io/v1/wallet/{wallet}?apiKey={matrica_key}").json()
                    isql = f"INSERT INTO hhuser (wallet, discordid) VALUES ('{wallet}','{user['discordId']}')"
                    try:
                        con.execute(isql)
                    except (Exception, exc.DatabaseError) as error:
                        print(error)
                else:
                    print('was not none')
            except (Exception, exc.DatabaseError) as error:
                print(error)
            for n in r['nfts']:
                nft_id = n['id']
                sql = f"INSERT INTO hhsnap (wallet,token) VALUES ('{wallet}','{nft_id}')"
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
