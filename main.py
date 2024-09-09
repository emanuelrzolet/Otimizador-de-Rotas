from turtle import update
import flet as ft
from numpy import integer
from functions import locations

def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("_-Gerador de Rotas Aprimoradas-_")))
    page.update()
    # Adicionar coordenada
    nameField = ft.TextField(label="Nome", border="underline", hint_text="Digite o nome do ponto de parada: ")
    coordField = ft.TextField(label="Coordenada", border="none", hint_text="Latitude, Longitude: ")
    page.add(nameField, coordField)
    page.add(ft.ElevatedButton(text="Adicionar Coordenada", on_click=lambda e: locations.addLocation(nameField.value, coordField.value)))
    page.update()
    
    
    # Mostrar coordenada
    
    def checkbox_changed(e, index=i):
        location[index]["enabled"] = e.control.value
        page.update()  # Atualiza a página para refletir a mudança
    items = locations.showLocations()
    for i, location in enumerate(items):
        # Função chamada quando o checkbox de um item é alterado
            
        page.add(
            ft.Row(
                controls=[
                    ft.Checkbox(
                        label=location[i],
                        value=1,
                        on_change=lambda e, idx=i: checkbox_changed(e, index=idx),
                    ),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        on_click=lambda e, idx=i: locations.deleteLocation(e, index=idx)
                    ),
                ]
            ))
                
        page.update()
                



ft.app(main)
