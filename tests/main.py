import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type':'application/json','trainer_token':'TOKEN_USER'}
PATH_CREATE = '/pokemons'

BODY = {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url= f'{URL}{PATH_CREATE}', headers = HEADERS, json = BODY)

print(response.text)



POKEMON_ID = response.json()['id']
print(POKEMON_ID) 

BODY_NAME = {
    "pokemon_id": f"{POKEMON_ID}",
    "name": "generate"
}

response_name = requests.patch(url = f'{URL}{PATH_CREATE}', headers = HEADERS, json = BODY_NAME)

print(response_name.text)



PATH_INPOKEBALL = '/trainers/add_pokeball'

BODY_INPOKEBALL = {
    "pokemon_id": f"{POKEMON_ID}"
}

response_pokebol =requests.post(url = f'{URL}{PATH_INPOKEBALL}', headers = HEADERS, json = BODY_INPOKEBALL)

print(response_pokebol.text)
