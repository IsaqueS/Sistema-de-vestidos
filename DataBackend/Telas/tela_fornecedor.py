class TelaFornecedor():

    def __init__(self, controlador):
        self.__controlador_fornecedor = controlador

    def le_numero_inteiro(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)