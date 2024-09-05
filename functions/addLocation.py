import json

with open('locations.json', 'r') as f:
    dados = json.load(f)

print(dados)