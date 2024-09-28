from supplier import Supplier
from decimal import *

class Product:

    def __init__(self, code: str, description: str, size: int, supplier: Supplier, purchase_price: Decimal, selling_price: Decimal) -> None:
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
        if isinstance(supplier, Supplier):
            self.__supplier = supplier
        self.__purchase_price = None
        if isinstance(purchase_price, Decimal):
            self.__purchase_price = purchase_price
        self.__selling_price = None
        if isinstance(selling_price, Decimal):
            self.__selling_price = selling_price
    
    def code(self) -> str:
        return self.__code
    
    @code.setter
    def code(self, code: str) -> None:
        if isinstance(code, str):
            self.__code = code
    
    def description(self) -> str:
        return self.__descripion
    
    @description.setter
    def description(self, description: str) -> None:
        if isinstance(description , str):
            self.__descripion = description
    
    def size(self) -> int:
        return self.__size
    
    @size.setter
    def size(self, size: int) -> None:
        if isinstance(size, int):
            self.__size = size
    
    @size.__str__
    def get_size_as_str(self) -> str:
        print("IMPLEMENT FEATURE HERE!")

    def supplier(self) -> Supplier:
        return self.__supplier
    
    @supplier.setter
    def supplier(self, supplier: Supplier) -> None:
        if isinstance(supplier, Supplier):
            self.__supplier = supplier

    def purchase_price(self) -> Decimal:
        return self.__purchase_price
    
    @purchase_price.setter
    def purchase_price(self, purchase_price: Decimal) -> None:
        if isinstance(purchase_price, Decimal):
            self.__purchase_price = purchase_price

    def selling_price(self) -> Decimal:
        return self.__selling_price
    
    @selling_price.setter
    def purchase_price(self, selling_price: Decimal) -> None:
        if isinstance(selling_price, Decimal):
            self.__selling_price = selling_price