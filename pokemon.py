import requests

pokemon = input('Choose your Pokemon: ')
pokemon = pokemon.lower()
url =f'https://pokeapi/co/api/v2/pokemon/{pokemon}'

req = requests.get(url)
data = req.json()

print(data)

