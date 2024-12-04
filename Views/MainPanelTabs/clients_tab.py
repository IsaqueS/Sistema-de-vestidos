from typing import override
import flet as ft
from .tab_data_table_base import TabDataTableBase
from DataBackend.Classes.client import Client
from DataBackend.Controls.client_control import clients, ClientControl

class ClientsTab(TabDataTableBase):
    def __init__(self) -> None:
        super().__init__("clients", ft.icons.PEOPLE, Client)
        self.client_control = ClientControl()
        self.data_table.rows = self.load_rows(clients)
    
    def get_all_names(self) -> list[str]:
        names = []
        for client in clients:
            names.append(client.name)
        return names

    @override
    @classmethod
    def select_action(cls, obj: ft.DataRow, action: ft.ControlEvent) -> None:
        cls.invert_selection(obj, action)


    
    
        


