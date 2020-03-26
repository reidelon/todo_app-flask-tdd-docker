import json


def test_todo(test_app):
    client = test_app.test_client()
    resp = client.get('/todo')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'todo' in data['message']
    assert 'success' in data['status']
