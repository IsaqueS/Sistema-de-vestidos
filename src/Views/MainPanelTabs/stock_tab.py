from datetime import datetime
from typing import Dict, override
import flet as ft
from .tab_data_table_base import TabDataTableBase
from DataBackend.Classes.suit import Suit
from DataBackend.Controls.suit_control import SuitControl, suits

class StockTab(TabDataTableBase):
    def __init__(self, app) -> None:
        super().__init__("stock", ft.icons.INBOX_OUTLINED, Suit, app)
        self.suit_control = SuitControl()
        self.data_table.rows = self.load_rows(suits)
    
    @override
    def delete_data(self) -> None:
        for data in self.selected_data:
            if isinstance(data, Suit):
                print(data.name)
                self.suit_control.remove_product(data.code)
        self.data_table.rows = self.load_rows(suits)
        self.update()
    
    @override
    def save_data(self, event) -> None:
        data: Dict[str:str] = self.get_data()

        # print(data)

        # date = data["date"].split("/")

        self.suit_control.add_product(
            data["name"],
            data["code"],
            data["description"],
            data["size"],
            data["supplier"],
            data["purchase_price"],
            data["selling_price"],
        )

        self.data_table.rows = self.load_rows(suits)
        self.app.go_back()
        self.app.page.update()