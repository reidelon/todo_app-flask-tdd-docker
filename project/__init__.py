from flask import Flask, jsonify
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList, ResourceRelationship
import os
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)


# model
class User(db.Model):  # new
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class Todo(ResourceList):
    def get(self):
        return {
            'status': 'success',
            'message': 'todo!'
        }


api.route(Todo, 'todo_list', '/todo')
