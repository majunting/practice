from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# # another straightaway method to add configurations (not recommended)
# app.config['SECRET_KEY'] = 'secret_key'

from app import routes