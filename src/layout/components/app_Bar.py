import flet as ft

def createAppBar():
    return ft.AppBar(
        title=ft.Text("Gerador de Rotas"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
        ],
    )
