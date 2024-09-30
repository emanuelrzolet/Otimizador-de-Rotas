# main_layout.py
from flet import Column, Text
from .components.app_Bar import createAppBar

def createAppLayout(page):
    page.title = "Gerador de rotas"
    print("createAppLayout chamada!")  # Verifique se essa mensagem aparece no console


    # Cria o layout principal
    page.add(
        Column([
            createAppBar(),
            Text("_-Gerador de Rotas Otimizadas!-_"),
            Text("_-TESTE!-_"),
        ])
    )
