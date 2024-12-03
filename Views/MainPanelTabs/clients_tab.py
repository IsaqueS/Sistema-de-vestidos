import flet as ft
from .tab_data_table_base import TabDataTableBase
from DataBackend.Classes.client import Client
from DataBackend.Controls.client_control import clients, ClientControl

class ClientsTab(TabDataTableBase):
    def __init__(self) -> None:
        super().__init__("clients", ft.icons.PEOPLE, Client)
        self.client_control = ClientControl()
    
    def get_all_names(self) -> list[str]:
        names = []
        for client in clients:
            names.append(client.name)
        return names
    
        


