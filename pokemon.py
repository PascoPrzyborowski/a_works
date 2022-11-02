
# dictionary = {
#     "next": "a link",
#     "results": [
#         {"name": "A"},
#         {"name": "B"},
#         {"name": "C"},
#         {"name": "D"},
#     ]
# }




#     # print(r['name'])
# with open('pokemon.txt', 'a') as file:
#     for r in dictionary['results']:
#     #file = open('pokemon.txt', 'w')
#         file.write(f"{r['name']}\n")
#     #file.close()



# # dictionary = {
# #     "next": "a link",
#     "results": [
#         {"name": "A", "items": ["Shaban"]},
#         {"name": "B", "items": ["Peer"]},
#         {"name": "C", "items": ["Jacques"]},
#         {"name": "D", "items": ["Muhannad"]},
#     ]
# }


# for r in dictionary['results']:
#     print(r['items'][0])

import requests

BASE_URL = 'https://pokeapi.co/api/v2/pokemon'

response = requests.get(BASE_URL)

data = response.json()

file = open('pokemon.txt', 'a')
for result in data['results']:    
    file.write(f"{result['name']}\n")
file.close()
