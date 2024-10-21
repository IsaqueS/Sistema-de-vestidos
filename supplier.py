import datetime

from person import Person


class Supplier(Person):

    def __init__(self, name: str, number: int, email: str, contact: str, cnpj: int, address: str, website: str) -> None:
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
        self.__contact = None
        if isinstance(contact, str):
            self.__contact = contact
        self.__cnpj = None
        if isinstance(cnpj, int):
            self.__cnpj = cnpj
        self.__address = None
        if isinstance(address, str):
            self.__address = address
        self.__website = None
        if isinstance(website, str):
            self.__website = website

    @property
    def contact(self) -> str:
        return self.__contact
    
    @contact.setter
    def contact(self, contact: str) -> None:
        if isinstance(contact, str):
            self.__contact = contact
    @property
    def cnpj(self) -> int:
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj: int) -> None:
        if isinstance(cnpj, int):
            self.__cnpj = cnpj
    @property
    def address(self) -> str:
        return self.__address
    
    @address.setter
    def address(self, address: str) -> None:
        if isinstance(address, str):
            self._address = address
    @property
    def website(self) -> str:
        return self.__website
    
    @website.setter
    def website(self, website: str) -> None:
        if isinstance(website, str):
            self._website = website
