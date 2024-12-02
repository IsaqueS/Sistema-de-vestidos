from ..Classes.suit import Suit
from supplier_control import fornecedores
from ..Screens.product_screen import ProductMenu

suits = []

class SuitControl:

    def __init__(self):
        self.__product_screen = ProductMenu(self)
    

    def start_product_screen(self):
        self.open_product_screen()

    def add_product(self):
        print("Insira as seguintes informações")
        code = input("Código do produto: ")
        description = input("Descrição do produto: ")
        size = input("Tamanho do produto: ")
        supplier = input("Nome do fornecedor do produto: ")
        buying_price = input("Preço de compra do produto: ")
        selling_price = input("Preço de venda do produto: ")
        for i in range(len(fornecedores)):
            check_supplier = fornecedores[i]
            if supplier == check_supplier.name:
                suits.append(Suit(code, description, int(size), supplier, float(buying_price), float(selling_price)))
                break
            else:
                print("O fornecedor informado não está cadastrado, cadastre o fornecedor e tente novamente.")
    
    def remove_product(self):
        code = input('Insira o código do produto que deseja remover: ')
        removed_product = None
        for d in range(len(suits)):
            suit = suits[d]
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
        exit(0)
    
    def open_product_screen(self):
        switcher = {1: self.add_product, 2: self.remove_product, 3: self.show_products, 
                4: self.back}
        while True:
            option = self.__product_screen.show_options()
            chosen_option = switcher[option]
            chosen_option()