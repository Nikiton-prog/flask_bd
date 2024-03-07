from requests import get, post, delete
from pprint import pprint

print(get('http://127.0.0.1:5000/api/v2/users/2').json())
print()
pprint(get('http://127.0.0.1:5000/api/v2/users').json())
# pprint(post('http://localhost:5000/api/v2/users',
#             json={'surname': 'ivanov',
#                   'name': 'ivan',
#                   'age': '9',
#                   'position': 'gfhrfrg',
#                   'speciality': 'hgdhfhfgh',
#                   'address': 'fdghghdgh',
#                   'email': 'nn.s.ivannikov@gmail.com',
#                   'hashed_password': '123'}).json())

# pprint(post('http://localhost:5000/api/v2/users',
#             json={'surname': 'ivanov',
#                   'name': 'ivan',
#                   'age': '9',
#                   'position': 'gfhrfrg',
#                   'speciality': 'hgdhfhfgh',
#                   'address': 'fdghghdgh',
#                   'email': 'nn.s.ivannikov@gmail.com'}).json())

print(delete('http://localhost:5000/api/v2/users/7').json())
print(delete('http://localhost:5000/api/v2/users/70').json())

