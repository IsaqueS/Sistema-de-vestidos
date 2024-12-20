from datetime import datetime
from .person import Person
from enum import Enum


class Client(Person):

    cpf: int
    birth_date: datetime
    instagram: str

    ORDER: dict[str, int] = {
        "name": 0,
        "number": 1,
        "cpf": 2,
        "email": 3,
        "birth_date": 4,
        "instagram": 5,
    }
        


    def __init__(self, name: str, number: int, email: str, instagram: str, cpf: int, birth_date: datetime) -> None:
        super().__init__(name, number, email)
        if isinstance(instagram, str):
            self.__instagram: str = instagram
        self.__cpf = None
        if isinstance(cpf, int):
            self.__cpf: int = cpf
        self.__birth_date = None
        if isinstance(birth_date, datetime):
            self.__birth_date: datetime = birth_date

        self.__registration_date: datetime = datetime.now()

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

    @property
    def registration_date(self) -> datetime:
        return self.__registration_date