import requests

resposta = requests.get('https://pokeapi.co/api/v2/pokemon/charmander')

def main():
    global pokemon
    pokemon = str(input('Pokémon: '))
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    res = requests.get(api)
    poke = res.json()
    pegarTipo(poke)

def pegarTipo(poke):
    print(f'Tipo {pokemon}:')
    for i in poke['types']:
        print(i['type']['name'])

if __name__ == '__main__':
    main()






