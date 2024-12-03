import flet as ft
from .tab_data_table_base import TabDataTableBase
from DataBackend.Classes.supplier import Supplier

class SupliersTab(TabDataTableBase):
    def __init__(self) -> None:
        super().__init__("suppliers", ft.icons.BUSINESS_ROUNDED, Supplier)