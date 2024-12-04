from decimal import Decimal
import inspect
from typing import List
from warnings import warn
import flet as ft
from DataBackend.Classes.client import Client
from Translations.translation_server import tr
from datetime import datetime

class TabDataTableBase(ft.Tab):    
    def __init__(self, text_id: str, icon: ft.Icon,class_def) -> None:
        super().__init__()
        self.text_id: str = text_id
        self.text: str = tr(text_id)
        self.icon = icon
        self.class_def = class_def
        self.DATA_ORDER: list[str] = None
        self.selected_data: set = set()

        self.data_columns: List[ft.DataColumn] = self.get_table_columns()

        self.data_table: ft.DataTable = ft.DataTable(
            columns=self.data_columns,
            show_checkbox_column=True
            
        )

        self.table_container: ft.Container = ft.Container(
            content=self.data_table,

            # expand=True,
        )

        self.content = self.table_container

    @staticmethod
    def __attr_format(attr) -> object:
        if isinstance(attr, datetime):
            return attr.strftime("%Y/%m/%d")
        if isinstance(attr, Client):
            return attr.name
        
        return attr
        

    def load_rows(self, obj_list: list[object]) -> list[ft.DataRow]:
        rows: list = []
        for obj in obj_list:
            cells: list = []
            for property in self.DATA_ORDER:
                attr = getattr(obj, property)
                attr = self.__attr_format(attr)
                
                cells.append(
                    ft.DataCell(
                        ft.Text(
                            attr
                        ),
                    )
                )
            
            
            row = ft.DataRow(
                    cells=cells,
                    data=obj
                )
            
            row_action: RowActions = RowActions(self, row)

            row.on_select_changed = row_action.select_action

            rows.append(row)

        return rows
    
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

        annotations = dict(
            sorted(
                annotations.items(),
                key=self.sorting_key,
            )
        )
        annotations.pop("ORDER", None)

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
        

        self.DATA_ORDER = list(annotations.keys())
        
        return data_columns
    
class RowActions:

    def __init__(self, tab: ft.Tab, row: ft.DataRow) -> None:
        assert isinstance(row, ft.DataRow), f"{row}, must be an DataRow!"
        assert isinstance(tab, ft.Tab), f"{row} is not ft.Tab!"

        self.row_ref:ft.DataRow = row
        self.tab: TabDataTableBase = tab

    def select_action(self, event: ft.ControlEvent) -> None:
        self.invert_selection(event)
        if self.row_ref.selected:
            self.tab.selected_data.add(self.row_ref.data)
        else:
            self.tab.selected_data.remove(self.row_ref.data)
        # print(self.tab.selected_data)
    
    def invert_selection(self, event: ft.ControlEvent) -> None:
        if isinstance(event, ft.ControlEvent):
            if event.name == "select_changed":
                match event.data:
                    case "true":
                        self.row_ref.selected = True
                    case "false":
                        self.row_ref.selected = False
                self.row_ref.update()
            else:
                warn(f"{event.name} its not implemented!")




    