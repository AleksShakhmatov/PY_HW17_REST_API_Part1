import requests


def test_get_not_found_user(base_url):
    response = requests.get(base_url + '/api/users/23')
    assert response.status_code == 404
    assert response.json() == {}
