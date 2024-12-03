from decimal import Decimal
from ..Classes.suit import Suit
from .supplier_control import suppliers
from ..Screens.product_screen import ProductMenu
import os
import pickle

suits: list = [].copy()

class SuitControl:
    
    def __init__(self):
        self.__product_screen = ProductMenu(self)
        self.is_on_screen: bool = True

        self.path: str = os.environ["APPDATA"]
        self.path_folder: str = os.path.join(self.path, "Vestidos")
        os.makedirs(self.path_folder, exist_ok=True)
        self.path_file: str = os.path.join(self.path_folder, "Suits.pkl")

        self.load()

    
    def save(self) -> None:
        with open(self.path_file,"wb") as save:
            pickle.dump(suits, save)
    
    def load(self):
        if os.path.isfile(self.path_file):
            with open(self.path_file,"rb") as save:
                suits.clear()
                for obj in pickle.load(save):
                    suits.append(obj)

    def start_product_screen(self):
        self.is_on_screen = True
        self.open_product_screen()

    def add_product(self, name: str, code: str, description: str, size: int, supplier: str, buying_price:Decimal, selling_price:Decimal):
        for i in range(len(suppliers)):
            check_supplier = suppliers[i]
            if supplier == check_supplier.name:
                suits.append(Suit(name, code, description, int(size), supplier, Decimal(buying_price), Decimal(selling_price)))
                self.save()
                break
            else:
                print("O fornecedor informado não está cadastrado, cadastre o fornecedor e tente novamente.")
    
    def remove_product(self, code):
        # code = input('Insira o código do produto que deseja remover: ')
        removed_product = None
        for d in range(len(self.suits)):
            suit: Suit = self.suits[d]
            if suit.code == code:
                removed_product = suits.pop(d)
                break
        if removed_product == None:
            print("Este produto não está cadastrado.")

    def show_products(self):
        print("Produtos cadastrados: ")
        for c in suits:
            data = '''Código: {code}
    Descrição: {description}
    Tamanho: {size}
    Fornecedor: {supplier}
    Preço de compra: {purchase_price}
    Preço de venda: {selling_price}'''.format(code = c.code, description = c.description, size = c.size, supplier = c.supplier, purchase_price = c.purchase_price, selling_price = c.selling_price)
            print(data)

    def back(self):
        #alterar para que ao invés de encerrar o programa o método retorne ao menu principal
        # exit(0)
        self.is_on_screen = False
    
    def open_product_screen(self):
        switcher = {
            1: lambda: self.add_product(
                input("Insira as seguintes informações\nNome do produto: "),
                input("Código do produto: "),
                input("Descrição do produto: "),
                input("Tamanho do produto: "),
                input("Nome do fornecedor do produto: "),
                input("Preço de compra do produto: "),
                input("Preço de venda do produto: "),
            ),
            2: lambda: self.remove_product(input("Código do produto: ")),
            3: self.show_products, 
            4: self.back
        }
        while self.is_on_screen:
            option = self.__product_screen.show_options()
            chosen_option = switcher[option]
            chosen_option()