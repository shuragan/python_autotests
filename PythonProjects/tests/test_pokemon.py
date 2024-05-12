import requests
import pytest

HOST = 'https://api.pokemonbattle.me/v2/'
TOKEN = 'введите токен'
HEADER = {'Conten-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '1488'


def test_status_code():
    response = requests.get(url = f'{HOST}trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_id_trainer():
    response_get_id = requests.get(url = f'{HOST}trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get_id.json()['data'][0]['id'] == '1488'