from ..Classes.client import Client
from ..Telas.tela_cliente import TelaCliente
import datetime

clientes = []
class ControladorCliente():

    def __init__(self):
        self.__tela_cliente = TelaCliente(self)

    def inicia_tela_cliente(self):
        self.abre_tela_cliente()

    def inclui_aluno(self):
        print("Insira as seguintes informações")
        nome = input("Nome do cliente: ")
        numero = input("Número de telefone do cliente: ")
        email = input("E-mail do cliente: ")
        instagram = input("Instagram do cliente (se não houver deixe vazio): ")
        cpf = input("CPF do cliente: ")
        data_nascimento = datetime.datetime(int(input("Ano de nascimento do cliente: ")),int(input("Mês de nascimento: ")),int(input("Dia de nascimento: ")))
        self.__clientes.append(Client(nome,int(numero),email,instagram,int(cpf),data_nascimento))

    def remove_cliente(self):
        nome = input("Insira o nome do cliente que deseja remover: ")
        removed_client = None
        for i in range(len(clientes)):
            client = clientes[i]
            if client.name == nome:
                removed_client = clientes.pop(i)
                break
        if removed_client == None:
            print("Por favor insira um cliente que já esteja cadastrado.")

    def exibe_cliente(self):
        print("Clientes cadastrados: ")
        for c in clientes:
            data = '''Nome: {name}
        Numero: {number}
        Email: {email}
        Instagram: {instagram}
        CPF: {cpf}
        Birth Date: {birth_date}
        Registration Date: {registration_date}
    
                '''.format(name = c.name,number = c.number, email = c.email, instagram = c.instagram, cpf = c.cpf, birth_date = c.birth_date, registration_date = c.registration_date)
            print(data)

def voltar(self):
        #alterar para que ao invés de encerrar o programa o método retorne ao menu principal
        exit(0)

def abre_tela_cliente(self):
    switcher = {1: self.inclui_cliente, 2: self.remove_cliente, 3: self.exibe_cliente, 
                4: self.voltar}
    while True:
        opcao = self.__tela_cliente()
        opcao_escolhida = switcher(opcao)
        opcao_escolhida()