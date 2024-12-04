from ..Classes.supplier import Supplier
from ..Screens.suplier_screen import SupplierMenu
import os
import pickle

suppliers = [].copy()

class SupplierControl:

    def __init__(self):
        self.__supplier_screen = SupplierMenu(self)
        self.is_on_screen: bool = True

        self.path: str = os.environ["APPDATA"]
        self.path_folder: str = os.path.join(self.path, "Vestidos")
        os.makedirs(self.path_folder, exist_ok=True)
        self.path_file: str = os.path.join(self.path_folder, "Suppliers.pkl")

        self.load()

    
    def save(self) -> None:
        with open(self.path_file,"wb") as save:
            pickle.dump(suppliers, save)
    
    def load(self):
        if os.path.isfile(self.path_file):
            with open(self.path_file,"rb") as save:
                suppliers.clear()
                for obj in pickle.load(save):
                    suppliers.append(obj)
        
    def start_supplier_screen(self):
        self.is_on_screen = True
        self.open_supplier_screen()

    def add_supplier(self, name: str, number: int, email: str, contact: str, cnpj: int, address: str, website: str):
        suppliers.append(Supplier(name, int(number), email, contact, int(cnpj), address, website))
        self.save()

    def remove_supplier(self, name):
        # nome = input("Insira o nome do fornecedor que deseja remover: ")
        removed_client = None
        for i in range(len(suppliers)):
            client = suppliers[i]
            if client.name == name:
                removed_client = suppliers.pop(i)
                self.save()
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
        # exit(0)
        self.is_on_screen = False

    def open_supplier_screen(self):
        switcher = {
            1: lambda: self.add_supplier(
                input("Insira as seguintes informações:\nNome do fornecedor: "),
                input("Número de telefone do fornecedor: "),
                input("E-mail do fornecedor: "),
                input("Informação adicional de contato do fornecedor: "),
                input("CNPJ do fornecedor: "),
                input("Endereço do fornecedor: "),
                input("Website do fornecedor: "),
            ),
            2: lambda: self.remove_supplier(
                input("Insira o nome do fornecedor que deseja remover: "),
            ),
            3: self.show_suppliers, 
            4: self.back
        }
        while self.is_on_screen:
            option = self.__supplier_screen.show_options()
            chosen_option = switcher[option]
            chosen_option()