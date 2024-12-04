from typing import Dict, override
import flet as ft
from .tab_data_table_base import TabDataTableBase
from DataBackend.Classes.client import Client
from DataBackend.Controls.client_control import clients, ClientControl
from Translations.translation_server import tr
from datetime import datetime

class ClientsTab(TabDataTableBase):
    def __init__(self, app) -> None:
        super().__init__("clients", ft.icons.PEOPLE, Client, app)
        self.client_control = ClientControl()
        self.data_table.rows = self.load_rows(clients)
        
    
    def get_all_names(self) -> list[str]:
        names = []
        for client in clients:
            names.append(client.name)
        return names
    
    @override
    def save_data(self, event) -> None:
        data: Dict[str:str] = self.get_data()

        date = data["birth_date"].split("/")

        self.client_control.add_client(
            data["name"],
            int(data["number"]),
            data["email"],
            data["instagram"],
            int(data["cpf"]),
            datetime(int(date[2]),int(date[1]),int(date[0])),
        )

        self.data_table.rows = self.load_rows(clients)
        self.app.go_back()
        self.app.page.update()



    @override
    def delete_data(self) -> None:
        for data in self.selected_data:
            if isinstance(data, Client):
                self.client_control.remove_client(data.name)
        self.data_table.rows = self.load_rows(clients)
        self.update()


    
    
        


