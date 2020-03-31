# Todo APP

This is a `todo` REST-FULL API made following TDD

## Getting Started

git clone https://github.com/reidelon/todo_app-flask-tdd-docker.git

cd todo_app-flask-tdd-docker

docker-compose up --build

endpoints:

/todos

/todos/`X`

where `X` is the id of a todo

`Create`

POST /todos HTTP/1.1

Content-Type: application/vnd.api+json

Accept: application/vnd.api+json


{
  "data": {
    "type": "todo",
    "attributes": {
      "name": "walk",
      "done": false
    }
  }
}

`Read`

GET /todos HTTP/1.1

Accept: application/vnd.api+json

`Update`

PATCH /todos/`X` HTTP/1.1

Content-Type: application/vnd.api+json

Accept: application/vnd.api+json

{
  "data": {
    "type": "todo",
    "id": `X`,
    "attributes": {
      "name": "eat",
      "done": true
    }
  }
}

`Delete`

DELETE /todos/`X` HTTP/1.1

Accept: application/vnd.api+json

`Filter`

GET /todos?filter[done]=false HTTP/1.1

Accept: application/vnd.api+json

`Note` any other combination can be made for filtering [read here](https://flask-rest-jsonapi.readthedocs.io/en/latest/filtering.html)

### Prerequisites

[Docker](https://www.docker.com/)

## Running the tests

docker-compose exec web python -m pytest "project/tests"

### Break down into end to end tests

There are 6 functional test about and 3 unit test.

Functional test:
test_list_todo
test_add_todo
test_delete_todo
test_update_todo
test_filter_todo_in_done
test_filter_todo_in_todo

Unit test:
test_development_config
test_testing_config
test_production_config


## Technology

* [FLask](https://palletsprojects.com/p/flask/) - The web framework used.
* [Python 3.8](https://www.python.org/) - Programming Lenguage used.
* [Flask-Migrate](https://flask-migrate.readthedocs.io/) - An extension that handles SQLAlchemy database migrations for Flask applications using Alembic.
* [Flask-rest-jsonapi](https://flask-rest-jsonapi.readthedocs.io/) - An extension for Flask that adds support for quickly building REST APIs around the JSONAPI 1.0 specification.
* [Pytest](https://docs.pytest.org/) - Python testing tool.
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) - An extension for Flask that adds support for SQLAlchemy.
* [PostgreSQL](https://www.postgresql.org/) - Database Engine used.
* [Docker](https://www.docker.com/) - Container technology used.

## Authors

* **Reidel Lazaro Rodriguez Torres** - (https://github.com/reidelon)
