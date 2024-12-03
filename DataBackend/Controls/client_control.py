from ..Classes.client import Client
from ..Screens.client_screen import ClientMenu
import datetime
import os
import pickle

clients: list = []

class ClientControl:

    def __init__(self):
        self.__client_screen = ClientMenu(self)
        self.is_on_screen: bool = True

        self.path: str = os.environ["APPDATA"]
        self.path_folder: str = os.path.join(self.path, "Vestidos")
        os.makedirs(self.path_folder, exist_ok=True)
        self.path_file: str = os.path.join(self.path_folder, "Clients.pkl")

        self.load()

    
    def save(self) -> None:
        with open(self.path_file,"wb") as save:
            pickle.dump(clients, save)
    
    def load(self):
        if os.path.isfile(self.path_file):
            with open(self.path_file,"rb") as save:
                clients.clear()
                for obj in pickle.load(save):
                    clients.append(obj)

    def start_client_screen(self):
        self.is_on_screen = True
        self.open_client_screen()

    def add_client(self, name, number, email, instagram, cpf, birth_date):
        clients.append(Client(name,int(number),email,instagram,int(cpf),birth_date))
        self.save()

    def remove_client(self, name):
        removed_client = None
        for i in range(len(clients)):
            client = clients[i]
            if client.name == name:
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
        # exit(0)
        self.is_on_screen = False

    def open_client_screen(self):
        switcher = {
            1: lambda: self.add_client(
                input("Insira as seguintes informações\nNome do cliente: "),
                input("Número de telefone do cliente: "),
                input("E-mail do cliente: "),
                input("Instagram do cliente (se não houver deixe vazio): "),
                input("CPF do cliente: "),
                datetime.datetime(int(input("Ano de nascimento do cliente: ")),int(input("Mês de nascimento: ")),int(input("Dia de nascimento: "))),
            ),
            2: lambda: self.remove_client(input("Insira o nome do cliente que deseja remover: ")),
            3: self.show_client, 
            4: self.back
        }
        while self.is_on_screen:
            option = self.__client_screen.show_options()
            chosen_option = switcher[option]
            chosen_option()