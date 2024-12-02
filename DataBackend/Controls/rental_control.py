from ..Classes.rental import Rental
from client_control import clients
import datetime
from suit_control import suits
from ..Screens.rental_screen import RentalMenu

rentals = []
class RentalControl:

    def __init__(self):
        self.__rental_screen = RentalMenu(self)

    def start_rental_screen(self):
        self.open_rental_screen()

    def add_rental(self):
            date = datetime.datetime.now()
            print('Insira as seguintes informações')
            wait_time = datetime.datetime(int(input("Ano de devolução do produto: ")), int(input("Mês de devolução do produto: ")), int(input("Dia de devolução do produto: ")))
            products = []
            client = input("Insira o nome do cliente: ")
            for i in range(len(clients)):
                check_client = clients[i]
                if client == check_client.name:
                    rentals.append(Rental(date, wait_time, products, client))
                    break
                else:
                    print("Cliente não cadastrado, cadastre o cliente e tente novamente.")

    def remove_rental(self):
            codigo_removido = input('Insira código do aluguel')
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
    Cliente: {client}'''.format(rent_code=d.rent_code, date=d.date, wait_time=d.wait_time, products=d.products, client=d.client)
                print(data)

    def back(self):
        #alterar para que ao invés de encerrar o programa o método retorne ao menu principal
        exit(0)

    def open_rental_screen(self):
        switcher = {1: self.add_rental, 2: self.remove_rental, 3: self.show_rentals, 
                4: self.back}
        while True:
            option = self.__rental_screen.show_options()
            chosen_option = switcher[option]
            chosen_option()