from ..Classes.supplier import Supplier
from ..Screens.suplier_screen import SupplierMenu


suppliers = []
class SupplierControl:

    def __init__(self):
        self.__supplier_screen = SupplierMenu(self)
        
    def start_supplier_screen(self):
        self.open_supplier_screen()

    def add_supplier(self):
            print("Insira as seguintes informações")
            name = input("Nome do fornecedor: ")
            number = input("Número de telefone do fornecedor: ")
            email = input("E-mail do fornecedor: ")
            contact = input("Informação adicional de contato do fornecedor: ")
            cnpj = input("CNPJ do fornecedor: ")
            address = input("Endereço do fornecedor: ")
            website = input("Website do fornecedor: ")
            suppliers.append(Supplier(name, int(number), email, contact, int(cnpj), address, website))

    def remove_supplier(self):
        nome = input("Insira o nome do fornecedor que deseja remover: ")
        removed_client = None
        for i in range(len(suppliers)):
            client = suppliers[i]
            if client.name == nome:
                removed_client = suppliers.pop(i)
                break
        if removed_client == None:
            print("Por favor insira um cliente que já esteja cadastrado.")

    def show_suppliers(self):
        print("Fornecedores cadastrados: ")
        for c in suppliers:
            data = '''Nome: {name}
    Numero: {number}
    E-mail: {email}
    Contato: {contact}
    CNPJ: {cnpj}
    Endereço: {address}
    Website: {website}'''.format(name = c.name,number = c.number, email = c.email, contact = c.contact, cnpj = c.cnpj, address = c.address, website = c.website)
            print(data)

    def back(self):
        #alterar para que ao invés de encerrar o programa o método retorne ao menu principal
        exit(0)

    def open_supplier_screen(self):
        switcher = {1: self.add_supplier, 2: self.remove_supplier, 3: self.show_suppliers, 
                4: self.back}
        while True:
            option = self.__supplier_screen.show_options()
            chosen_option = switcher[option]
            chosen_option()