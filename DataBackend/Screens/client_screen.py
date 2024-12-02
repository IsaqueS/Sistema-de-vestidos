class ClientMenu:

    def __init__(self, controlador):
        self.__controlador_cliente = controlador

    def read_integer(self, message: str = "", valid_integer = []):
        while True:
            read_value = input(message)
            try:
                inteiro = int(read_value)
                if valid_integer and inteiro not in valid_integer:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Por favor digite uma opção válida")
                if valid_integer:
                    print("Opções válidos: ", valid_integer)

    def show_options(self):
        print("----|Menu de Clientes|----")
        print("1 - Incluir cliente")
        print("2 - Remover clientes")
        print("3 - Listar clientes")
        print("4 - Voltar clientes")
        opcao = self.read_integer("Escolha uma opção: ", [1, 2, 3, 4])
        return opcao