import flet as ft
from src.layout import main_layout

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ALWAYS  # Permite rolagem sempre
    page.title = "Gerador de Rotas"  # Define o título da página

    # Cria o layout da Aplicação
    main_layout.createAppLayout(page)


# Inicia a aplicação
ft.app(target=main)