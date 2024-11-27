import flet as ft
from Views.view_template import ViewTemplate

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

        self.menu_bar: ft.NavigationBar = ft.NavigationBar(
            
        )
        
        self.view.controls.append(self.menu_bar)
        self.view.controls.append(ft.Text( "Teste!"))
        self.view.controls.append(ft.TextButton("GoBack", on_click=lambda x:self.app.go_back()))
        return self.view