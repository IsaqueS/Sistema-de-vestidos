from abc import ABC, abstractmethod
class Person(ABC):

    name: str
    number: int
    email: str

    @abstractmethod
    def __init__(self, name: str, number: int, email: str) -> None:
        self.__name = None
        if isinstance(name, str):
            self.__name: str = name
        self.__number = None
        if isinstance(number, int):
            self.__number: int = number
        self.__email = None
        if isinstance(email, str):
            self.__email: str = email

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if isinstance(name, str):
            self.__name = name

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        if isinstance(number, int):
            self.__number = number

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        if isinstance(email, str):
            self.__email = email