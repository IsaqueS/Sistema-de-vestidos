from ..Classes.supplier import Supplier
from ..Telas.tela_fornecedor import TelaFornecedor


fornecedores = []
class ControladorFornecedor():

    def __init__(self):
        self.__tela_fornecedor = TelaFornecedor(self)