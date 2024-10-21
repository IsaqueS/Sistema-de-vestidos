import datetime

from person import Person


class Client(Person):

    def __init__(self, name: str, number: int, email: str, instagram: str, cpf: int, birth_date: datetime) -> None:
        super().__init__(name, number, email)
        self.__name = None
        if isinstance(name, str):
            self.__name = name
        self.__number = None
        if isinstance(number, int):
            self.__number = number
        self.__email = None
        if isinstance(email, str):
            self.__email = email
        self.__instagram = None
        if isinstance(instagram, str):
            self.__instagram = instagram
        self.__cpf = None
        if isinstance(cpf, int):
            self.__cpf = cpf
        self.__birth_date = None
        if isinstance(birth_date, datetime.datetime):
            self.__birth_date = birth_date
        
        print("IMPLEMENTAR VAREAVEL DA DATA DE REGISTRO NO SISTEMA, AUTOMATICAMENTE")

    @property
    def instagram(self) -> str:
        return self.__instagram
    
    @instagram.setter
    def instagram(self, instagram: str) -> None:
        if isinstance(instagram, str):
            self.__instagram = instagram
    @property
    def cpf(self) -> int:
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf: int) -> None:
        if isinstance(cpf, int):
            self.__cpf = cpf
    @property
    def birth_date(self) -> datetime:
        return self.__birth_date
    
    @birth_date.setter
    def birth_date(self, birth_date: datetime) -> None:
        if isinstance(birth_date, datetime.datetime):
            self.__birth_date = birth_date
