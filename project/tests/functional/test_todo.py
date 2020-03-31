import json


def test_list_todo(test_app, test_database):
    client = test_app.test_client()
    todo_name = 'tarea'
    done = False
    count_todo = 10
    create_in_done_or_todo(client, done, todo_name, count_todo)
    resp = client.get(
        '/todos'
    )
    assert resp.status_code == 200
    data = json.loads(resp.data.decode())
    assert len(data['data']) == count_todo


def test_add_todo(test_app, test_database):
    client = test_app.test_client()
    todo_name = "comer1"
    data, self_url, resp = create_todo(client, todo_name)
    assert resp.status_code == 201
    assert todo_name in data['data']['attributes']['name']


def test_delete_todo(test_app, test_database):
    client = test_app.test_client()
    data, self_url, resp = create_todo(client, "comer")
    resp = client.delete(
        self_url,
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'Object successfully deleted' in data['meta']['message']


def test_update_todo(test_app, test_database):
    client = test_app.test_client()
    todo_name = "comer"
    data, self_url, resp = create_todo(client, todo_name)
    resp = client.patch(
        self_url,
        data=json.dumps({
            "data": {
                "type": "todo",
                "id": int(self_url.split('/')[-1]),
                "attributes": {
                    "name": "jamar"
                }
            }
        }),
        content_type='application/json',
    )
    assert resp.status_code == 200
    assert todo_name in data['data']['attributes']['name']


def test_filter_todo_in_done(test_app, test_database):
    client = test_app.test_client()
    # True means done
    done = True
    done_name = "dormir"
    count_done = 6
    create_in_done_or_todo(client, done, done_name, count_done)
    todo_name = "comer"
    done = False
    count_todo = 1
    create_in_done_or_todo(client, done, todo_name, count_todo)
    filter = "true"
    resp = client.get(
        "todos?filter[done]=" + filter,
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    dormir_list = [item for item in data['data'] if
                   item['attributes']['name'] == done_name and item['attributes']['done']]
    assert resp.status_code == 200
    assert len(dormir_list) == count_done


def test_filter_todo_in_todo(test_app, test_database):
    client = test_app.test_client()
    # True means done
    done = True
    done_name = "cazar"
    count_done = 6
    create_in_done_or_todo(client, done, done_name, count_done)
    todo_name = "salvar"
    done = False
    count_todo = 10
    create_in_done_or_todo(client, done, todo_name, count_todo)
    filter = "false"
    resp = client.get(
        "todos?filter[done]=" + filter,
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    dormir_list = [item for item in data['data'] if
                   item['attributes']['name'] == todo_name and item['attributes']['done'] is False]
    assert resp.status_code == 200
    assert len(dormir_list) == count_todo


def create_in_done_or_todo(client, done, todo_name, count):
    for item in range(0, count):
        create_todo(client, todo_name, done=done)


def create_todo(client, todo_name, done=False):
    resp = client.post(
        '/todos',
        data=json.dumps({"data": {"type": "todo", "attributes": {"name": todo_name, "done": done}}}),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    return data, data['data']['links']['self'], resp
