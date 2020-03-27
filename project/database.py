from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)
# instantiate the db
db = SQLAlchemy(app)
