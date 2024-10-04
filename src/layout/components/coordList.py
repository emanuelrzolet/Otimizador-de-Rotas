import flet as ft
from src.data import locations
from ...utils import gerador

def createCoordList(page):

    # Contêiner principal com alinhamento centralizado
    layout_container = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza verticalmente os itens dentro da coluna
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza horizontalmente os itens dentro da coluna
    )

    # Campos de entrada para adicionar novas coordenadas
    nameField = ft.TextField(
    label="Nome",
    border="underline",
    hint_text="Digite o nome do ponto de parada: ",
    expand=4
    )
    coordField = ft.TextField(
    label="Coordenada",
    border="none",
    hint_text="Latitude, Longitude: ",
    expand=4
    )


    # Colocar os campos de entrada em um Row para centralização
    input_fields = ft.Row(
        controls=[nameField, coordField],
        alignment=ft.MainAxisAlignment.CENTER  # Centraliza os campos horizontalmente
    )

    # Adicionar os campos de entrada ao layout centralizado
    layout_container.controls.append(input_fields)

    # Botão para adicionar coordenada
    layout_container.controls.append(
        ft.ElevatedButton(text="Adicionar Coordenada", on_click=lambda e: locations.addLocation(nameField.value, coordField.value, page, reload_locations))
    )

    # Contêiner contendo a lista de coordenadas, visível por padrão
    coord_list_container = ft.Column(visible=True)
    layout_container.controls.append(coord_list_container)
    page.add(layout_container)

    selected_items = {}  # Armazena o estado dos checkboxes (True/False) com base no nome

    # Função para recarregar a lista de coordenadas
    def reload_locations():
        # Limpa os controles do contêiner
        coord_list_container.controls.clear()
        
        # Mostrar coordenada
        items = locations.getLocations()
        for name, coord in items.items():
            selected_items[name] = True  # Inicializa todos os checkboxes como True

            def checkbox_changed(e, loc_name=name):
                selected_items[loc_name] = e.control.value  # Atualiza o estado quando o checkbox é alterado

            # Adiciona coordenada ao contêiner
            coord_list_container.controls.append(
                ft.Row(
                    controls=[
                        ft.Checkbox(
                            label=name,
                            value=True,
                            on_change=checkbox_changed
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            on_click=lambda e, loc_name=name: locations.deleteLocation(loc_name, page, reload_locations)
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER  # Centraliza os itens dentro da linha
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
            page.add(ft.TextButton(text=f"{name}: {coord}", url=maps_url))

        # Minimiza a lista automaticamente após gerar a rota
        coord_list_container.visible = False
        coord_list_container.update()
        page.update()
        
    # Botão para expandir/minimizar a lista
    def toggle_list(e):
        coord_list_container.visible = not coord_list_container.visible
        coord_list_container.update()

    # Contêiner horizontal para os botões
    button_row = ft.Row(
        controls=[
            ft.ElevatedButton(text="Expandir/Minimizar Lista", on_click=toggle_list),
            ft.ElevatedButton(text="Gerar Rota", on_click=captureLocations)
        ],
        alignment=ft.MainAxisAlignment.CENTER  # Alinha os botões no centro horizontalmente
    )

    # Adicionar a linha de botões ao layout centralizado
    layout_container.controls.append(button_row)

    page.update()

