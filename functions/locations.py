import flet as ft
def addLocation(name, coord):
    import json

    with open('locations.json', 'r+') as f:
        dados = json.load(f)
        # Passagem dos dados para dentro do objeto
        dados[name] = coord
        
        f.seek(0)  # Move o cursor para o início do arquivo
        f.truncate()  # Limpa o conteúdo do arquivo
        
        # Escrevendo os dados atualizados
        json.dump(dados, f, indent=4)
        
    # Exibindo as chaves e valores
    for k, v in dados.items():
        print(k, v)
    
    

def showLocations():
    import json

    with open('locations.json', 'r') as f:
        dados = json.load(f)
        return dados
    
def deleteLocation(index):
    import json

    with open('locations.json', 'r+') as f:
        dados = json.load(f)
    
    del dados[index]  # Remove o item da lista
    json.dump(dados, f, indent=4) #Salva os itens

    
