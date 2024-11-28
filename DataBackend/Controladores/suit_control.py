from ..Classes.suit import Suit
from supplier_control import fornecedores
from ..Telas.tela_produto import TelaProduto

suits = []

class ControladorProduto:

    def __init__(self):
        self.__tela_produto = TelaProduto(self)
    

    def inicia(self):
        self.abre_tela_produto()

    def inclui_produto(self):
        print("Insira as seguintes informações")
        codigo = input("Código do produto: ")
        descricao = input("Descrição do produto: ")
        tamanho = input("Tamanho do produto: ")
        fornecedor = input("Nome do fornecedor do produto: ")
        preco_de_compra = input("Preço de compra do produto: ")
        preco_de_venda = input("Preço de venda do produto: ")
        for i in range(len(fornecedores)):
            check_supplier = fornecedores[i]
            if fornecedor == check_supplier.name:
                suits.append(Suit(codigo, descricao, int(tamanho), fornecedor, float(preco_de_compra), float(preco_de_venda)))
                break
            else:
                print("O fornecedor informado não está cadastrado, cadastre o fornecedor e tente novamente.")
    
    def remove_produto(self):
        code = input('Insira o código do produto que deseja remover: ')
        removed_product = None
        for d in range(len(suits)):
            suit = suits[d]
            if suit.code == code:
                removed_product = suits.pop(d)
                break
        if removed_product == None:
            print("Este produto não está cadastrado.")

    def exibe_produtos(self):
        print("Produtos cadastrados: ")
        for c in suits:
            data = '''Código: {code}
    Descrição: {description}
    Tamanho: {size}
    Fornecedor: {supplier}
    Preço de compra: {purchase_price}
    Preço de venda: {selling_price}'''.format(code = c.code, description = c.description, size = c.size, supplier = c.supplier, purchase_price = c.purchase_price, selling_price = c.selling_price)
            print(data)

    def voltar(self):
        #alterar para que ao invés de encerrar o programa o método retorne ao menu principal
        exit(0)
    
    def abre_tela_produto(self):
        switcher = {1: self.inclui_produto, 2: self.remove_produto, 3: self.exibe_produtos, 
                4: self.voltar}
        while True:
            opcao = self.__tela_produto.mostra_opcoes()
            opcao_escolhida = switcher[opcao]
            opcao_escolhida()