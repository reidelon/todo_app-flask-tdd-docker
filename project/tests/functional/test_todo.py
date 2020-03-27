import json


def test_todo(test_app):
    client = test_app.test_client()
    resp = client.get('/todos')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'todo' in data['message']
    assert 'success' in data['status']


def test_add_todo(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/todos',
        data=json.dumps({
            'name': 'comer',
            'state': False
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'comer' in data['attributes']['name']