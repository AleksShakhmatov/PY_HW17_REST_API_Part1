import json
import requests
from jsonschema import validate
from path import path


def test_post_create_user(base_url):
    response = requests.post(base_url + '/api/users', data={"name": "morpheus", "job": "leader"})
    body = response.json()
    schema = path('create_user.json')
    assert response.status_code == 201
    assert response.json()['name'] == 'morpheus'
    assert response.json()['job'] == 'leader'
    assert response.json()['id'] != ''
    assert response.json()['createdAt'] != ''
    with open(schema) as file:
        f = file.read()
        validate(body, schema=json.loads(f))


def test_delete_user(url, base_url):
    response = requests.delete(base_url + '/api/users', params='page=2')
    assert response.status_code == 204
    assert response.text == ''
