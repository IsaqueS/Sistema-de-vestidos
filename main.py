import flet as ft

from Views import *

class App:

    def __init__(self) -> None:
        self.__window_title = "Vestidos Essencia"
        
    
    def run(self) -> None:
        ft.app(self.main)
    
    def initial_window_setup(self, page: ft.Page):
        page.title = self.__window_title
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.theme_mode=ft.ThemeMode.DARK
        page.window.min_width = 700
        page.window.min_height = 500
        
        page.views.clear()

    def main(self, page: ft.Page) -> None:
        
        self.initial_window_setup(page)


        main_view = MainPanel(page)
        

        page.go("/")
        print(page.views)

if __name__ == "__main__":
    app = App()
    app.run()