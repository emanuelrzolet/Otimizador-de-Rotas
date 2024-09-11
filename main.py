import flet as ft
from functions import locations

def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("_-Gerador de Rotas Aprimoradas-_")))
    page.update()
    
    # Adicionar coordenada
    nameField = ft.TextField(label="Nome", border="underline", hint_text="Digite o nome do ponto de parada: ")
    coordField = ft.TextField(label="Coordenada", border="none", hint_text="Latitude, Longitude: ")
    page.add(nameField, coordField)
    page.add(ft.ElevatedButton(text="Adicionar Coordenada", on_click=lambda e: locations.addLocation(nameField.value, coordField.value, page)))
    page.update()
    
    # Mostrar coordenada
    def checkbox_changed(e, index):
        items[index]["enabled"] = e.control.value
        page.update()  # Atualiza a página para refletir a mudança

    items = locations.showLocations()
    for i, (name, coord) in enumerate(items.items()):
        # Função chamada quando o checkbox de um item é alterado
        page.add(
            ft.Row(
                controls=[
                    ft.Checkbox(
                        label=name,
                        value=True,  # Valor inicial sempre true para demonstrar o estado
                        on_change=lambda e, idx=i: checkbox_changed(e, idx),  # Passa o índice diretamente
                    ),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        on_click=lambda e, idx=name: locations.deleteLocation(idx, page)  # Passa o nome do local diretamente
                    ),
                ]
            )
        )
        
    page.update()

ft.app(main)
