from project.database import db


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    state = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, name, state):
        self.name = name
        self.state = state
