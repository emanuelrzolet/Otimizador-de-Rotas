import flet as ft
from functions import addLocation

def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("_-Gerador de Rotas Aprimoradas-_")))
    page.add(ft.SafeArea(ft.Text("Insira o ponto de inicio e fim da rota e seus pontos de parada.")))
    page.update()
    page.add(ft.ElevatedButton(text="Adicionar Coordenada", on_click={}))
    page.update()
    
    
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
