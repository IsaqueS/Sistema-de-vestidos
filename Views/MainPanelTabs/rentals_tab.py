import flet as ft
from .tab_data_table_base import TabDataTableBase
from DataBackend.Classes.rental import Rental
from DataBackend.Controls.rental_control import RentalControl, rentals

class RentalsTab(TabDataTableBase):
    def __init__(self) -> None:
        super().__init__("rentals", ft.icons.CURRENCY_EXCHANGE_OUTLINED, Rental)
        self.rental_control = RentalControl()
        self.data_table.rows = self.load_rows(rentals)