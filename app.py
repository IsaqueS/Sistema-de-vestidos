import flet as ft
from Translations.translation_server import tr, translate
from typing import Dict

from Views import *

class App:

    def __init__(self) -> None:
        self.__window_title = tr("app_name")
        self.__last_poped_view: ft.View
        self.title_size: int = 28
        self.__input_method_name: str = "input"
    
    def run(self) -> None:
        ft.app(self.main)
    
    def initial_window_setup(self):
        self.page.title = self.__window_title
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.theme_mode=ft.ThemeMode.DARK
        self.page.window.min_width = 700
        self.page.window.min_height = 500
        
        self.page.views.clear()
    
    def load_views(self) -> None:
        
        self.views: Dict[str,ViewTemplate] = {
            "MainView": MainPanel(self),
            "Manual": Manual(self),
        }

        

        self.page.views.append(self.views["MainView"].view)

        

    def main(self, page: ft.Page) -> None:
        
        self.page = page

        self.initial_window_setup()
        
        self.load_views()

        page.on_keyboard_event = self.global_keyboard_events
        
        page.go(self.views["MainView"].view.route)

    def go_to_manual(self, event: ft.ControlEvent) -> None:
        self.page.views.append(self.views["Manual"].view)
        self.page.go("/manual")
        self.page.update()
    
    def go_back(self) -> None:
        self.__last_poped_view = self.page.views.pop()
        self.page.go(self.page.views[-1].route)

    def global_keyboard_events(self, event: ft.KeyboardEvent) -> None:
        match event.key:
            case "F11":
                self.page.window.full_screen = not self.page.window.full_screen
                self.page.update()
            case _:
                if hasattr(self.page.views[-1], self.__input_method_name) and callable(getattr(self.page.views[-1], self.__input_method_name)):
                    input_func = getattr(self.page.views[-1])
                    input_func(event)
                else:
                    print("function does not exist :P")
                    print(type(self.page.views[-1]))
                    print(self.page.views[-1])


                

