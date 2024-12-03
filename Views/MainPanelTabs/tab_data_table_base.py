from decimal import Decimal
import inspect
from typing import List
import flet as ft
from Translations.translation_server import tr

class TabDataTableBase(ft.Tab):    
    def __init__(self, text_id: str, icon: ft.Icon,class_def) -> None:
        super().__init__()
        self.text_id: str = text_id
        self.text: str = tr(text_id)
        self.icon = icon
        self.class_def = class_def

        self.data_columns: List[ft.DataColumn] = self.get_table_columns()

        self.data_table: ft.DataTable = ft.DataTable(
            columns=self.get_table_columns(),
            
        )

        self.table_container: ft.Container = ft.Container(
            content=self.data_table,
            # expand=True,
        )

        self.content = self.table_container
        
    
    def sorting_key(tab, value) -> int:
        assert isinstance(tab, TabDataTableBase), f"{tab} is not an 'TabDataTableBase'!"
        if hasattr(tab.class_def, "ORDER") and isinstance(tab.class_def.ORDER, dict):
            return tab.class_def.ORDER.get(value[0], len(value[0]) + 100)
            
        return len(value[0]) + 100

    def get_table_columns(self) -> List[ft.DataColumn]:
        annotations: dict = {}

        for c in inspect.getmro(self.class_def):
            if '__annotations__' in c.__dict__:
                annotations.update(c.__dict__['__annotations__'])
        
        # print(annotations)

        annotations = dict(
            sorted(
                annotations.items(),
                key=self.sorting_key,
            )
        )

        # print(annotations)

        data_columns: List[ft.Column] = []

        for name, type in annotations.items():

            if not inspect.isclass(type):
                continue
            
            is_numeric: bool = False
            if issubclass(type, int) or issubclass(type, Decimal) or issubclass(type, float):
                is_numeric = True

            data_columns.append(
                ft.DataColumn(
                    label=ft.Text(tr(name)),
                    numeric=is_numeric
                )
            )
        
        return data_columns

        