import flet as ft
from .tab_data_table_base import TabDataTableBase
from DataBackend.Classes.suit import Suit
from DataBackend.Controls.suit_control import SuitControl, suits

class StockTab(TabDataTableBase):
    def __init__(self) -> None:
        super().__init__("stock", ft.icons.INBOX_OUTLINED, Suit)
        self.suit_control = SuitControl()
        self.data_table.rows = self.load_rows(suits)