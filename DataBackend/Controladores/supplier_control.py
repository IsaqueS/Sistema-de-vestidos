from ..Classes.supplier import Supplier
from ..Telas.tela_fornecedor import TelaFornecedor


fornecedores = []
class ControladorFornecedor():

    def __init__(self):
        self.__tela_fornecedor = TelaFornecedor(self)
        
    def inicia(self):
        self.abre_tela_fornecedor()

    def inclui_fornecedor(self):
            print("Insira as seguintes informações")
            nome = input("Nome do fornecedor: ")
            numero = input("Número de telefone do fornecedor: ")
            email = input("E-mail do fornecedor: ")
            contato = input("Informação adicional de contato do fornecedor: ")
            cnpj = input("CNPJ do fornecedor: ")
            endereço = input("Endereço do fornecedor: ")
            website = input("Website do fornecedor: ")
            fornecedores.append(Supplier(nome, int(numero), email, contato, int(cnpj), endereço, website))

    def remove_fornecedor(self):
        nome = input("Insira o nome do fornecedor que deseja remover: ")
        removed_client = None
        for i in range(len(fornecedores)):
            client = fornecedores[i]
            if client.name == nome:
                removed_client = fornecedores.pop(i)
                break
        if removed_client == None:
            print("Por favor insira um cliente que já esteja cadastrado.")

    def exibe_fornecedores(self):
        print("Fornecedores cadastrados: ")
        for c in fornecedores:
            data = '''Code: {rent_code}
    Date: {date}
    Wait_time: {wait_time}
    Products: {products}
    Client: {client}'''.format(rent_code=d.rent_code, date=d.date, wait_time=d.wait_time, products=d.products, client=d.client)
            print(data)

    def voltar(self):
        #alterar para que ao invés de encerrar o programa o método retorne ao menu principal
        exit(0)

    def abre_tela_fornecedor(self):
        switcher = {1: self.inclui_fornecedor, 2: self.remove_fornecedor, 3: self.exibe_fornecedores, 
                4: self.voltar}
        while True:
            opcao = self.__tela_fornecedor.mostra_opcoes
            opcao_escolhida = switcher[opcao]
            opcao_escolhida()