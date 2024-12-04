from .supplier import Supplier
from decimal import *


class Suit:

    name: str
    code: str
    description: str
    size: int
    supplier: str
    purchase_price: Decimal
    selling_price: Decimal

    ORDER: dict[str, int] = {
        "name": 0,
        "code": 1,
        "description": 3,
        "size": 2,
        "purchase_price": 4,
        "selling_price": 5,
    }

    def __init__(self, name: str, code: str, description: str, size: int, supplier: str, purchase_price: Decimal, selling_price: Decimal) -> None:
        self.__name: str = None
        if isinstance(name, str):
            self.__name = name
        self.__code = None
        if isinstance(code, str):
            self.__code = code
        self.__descripion = None
        if isinstance(description, str):
            self.__descripion = description
        self.__size = None
        if isinstance(size, int):
            self.__size = size
        self.__supplier = None
        if isinstance(supplier, str):
            self.__supplier = supplier
        self.__purchase_price = None
        if isinstance(purchase_price, Decimal):
            self.__purchase_price = purchase_price
        self.__selling_price = None
        if isinstance(selling_price, Decimal):
            self.__selling_price = selling_price

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        if isinstance(name, str):
            self.__name = name

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str) -> None:
        if isinstance(code, str):
            self.__code = code

    @property
    def description(self) -> str:
        return self.__descripion

    @description.setter
    def description(self, description: str) -> None:
        if isinstance(description , str):
            self.__descripion = description

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int) -> None:
        if isinstance(size, int):
            self.__size = size

    @property
    def supplier(self) -> str:
        return self.__supplier

    @supplier.setter
    def supplier(self, supplier: Supplier) -> None:
        if isinstance(supplier, str):
            self.__supplier = supplier

    @property
    def purchase_price(self) -> Decimal:
        return self.__purchase_price

    @purchase_price.setter
    def purchase_price(self, purchase_price: Decimal) -> None:
        if isinstance(purchase_price, Decimal):
            self.__purchase_price = purchase_price

    @property
    def selling_price(self) -> Decimal:
        return self.__selling_price

    @selling_price.setter
    def purchase_price(self, selling_price: Decimal) -> None:
        if isinstance(selling_price, Decimal):
            self.__selling_price = selling_price