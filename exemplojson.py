import json
import os

pessoas = [
    {"name": "luiz", "lastname":"Miranda"},
    {"name": "Maria", "lastname":"Moreira"},
    {"name": "Helena", "lastname":"Vieira", "age" : 22}

]

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')

with open(SAVE_TO, 'w') as file:
    json.dump(pessoas, file, indent=2)

print(22, BASE_DIR)