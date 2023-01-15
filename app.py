from flask import Flask, jsonify
import os
from dotenv import load_dotenv
import time
import random
from sqlalchemy import create_engine

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify(hello="world")
