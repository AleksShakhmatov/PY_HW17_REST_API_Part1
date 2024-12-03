import json
import requests
from jsonschema import validate
from path import path


def test_post_register_successful(base_url):
    response = requests.post(base_url + '/api/register', data={"email": "eve.holt@reqres.in", "password": "pistol"})
    body = response.json()
    schema = path('register_successful.json')
    assert response.status_code == 200
    assert response.json()['id'] != ''
    assert response.json()['token'] != ''
    with open(schema) as file:
        f = file.read()
        validate(body, schema=json.loads(f))
