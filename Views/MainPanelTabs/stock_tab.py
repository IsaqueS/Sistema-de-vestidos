import flet as ft
from .tab_data_table_base import TabDataTableBase
from DataBackend.Classes.suit import Suit

class StockTab(TabDataTableBase):
    def __init__(self) -> None:
        super().__init__("stock", ft.icons.INBOX_OUTLINED, Suit)