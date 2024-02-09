import pytest
import requests

@pytest.fixture
def yandex_token():
    return 'не нашёл токен, есть способ только через https://oauth.yandex.ru/, но нужно создавать приложение'

def create_folder(token, folder_name):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': folder_name}
    response = requests.put(url, headers=headers, params=params)
    return response

def check_folder_exists(token, folder_name):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': folder_name}
    response = requests.get(url, headers=headers, params=params)
    return response.status_code == 200

@pytest.mark.positive
def test_create_folder_success(yandex_token):
    folder_name = 'test_folder'
    response = create_folder(yandex_token, folder_name)
    assert response.status_code == 201
    assert check_folder_exists(yandex_token, folder_name)

@pytest.mark.negative
def test_create_folder_without_auth():
    folder_name = 'test_folder'
    response = create_folder('', folder_name)
    assert response.status_code in [401, 403]
