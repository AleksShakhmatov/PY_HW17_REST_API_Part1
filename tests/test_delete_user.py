import requests


def test_delete_user(base_url):
    response = requests.delete(base_url + '/api/users', params='page=2')
    assert response.status_code == 204
    assert response.text == ''
