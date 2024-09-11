import flet as ft
from functions import locations

def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("_-Gerador de Rotas Aprimoradas-_")))
    
    # Função para recarregar a lista de coordenadas
    def reload_locations():
        # Limpa todos os controles da página e recria os campos
        page.controls.clear()
        page.add(ft.SafeArea(ft.Text("_-Gerador de Rotas Aprimoradas-_")))
        page.add(nameField, coordField)
        page.add(ft.ElevatedButton(text="Adicionar Coordenada", on_click=lambda e: locations.addLocation(nameField.value, coordField.value, page, reload_locations)))
        
        # Mostrar coordenada
        items = locations.showLocations()
        for name, coord in items.items():
            page.add(
                ft.Row(
                    controls=[
                        ft.Checkbox(
                            label=name,
                            value=True,
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            on_click=lambda e, loc_name=name: locations.deleteLocation(loc_name, page, reload_locations)  # Passa o nome do local diretamente
                        ),
                    ]
                )
            )
        page.update()

    # Adicionar coordenada
    nameField = ft.TextField(label="Nome", border="underline", hint_text="Digite o nome do ponto de parada: ")
    coordField = ft.TextField(label="Coordenada", border="none", hint_text="Latitude, Longitude: ")
    
    page.add(nameField, coordField)
    page.add(ft.ElevatedButton(text="Adicionar Coordenada", on_click=lambda e: locations.addLocation(nameField.value, coordField.value, page, reload_locations)))

    # Carrega as coordenadas inicialmente
    reload_locations()
    
    page.update()

ft.app(main)
