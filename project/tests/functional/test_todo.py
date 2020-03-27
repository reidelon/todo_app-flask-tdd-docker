import json

base_url = 'http://localhost:5000/'
headers = {'Accept': 'application/vnd.api+json', 'Content-Type': 'application/vnd.api+json'}


def test_list_todo(test_app, test_database):
    client = test_app.test_client()
    resp = client.get(
        '/todos'
    )
    assert resp.status_code == 200


def test_add_todo(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/todos',
        data=json.dumps({"data": {"type": "todo", "attributes": {"name": "merienda", "state": True}}}),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'merienda' in data['data']['attributes']['name']
