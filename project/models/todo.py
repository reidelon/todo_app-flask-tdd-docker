from project.database import db


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    done = db.Column(db.Boolean(), default=False, nullable=False)

    def __init__(self, name, done):
        self.name = name
        self.done = done
