from fastapi import Depends, FastAPI
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from fastapi.security.api_key import APIKey
import auth
load_dotenv()
app = FastAPI()
db_name = os.getenv('DBNAME')
db_user = os.getenv('DBUSER')
db_pass = os.getenv('DBPASS')
db_host = os.getenv('DBHOST')
db_port = '5432'

# Connecto to the database
db_string = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
db = create_engine(db_string)
con = db.connect()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/test")
async def testquery(api_key: APIKey = Depends(auth.get_api_key)):
    df = pd.read_sql("SELECT * FROM hhsnap", con)
    return df.to_json(orient="records")
