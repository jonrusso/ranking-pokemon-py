import requests


f = 0


def pegarpokemon(poke):
    global f, m
    m = 0
    print('-=' * 15)
    print('essa é a lista de pokemons !!!!')
    for i in poke['pokemon']:
        url = (i['pokemon']['url'])
        api = url
        res = requests.get(api)
        poke = res.json()
        for i in poke['stats']:
            nome = str(i['stat']['name'])
            estatus = int(i['base_stat'])
            if nome == status:
                if f < estatus:
                    f = estatus
                    m = (poke['name'])
                    print(m)


def pegarpokemon3(poke):
    global f, m
    print('-=' * 15)
    print('essa é a lista de pokemons !!!!')
    for i in poke['pokemon']:
        url = (i['pokemon']['url'])
        api = url
        res = requests.get(api)
        poke = res.json()
        for i in poke['stats']:
            nome = str(i['stat']['name'])
            estatus = int(i['base_stat'])
            if nome == status:
                if f < estatus:
                    f = estatus
                    m = (poke['name'])
    print(m)


def pegarpokemon2(poke):
    for i in poke['stats']:
        print(i['stat']['name'], end=' ')
        print(i['base_stat'])


def main():
    global pokemon
    global status
    pokemon = str(input('insira o tipo do pokemon'))
    status = str(input('insira o status a ser procurado'))
    url = f'https://pokeapi.co/api/v2/type/{pokemon}'
    res = requests.get(url)
    poke = res.json()
    pegarpokemon(poke)


def main3():
    pokemon = str(input('insira o tipo do pokemon'))
    api = f'https://pokeapi.co/api/v2/type/{pokemon}'
    res = requests.get(api)
    poke = res.json()
    pegarpokemon3(poke)


def main2():
    apo = f'https://pokeapi.co/api/v2/pokemon/{m}'
    res = requests.get(apo)
    poke = res.json()
    print(f'o pokemon mais forte é o {m} : ')
    pegarpokemon2(poke)


main()
while True:
    escolha = str(input('deseja escolher outro tipo para comparar tambem?')).lower()
    if escolha == 'sim':
        main3()
    else:
        break

print('-=' * 20)
main2()