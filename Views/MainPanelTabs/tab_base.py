import inspect
from typing import List
import flet as ft
from Translations.translation_server import tr

class TabBase:
    def __init__(self) -> None:
        self.__tab: ft.Tab
        self.setup_tab()
    
    @property
    def tab(self) -> ft.Tab:
        return self.__tab
    
    @tab.setter
    def tab(self, new_tab: ft.Tab) -> None:
        if isinstance(new_tab, ft.Tab):
            self.__tab = new_tab
        else:
            raise ValueError(f"{new_tab} is not an Flet Tab!")
    
    def setup_tab(self) -> None:
        pass
    
    def get_table_columns(self, class_def) -> List[ft.DataColumn]:
        annotations: dict = {}
        for c in inspect.getmro(class_def):
            if '__annotations__' in c.__dict__:
                annotations.update(c.__dict__['__annotations__'])

        data_columns: List[ft.Column] = []
        for name, type in annotations.items():
            
            is_numeric: bool = False
            if issubclass(type, int) or issubclass(type, float):
                is_numeric = True

            data_columns.append(
                ft.DataColumn(
                    label=tr(name),
                    numeric=is_numeric
                )
            )
        return data_columns

        