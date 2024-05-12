import requests

HOST = 'https://api.pokemonbattle.me/v2/'
TOKEN = 'введите токен'
HEADER = {'Conten-Type':'application/json', 'trainer_token':TOKEN}

body_creation_pokemon = {
    'name': 'Бульбазавр',
    'photo': 'https://dolnikov.ru/pokemons/albums/001.png'
}

body_change_poremon = {
    'pokemon_id': '17814',
    'name': 'Сквиртл',
    'photo': 'https://dolnikov.ru/pokemons/albums/007.png'
}

body_catch_pokemon = {
    "pokemon_id": "26369"
}

response_create = requests.post(url = f'{HOST}pokemons', headers = HEADER, json = body_creation_pokemon)
print(response_create.text)

change_pokemon = requests.put(url = f'{HOST}pokemons', headers = HEADER, json = body_change_poremon)
print(change_pokemon.text)

catch_pokemon = requests.post(url = f'{HOST}trainers/add_pokeball', headers = HEADER, json = body_catch_pokemon)
print(catch_pokemon.text)
