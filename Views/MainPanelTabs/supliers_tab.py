from typing import Dict, override
import flet as ft
from .tab_data_table_base import TabDataTableBase
from DataBackend.Classes.supplier import Supplier
from DataBackend.Controls.supplier_control import suppliers, SupplierControl

class SupliersTab(TabDataTableBase):
    def __init__(self, app) -> None:
        super().__init__("suppliers", ft.icons.BUSINESS_ROUNDED, Supplier, app)
        self.supplier_control = SupplierControl()
        self.data_table.rows = self.load_rows(suppliers)
    
    @override
    def delete_data(self) -> None:
        for data in self.selected_data:
            if isinstance(data, Supplier):
                print(data.name)
                self.supplier_control.remove_supplier(data.name)
        self.data_table.rows = self.load_rows(suppliers)
        self.update()
    
    @override
    def save_data(self, event) -> None:
        data: Dict[str:str] = self.get_data()

        # print(data)

        # date = data["date"].split("/")

        self.supplier_control.add_supplier(
            data["name"],
            data["number"],
            data["email"],
            data["contact"],
            data["cnpj"],
            data["address"],
            data["website"],
        )

        self.data_table.rows = self.load_rows(suppliers)
        self.app.go_back()
        self.app.page.update()
