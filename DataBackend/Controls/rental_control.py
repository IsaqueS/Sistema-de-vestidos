from ..Classes.rental import Rental
from .client_control import clients
import datetime
from .suit_control import suits
from ..Screens.rental_screen import RentalMenu
import os
import pickle

rentals = []
class RentalControl:

    def __init__(self):
        self.__rental_screen = RentalMenu(self)
        self.is_on_screen: bool = True

        self.path: str = os.environ["APPDATA"]
        self.path_folder: str = os.path.join(self.path, "Vestidos")
        os.makedirs(self.path_folder, exist_ok=True)
        self.path_file: str = os.path.join(self.path_folder, "Rentals.pkl")

        self.load()

    
    def save(self) -> None:
        with open(self.path_file,"wb") as save:
            pickle.dump(rentals, save)
    
    def load(self):
        if os.path.isfile(self.path_file):
            with open(self.path_file,"rb") as save:
                rentals.clear()
                for obj in pickle.load(save):
                    rentals.append(obj)

    def start_rental_screen(self):
        self.is_on_screen = True
        self.open_rental_screen()

    def add_rental(self, wait_time: datetime.datetime, client: str):
            date = datetime.datetime.now()
            print('Insira as seguintes informações')
            products = []
            for i in range(len(clients)):
                check_client = clients[i]
                if client == check_client.name:
                    rentals.append(Rental(date, wait_time, products, check_client))
                    self.save()
                    break
                else:
                    print("Cliente não cadastrado, cadastre o cliente e tente novamente.")

    def remove_rental(self, codigo_removido: str):
            # codigo_removido = input('Insira código do aluguel')
            for c in range(len(rentals)):
                if codigo_removido == rentals[c].rent_code:
                    rentals.pop(c)
                    break
                else:
                    print("Não há aluguel com esse código")
                    break

    def show_rentals(self):
            print("Alugueis cadastrados: ")

            for d in rentals:
                data = '''Código: {rent_code}
    Data: {date}
    Tempo de espera: {wait_time}
    Produtos: {products}
    Cliente: {client}'''.format(rent_code=d.rent_code, date=d.date, wait_time=d.wait_time, products=d.products, client=d.client.name)
                print(data)

    def back(self):
        #alterar para que ao invés de encerrar o programa o método retorne ao menu principal
        # exit(0)
        self.is_on_screen = False

    def open_rental_screen(self):
        switcher = {
            1: lambda: self.add_rental(
                 datetime.datetime(int(input("Ano de devolução do produto: ")), int(input("Mês de devolução do produto: ")), int(input("Dia de devolução do produto: "))),
                 input("Insira o nome do cliente: "),
            ),
            2: lambda: self.remove_rental(
                codigo_removido = input('Insira código do aluguel'),
            ),
            3: self.show_rentals, 
            4: self.back
        }
        while self.is_on_screen:
            option = self.__rental_screen.show_options()
            chosen_option = switcher[option]
            chosen_option()