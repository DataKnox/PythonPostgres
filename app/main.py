from fastapi import FastAPI
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()
db_name = 'postgres'
db_user = 'postgres'
db_pass = os.getenv('DBPASS')
db_host = 'db'
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
def testquery():
    df = pd.read_sql("SELECT table_name FROM information_schema.tables", con)
    return df.to_json(orient="records")