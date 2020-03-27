from project import create_app
from project import app, db


if __name__ == '__main__':
    create_app()
    app.run(host='0.0.0.0')
