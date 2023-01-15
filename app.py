from flask import Flask
import os
from dotenv import load_dotenv
import time
import random
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route("/")
def hello_world():
        return {
            "message": "hello world"
    }