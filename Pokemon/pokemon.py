import requests
#import pandas as pd
resposta = requests.get('https://pokeapi.co/api/v2/pokemon/charmander')

#pkm_df = pd.DataFrame(data, columns=['Nome', 'Type1', 'Type2', 'HP', 'Attack', 'Defense', 'Img'])

nome = []
def main():
    global pokemon
    pokemon = str(input('Pokémon: '))
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    res = requests.get(api)
    poke = res.json()
    pegarNome(poke)
    pegarTipo(poke)
    

def pegarTipo(poke):
    print(f'Tipo {pokemon}:')
    for i in poke['types']:
        print(i['type']['name'])

def pegarNome(poke):
    print(f'Nome')
    nome.append(poke['name'])

if __name__ == '__main__':
    main()






