import requests

req = requests.get("https://swapi.dev/api/people/11/")
print(req.status_code)
person = req.json()
print(person['name'])
print('films involved in: ')
for film in person['films']:
    req = requests.get(film)
    film = req.json()
    print('Film is: ', film['title'])