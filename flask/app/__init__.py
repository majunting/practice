from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# # another straightaway method to add configurations (not recommended)
# app.config['SECRET_KEY'] = 'secret_key'

from app import routes