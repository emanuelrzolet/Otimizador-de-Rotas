import flet as ft
from functions import addLocation, showLocation

def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("_-Gerador de Rotas Aprimoradas-_")))
    page.add(ft.SafeArea(ft.Text("Insira o ponto de inicio e fim da rota e seus pontos de parada.")))
    page.update()
    page.update()
    # Adicionar coordenada
    nameField = ft.TextField(label="Nome", border="underline", hint_text="Digite o nome do ponto de parada: ")
    coordField = ft.TextField(label="Coordenada", border="none", hint_text="Latitude, Longitude: ")
    page.add(nameField, coordField)
    page.add(ft.ElevatedButton(text="Adicionar Coordenada", on_click=lambda e: addLocation.addLocation(nameField, coordField)))
    
    
    # Mostrar coordenada
    def checkbox_changed(e):
        output_text.value = (
            f"Adicionar :  {addCheck.value}."
        )
        page.update()

    output_text = ft.Text()
    addCheck = ft.Checkbox(label="NOME CLIENTE", value=True, on_change=checkbox_changed)
    page.add(addCheck, output_text)


ft.app(main)
