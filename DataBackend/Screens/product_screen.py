class ProductMenu:

    def __init__(self, controlador):
        self.__controlador = controlador
    
    def le_numero_inteiro(self, mensagem: str = "", inteiros_validos = [1, 2, 3, 4]):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Por favor digite uma opção válida")
                if inteiros_validos:
                    print("Valores válidos: ", inteiros_validos)

    def mostra_opcoes(self):
        print("----|Menu de Produtos|----")
        print("1 - Incluir produtos")
        print("2 - Remover produtos")
        print("3 - Listar produtos  ")
        print("4 - Voltar")
        opcao = self.le_numero_inteiro("Escolha uma opção: ", [1, 2, 3, 4])
        return opcao