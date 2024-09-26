import flet as ft
from src.utils import gerador
from src.data import locations
from src.layout import main_layout


def main(page: ft.Page):
    page.scroll = ft.ScrollMode.ALWAYS  # Permite rolagem sempre
    #Cria a parte visual principal do APP
    # TESTAR
    main_layout.CreateAppLayout(page)
    
    
    page.add(ft.SafeArea(ft.Text("_-Gerador de Rotas Aprimoradas-_")))

    selected_items = {}  # Armazena o estado dos checkboxes (True/False) com base no nome

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
            selected_items[name] = True  # Inicializa todos os checkboxes como True
            
            def checkbox_changed(e, loc_name=name):
                selected_items[loc_name] = e.control.value  # Atualiza o estado quando o checkbox é alterado

            page.add(
                ft.Row(
                    controls=[
                        ft.Checkbox(
                            label=name,
                            value=True,  # Valor inicial sempre true para demonstrar o estado
                            on_change=checkbox_changed  # Função chamada ao alterar o checkbox
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            on_click=lambda e, loc_name=name: locations.deleteLocation(loc_name, page, reload_locations)  # Passa o nome do local diretamente
                        ),
                    ]
                )
            )

        # Botão para capturar os itens selecionados
        page.add(ft.ElevatedButton(text="Capturar Selecionados", on_click=CaptureLocations))

        page.update()

    # Função para capturar os itens marcados e exibir como JSON
    def CaptureLocations(e):
        selected_coords = {name: coord for name, coord in locations.showLocations().items() if selected_items.get(name)}
        
        # Gere as coordenadas para cada local selecionado
        gerador.generate(selected_coords)
        
        for name, coord in selected_coords.items():
            
            formatted_coord = ','.join(map(str, coord))
            maps_url = f"https://www.google.com/maps/search/?api=1&query={formatted_coord}"
            
            # Adiciona o link clicável para cada coordenada
            page.add(ft.TextButton(text=f"{name}: {coord}", url=maps_url))  # Usa TextButton para criar o link
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
