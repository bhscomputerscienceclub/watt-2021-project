
from flask import Flask
from config import Config
import os
app = Flask(__name__,
template_folder='../templates')
app.config.from_object(Config)
app.secret_key = "aaa" #os.urandom(10)
from app.Score import init
init()
from app import routes

