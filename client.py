import datetime

class Client:

    def __init__(self, name: str, number: int, email: str, instagram: str, cpf: int, birth_date: datetime) -> None:
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
        if isinstance(birth_date, datetime):
            self.__birth_date = birth_date
        
        print("IMPLEMENTAR VAREAVEL DA DATA DE REGISTRO NO SISTEMA, AUTOMATICAMENTE")

    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        if isinstance(name, str):
            self.__name = name

    def number(self) -> int:
        return self.__number
    
    @number.setter
    def number(self, number: int) -> None:
        if isinstance(number, int):
            self.__number = number

    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email: str) -> None:
        if isinstance(email, str):
            self.__email = email
    
    def instagram(self) -> str:
        return self.__instagram
    
    @instagram.setter
    def instagram(self, instagram: str) -> None:
        if isinstance(instagram, str):
            self.__instagram = instagram
    
    def cpf(self) -> int:
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf: int) -> None:
        if isinstance(cpf, int):
            self.__cpf = cpf

    def birth_date(self) -> datetime:
        return self.__birth_date
    
    @birth_date.setter
    def birth_date(self, birth_date: datetime) -> None:
        if isinstance(birth_date, datetime):
            self.__birth_date = birth_date
