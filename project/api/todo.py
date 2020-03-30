from flask_rest_jsonapi import ResourceList, ResourceDetail, Api
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema
from project.models.todo import Todo
from project.database import db


class TodoSchema(Schema):
    class Meta:
        type_ = 'todo'
        self_view = 'todo_detail'
        self_view_kwargs = {'id': '<id>'}

    id = fields.Integer(dump_only=True)
    name = fields.Str()
    done = fields.Bool()


# Create resource managers
class TodoList(ResourceList):
    schema = TodoSchema
    data_layer = {'session': db.session,
                  'model': Todo}


class TodoDetail(ResourceDetail):
    schema = TodoSchema
    data_layer = {'session': db.session,
                  'model': Todo}


def register_api(app):
    api = Api(app)
    db.create_all(app=app)
    api.route(TodoList, 'todo_list', '/todos')
    api.route(TodoDetail, 'todo_detail', '/todos/<int:id>')
