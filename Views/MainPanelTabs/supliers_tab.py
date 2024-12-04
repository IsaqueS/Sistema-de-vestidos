import flet as ft
from .tab_data_table_base import TabDataTableBase
from DataBackend.Classes.supplier import Supplier
from DataBackend.Controls.supplier_control import suppliers, SupplierControl

class SupliersTab(TabDataTableBase):
    def __init__(self) -> None:
        super().__init__("suppliers", ft.icons.BUSINESS_ROUNDED, Supplier)
        self.supplier_control = SupplierControl()
        self.data_table.rows = self.load_rows(suppliers)
