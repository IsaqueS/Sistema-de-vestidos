from datetime import datetime
import flet as ft
from .tab_base import TabBase
from typing import List, override
from Translations.translation_server import tr
from DataBackend.Classes.client import Client

class ClientTab(TabBase):
    def __init__(self) -> ft.Tab:
        super().__init__()
    
    @override
    def setup_tab(self) -> ft.Tab:
        
        test_clients: list = [Client("IsaqueS", 123123123, "Email@email.com","@IsaqueS", 6969696969,datetime(day=12, month=8, year=2024)),Client("IsaqueS", 123123123, "Email@email.com","@IsaqueS", 6969696969,datetime(day=12, month=8, year=2024)),Client("IsaqueS", 123123123, "Email@email.com","@IsaqueS", 6969696969,datetime(day=12, month=8, year=2024))]
        
        user_defined_attrs = [attr for attr in dir(Client) if not attr.startswith('_')]

        value = self.get_table_columns(Client)
        print(value)
        for i in value:
            print(i.label)

        self.data_table: ft.DataTable = ft.DataTable(
            columns=[]
        )


        self.table_container: ft.Container = ft.Container(
            content=None,
            expand=True
        )
        
        self.tab = ft.Tab(
            text=tr("clients"),
            icon=ft.Icons.PEOPLE,
    	    content=self.table_container
        )

