import requests
#import pandas as pd
resposta = requests.get('https://pokeapi.co/api/v2/pokemon/charmander')

#pkm_df = pd.DataFrame(data, columns=['Nome', 'Type1', 'Type2', 'HP', 'Attack', 'Defense', 'Img'])
def main():
    global poke
    pokemon = str(input('Pokémon: '))
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    res = requests.get(api)
    poke = res.json()
    pegarNome(poke)
    pegarTipo(poke)
    
def pegarNome(poke):
    print(f'Nome: {poke["name"].upper()}')

def pegarTipo(poke):
    print('Tipo:', end=" ")
    for i in poke['types']:
        print(i['type']['name'].upper(), end=" ")

if __name__ == '__main__':
    main()






