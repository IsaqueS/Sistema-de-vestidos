from ..Classes.rental import Rental
from client_control import clientes
import datetime
from suit_control import suits
from ..Screens.rental_screen import RentalMenu

alugueis = []
class RentalControl:

    def __init__(self):
        self.__tela_aluguel = RentalMenu(self)

    def inicia(self):
        self.abre_tela_aluguel()

    def inclui_aluguel(self):
            data = datetime.datetime.now()
            print('Insira as seguintes informações')
            tempo_de_espera = datetime.datetime(int(input("Ano de devolução do produto: ")), int(input("Mês de devolução do produto: ")), int(input("Dia de devolução do produto: ")))
            produtos = []
            cliente = input("Insira o nome do cliente: ")
            for i in range(len(clientes)):
                check_client = clientes[i]
                if cliente == check_client.name:
                    alugueis.append(Rental(data, tempo_de_espera, produtos, cliente))
                    break
                else:
                    print("Cliente não cadastrado, cadastre o cliente e tente novamente.")

    def remove_aluguel(self):
            codigo_removido = input('Insira código do aluguel')
            for c in range(len(alugueis)):
                if codigo_removido == alugueis[c].rent_code:
                    alugueis.pop(c)
                    break
                else:
                    print("Não há aluguel com esse código")
                    break

    def exibe_alugueis(self):
            print("Alugueis cadastrados: ")

            for d in alugueis:
                data = '''Código: {rent_code}
    Data: {date}
    Tempo de espera: {wait_time}
    Produtos: {products}
    Cliente: {client}'''.format(rent_code=d.rent_code, date=d.date, wait_time=d.wait_time, products=d.products, client=d.client)
                print(data)

    def voltar(self):
        #alterar para que ao invés de encerrar o programa o método retorne ao menu principal
        exit(0)

    def abre_tela_aluguel(self):
        switcher = {1: self.inclui_aluguel, 2: self.remove_aluguel, 3: self.exibe_alugueis, 
                4: self.voltar}
        while True:
            opcao = self.__tela_produto.mostra_opcoes()
            opcao_escolhida = switcher[opcao]
            opcao_escolhida()