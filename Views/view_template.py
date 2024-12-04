import flet as ft
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

class ViewTemplate:
    def __init__(self, app: "App") -> None:
        
        self.__view: ft.View = ft.View()
        self.__view.ref = self
        self.__app: "App" = app

    
    @property
    def app(self) -> "App":
        return self.__app
    
    @property
    def view(self) -> ft.View:
        return self.__view
    
    @view.setter
    def view(self, view: ft.View) -> None:
        if isinstance(view, ft.View):
            self.__view = view
        else:
            raise ValueError("{vw} is not the 'View' class!".format(vw = view))
    
    def setup_view(self) -> ft.View:
        pass