import requests
from collections import defaultdict

data = defaultdict(list)
pokemon = ['ditto', 'snorlax']
base = 'https://pokeapi.co/api/v2/'
for p in pokemon:
    d = requests.get(base + f"pokemon/{p}/")
    for move in d.json()['moves']:
        data[p].append(move['move']['name'])
print(data)