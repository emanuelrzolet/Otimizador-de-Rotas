def addLocation():
    import json

    with open('locations.json', 'r+') as f:
        dados = json.load(f)
        dados["Teste"] = "-48.50, -25.00"
        
        f.seek(0)  # Move o cursor para o início do arquivo
        f.truncate()  # Limpa o conteúdo do arquivo
        
        # Escrevendo os dados atualizados
        json.dump(dados, f, indent=4)
        
    # Exibindo as chaves e valores
    for k, v in dados.items():
        print(k, v)
