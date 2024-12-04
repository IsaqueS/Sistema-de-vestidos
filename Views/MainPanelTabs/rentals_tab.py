from datetime import datetime
from typing import Dict, override
import flet as ft
from .tab_data_table_base import TabDataTableBase
from DataBackend.Classes.rental import Rental
from DataBackend.Controls.rental_control import RentalControl, rentals

class RentalsTab(TabDataTableBase):
    def __init__(self, app) -> None:
        super().__init__("rentals", ft.icons.CURRENCY_EXCHANGE_OUTLINED, Rental, app)
        self.rental_control = RentalControl()
        self.data_table.rows = self.load_rows(rentals)
    
    @override
    def delete_data(self) -> None:
        for data in self.selected_data:
            if isinstance(data, Rental):
                self.rental_control.remove_rental(data.rent_code)
        self.data_table.rows = self.load_rows(rentals)
        self.update()
    
    @override
    def save_data(self, event) -> None:
        data: Dict[str:str] = self.get_data()

        print(data)

        date = data["date"].split("/")

        self.rental_control.add_rental(
            datetime(int(date[2]),int(date[1]),int(date[0])),
            data["client"],
        )

        self.data_table.rows = self.load_rows(rentals)
        self.app.go_back()
        self.app.page.update()