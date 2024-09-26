from flet import Column, Text
from components.app_Bar import createAppBar
def CreateAppLayout(page):
    page.title = "Gerador de rotas"
    page.add(createAppBar())
    page.add(Text(Column("_-Gerador de Rotas Otimizadas!-_")))
    page.add(Text(Column("_-TESTE!-_")))
    page.update()