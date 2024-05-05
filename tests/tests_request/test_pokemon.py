import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type':'application/json','trainer_token':'TOKEN_USER'}
PATH_POKEMONS = '/pokemons'

def test_status_code_pokemons():
    response = requests.get(url = f'{URL}{PATH_POKEMONS}', headers = HEADERS, params= {"in_pokeball": 1})
    assert response.status_code== 200

PATH_TRENERS = '/trainers'

def test_status_code_trainers():
    response2 = requests.get(url = f'{URL}{PATH_TRENERS}', headers = HEADERS, params= {"trainer_id": 2829})
    assert response2.status_code== 200

def test_part_of_response():
    response2 = requests.get(url = f'{URL}{PATH_TRENERS}', headers = HEADERS, params= {"trainer_id": 2829})
    assert response2.json()['data'][0]['trainer_name'] == 'Каспер'