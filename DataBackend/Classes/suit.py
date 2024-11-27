from .supplier import Supplier
from decimal import *

class Suit:

    def __init__(self, code: str, description: str, size: int, supplier: str, purchase_price: float, selling_price: float) -> None:
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
        if isinstance(purchase_price, float):
            self.__purchase_price = purchase_price
        self.__selling_price = None
        if isinstance(selling_price, float):
            self.__selling_price = selling_price
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
    def purchase_price(self) -> float:
        return self.__purchase_price
    
    @purchase_price.setter
    def purchase_price(self, purchase_price: float) -> None:
        if isinstance(purchase_price, float):
            self.__purchase_price = purchase_price
    @property
    def selling_price(self) -> float:
        return self.__selling_price
    
    @selling_price.setter
    def purchase_price(self, selling_price: float) -> None:
        if isinstance(selling_price, float):
            self.__selling_price = selling_price
