import flet as ft
from Translations.translation_server import tr, translate

from Views import *

class App:

    def __init__(self) -> None:
        self.__window_title = "Vestidos Essencia"
        
    
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
        self.main_view = MainPanel(self)

    def main(self, page: ft.Page) -> None:
        
        self.page = page

        self.initial_window_setup()
        
        self.load_views()

        page.on_keyboard_event = self.global_keyboard_events
        page.go("/")

    
    def global_keyboard_events(self, event: ft.KeyboardEvent) -> None:
        match event.key:
            case "F11":
                self.page.window.full_screen = not self.page.window.full_screen
                self.page.update()

                

if __name__ == "__main__":
    # translate.set_language("en")
    # print(tr("settings"))
    
    app = App()
    app.run()