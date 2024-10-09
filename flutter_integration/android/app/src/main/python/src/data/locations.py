import json

def addLocation(name, coord, page, reload_locations):
    with open('locations.json', 'r+') as f:
        dados = json.load(f)
        # Passagem dos dados para dentro do objeto
        dados[name] = coord
        
        f.seek(0)  # Move o cursor para o início do arquivo2
        f.truncate()  # Limpa o conteúdo do arquivo
        
        # Escrevendo os dados atualizados
        json.dump(dados, f, indent=4)
    
    # Atualiza a lista de coordenadas
    reload_locations()

def getLocations():
    with open('locations.json', 'r') as f:
        dados = json.load(f)
        return dados
    
def deleteLocation(name, page, reload_locations):
    with open('locations.json', 'r+') as f:
        dados = json.load(f)
        
        if name in dados:
            del dados[name]  # Remove o item do dicionário
            
            f.seek(0)  # Move o cursor para o início do arquivo
            f.truncate()  # Limpa o conteúdo do arquivo
            
            # Salva os itens restantes
            json.dump(dados, f, indent=4)
    
    # Atualiza a lista de coordenadas
    reload_locations()
