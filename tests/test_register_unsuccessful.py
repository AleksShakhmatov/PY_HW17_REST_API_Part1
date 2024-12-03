import json
import requests
from jsonschema import validate
from path import path


def test_post_register_unsuccessful(base_url):
    response = requests.post(base_url + '/api/register', data={"email": "sydney@fife"})
    body = response.json()
    schema = path('register_unsuccessful.json')
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'
    with open(schema) as file:
        f = file.read()
        validate(body, schema=json.loads(f))
