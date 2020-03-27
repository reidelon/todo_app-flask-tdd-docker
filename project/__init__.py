from flask import Flask
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList, ResourceRelationship
import os
from flask_sqlalchemy import SQLAlchemy
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    state = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, name, state):
        self.name = name
        self.state = state


db.create_all()


# Create logical data abstraction (same as data storage for this first example)
class TodoSchema(Schema):
    class Meta:
        type_ = 'todo'
        self_view = 'todo_detail'
        self_view_kwargs = {'id': '<id>'}

    id = fields.Integer(dump_only=True)
    name = fields.Str()
    state = fields.Bool()


# Create resource managers
class TodoList(ResourceList):
    schema = TodoSchema
    data_layer = {'session': db.session,
                  'model': Todo}


class TodoDetail(ResourceDetail):
    schema = TodoSchema
    data_layer = {'session': db.session,
                  'model': Todo}


api.route(TodoList, 'todo_list', '/todos')
api.route(TodoDetail, 'todo_detail', '/todos/<int:id>')