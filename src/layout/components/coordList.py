import flet as ft
from src.data import locations
from ...utils import gerador

def createCoordList(page):
    
    # Campos de entrada para adicionar novas coordenadas
    nameField = ft.TextField(label="Nome", border="underline", hint_text="Digite o nome do ponto de parada: ")
    coordField = ft.TextField(label="Coordenada", border="none", hint_text="Latitude, Longitude: ")

    # Botão para adicionar coordenada
    page.add(nameField, coordField)
    page.add(ft.ElevatedButton(text="Adicionar Coordenada", on_click=lambda e: locations.addLocation(nameField.value, coordField.value, page, reload_locations)))
    
    # Container contendo a lista de coordenadas.
    coord_list_container = ft.Column()
    page.add(coord_list_container)

    selected_items = {}  # Armazena o estado dos checkboxes (True/False) com base no nome

    # Função para recarregar a lista de coordenadas
    def reload_locations():
        # Limpa apenas o contêiner de coordenadas
        coord_list_container.controls.clear()  # Remove todos os controles dentro do contêiner
        
        # Mostrar coordenada
        items = locations.getLocations()
        for name, coord in items.items():
            selected_items[name] = True  # Inicializa todos os checkboxes como True

            def checkbox_changed(e, loc_name=name):
                selected_items[loc_name] = e.control.value  # Atualiza o estado quando o checkbox é alterado

            # Adiciona a coordenada ao contêiner
            coord_list_container.controls.append(
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
        
        # Atualiza o contêiner
        coord_list_container.update()
        
    # Exibe a lista
    reload_locations()
    
    # Função para capturar os itens marcados e exibir como JSON
    def captureLocations(e):
        selected_coords = {name: coord for name, coord in locations.getLocations().items() if selected_items.get(name)}
        
        # Gere as coordenadas para cada local selecionado
        gerador.generate(selected_coords)
        
        for name, coord in selected_coords.items():
            formatted_coord = ','.join(map(str, coord))
            maps_url = f"https://www.google.com/maps/search/?api=1&query={formatted_coord}"
            
            # Adiciona o link clicável para cada coordenada
            page.add(ft.TextButton(text=f"{name}: {coord}", url=maps_url))  # Usa TextButton para criar o link
        page.update()
        
    # Botão para Adicionar Coordenadas dos itens selecionados
    page.add(ft.ElevatedButton(text="Gerar Rota", on_click=captureLocations))