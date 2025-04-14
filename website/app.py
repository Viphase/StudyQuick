from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
URL = os.getenv("URL")

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
