from project.api.todo import register_api
from project.database import db, app


def create_app():
    # set up extensions
    db.init_app(app)
    register_api()
