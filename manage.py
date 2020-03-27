from project import create_app, register_api

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')
