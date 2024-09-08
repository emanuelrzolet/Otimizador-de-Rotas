import json

with open('locations.json', 'r') as f:
    dados = json.load(f)
    
for k, v in enumerate(dados):
    print(k,v)