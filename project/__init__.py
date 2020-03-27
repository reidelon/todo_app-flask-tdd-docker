from project.api.todo import register_api
from project.database import db
from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    db.init_app(app)
    register_api(app)
    return app
