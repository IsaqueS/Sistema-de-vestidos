import flet as ft
from Views.view_template import ViewTemplate
from Translations.translation_server import tr

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

class Manual(ViewTemplate):
    
    def __init__(self, app) -> None:
        super().__init__(app)

        self.view: ft.View = ft.View(
            route="/manual",
        )

        self.setup_view()
    
    def setup_view(self) -> ft.View:
        super().setup_view()

        self.view.vertical_alignment = ft.VerticalAlignment.CENTER

        self.menu_bar_up: ft.MenuBar = ft.AppBar(
            title=ft.Text(tr("manual"), weight=ft.FontWeight.BOLD, size=self.app.title_size),
            center_title=True,
            leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda x: self.app.go_back()),
        )

        self.menu_bar_left: ft.NavigationRail = ft.NavigationRail(
            #expand=True,
            leading=ft.Text(tr("Topicos"), size=20, weight=ft.FontWeight.BOLD),
            # min_width=100,
            bgcolor=ft.colors.BLUE, #For debug only
            width=100,
            

            destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Second",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ]
        )

        row: ft.Row = ft.Row(
            [
                self.menu_bar_left,
                ft.VerticalDivider(),
                ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )


        self.view.controls.append(self.menu_bar_up)
        self.view.controls.append(row)
        
        return self.view