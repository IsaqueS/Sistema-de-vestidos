import flet as ft
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

class ViewTemplate(ft.View):
    def __init__(self, app: "App") -> None:
        self.__app: "App" = app
    
    @property
    def app(self) -> "App":
        return self.__app
    
    def setup_view(self) -> ft.View:
        pass