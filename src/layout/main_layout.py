import flet as ft

# from layout.components.listView import createListView
from .components.app_Bar import createAppBar
from .components.coordList import createCoordList

def createAppLayout(page):
    page.title = "Gerador de rotas"

    # Cria o layout principal
    page.appbar = createAppBar()  # Adiciona a AppBar diretamente à página
    page.coordList = createCoordList(page) # Adiciona o formulário para a Página
    # page.listView = createListView(page)
    
