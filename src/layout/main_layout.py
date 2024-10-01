import flet as ft
from .components.app_Bar import createAppBar

def createAppLayout(page):
    page.title = "Gerador de rotas"

    # Cria o layout principal
    page.appbar = createAppBar()  # Adiciona a AppBar diretamente à página

    page.add(
        ft.Column([
        ])
    )
