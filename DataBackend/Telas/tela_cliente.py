class TelaCliente:

    def __init__(self, controlador):
        self.__controlador_cliente = controlador

    def le_numero_inteiro(self, mensagem: str = "", inteiros_validos: [] = None):
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
                    print("Opções válidos: ", inteiros_validos)

    def mostra_opcoes(self):
        print("----|Menu de Clientes|----")
        print("1 - Incluir cliente")
        print("2 - Remover clientes")
        print("3 - Listar clientes")
        print("4 - Voltar clientes")
        opcao = self.le_numero_inteiro("Escolha uma opção: ", [1, 2, 3, 4])
        return opcao