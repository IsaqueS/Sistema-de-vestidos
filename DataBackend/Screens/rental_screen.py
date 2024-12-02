class RentalMenu:

    def __init__(self, control):
        self.__rental_control = control

    def read_integer(self, message: str = "", valid_integer = []):
        while True:
            read_value = input(message)
            try:
                integer = int(read_value)
                if valid_integer and integer not in valid_integer:
                    raise ValueError
                return integer
            except ValueError:
                print("Por favor digite uma opção válida")
                if valid_integer:
                    print("Opções validas: ", valid_integer)

    def show_options(self):
        print("----|Menu de Aluguéis|----")
        print("1 - Incluir aluguéis")
        print("2 - Remover aluguéis")
        print("3 - Listar aluguéis")
        print("4 - Voltar aluguéis")
        option = self.read_integer("Escolha uma opção: ", [1, 2, 3, 4])
        return option