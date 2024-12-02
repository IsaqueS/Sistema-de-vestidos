from ..Classes.client import Client
from ..Screens.client_screen import ClientMenu
import datetime

clients = []
class ClientControl:

    def __init__(self):
        self.__client_screen = ClientMenu(self)

    def start_client_screen(self):
        self.open_client_screen()

    def add_client(self):
        print("Insira as seguintes informações")
        name = input("Nome do cliente: ")
        number = input("Número de telefone do cliente: ")
        email = input("E-mail do cliente: ")
        instagram = input("Instagram do cliente (se não houver deixe vazio): ")
        cpf = input("CPF do cliente: ")
        birthday = datetime.datetime(int(input("Ano de nascimento do cliente: ")),int(input("Mês de nascimento: ")),int(input("Dia de nascimento: ")))
        clients.append(Client(name,int(number),email,instagram,int(cpf),birthday))

    def remove_client(self):
        nome = input("Insira o nome do cliente que deseja remover: ")
        removed_client = None
        for i in range(len(clients)):
            client = clients[i]
            if client.name == nome:
                removed_client = clients.pop(i)
                break
        if removed_client == None:
            print("Por favor insira um cliente que já esteja cadastrado.")

    def show_client(self):
        print("Clientes cadastrados: ")
        for c in clients:
            data = '''Nome: {name}
        Numero: {number}
        Email: {email}
        Instagram: {instagram}
        CPF: {cpf}
        Birth Date: {birth_date}
        Registration Date: {registration_date}
    
                '''.format(name = c.name,number = c.number, email = c.email, instagram = c.instagram, cpf = c.cpf, birth_date = c.birth_date, registration_date = c.registration_date)
            print(data)

def back(self):
        #alterar para que ao invés de encerrar o programa o método retorne ao menu principal
        exit(0)

def open_client_screen(self):
    switcher = {1: self.add_client, 2: self.remove_client, 3: self.show_client, 
                4: self.back}
    while True:
        option = self.__client_screen.show_options()
        chosen_option = switcher(option)
        chosen_option()