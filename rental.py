import datetime
from supplier import Supplier
from product import Product
from client import Client

#CLASSE DE AGENDA PODE SER REFEITA, PARA ATENDER MELHOR OS REQUISITOS

#Ainda não temos uma forma boa de organizar os dados por data

class Rental:

    def __init__(self, date: datetime, wait_time: datetime, products: list[Product], suppliers: list[Supplier], client: Client) -> None:
        self.__date = None
        if isinstance(date, datetime):
            self.__date = date
        self.__products = None
        if isinstance(products, list[Product]):
            self.__products
        self.__wait_time = None
        if isinstance(wait_time, datetime):
            self.__wait_time = wait_time
        self.__suppliers = None
        if isinstance(suppliers, list[Supplier]):
            self.__date = date
        self.__client = None
        if isinstance(client, Client):
            self.__client = client
        
    def date(self) -> datetime:
        return self.__date

    @date.setter
    def date(self, date: datetime) -> None:
        if isinstance(date,datetime):
            self.__date = date
    
    def wait_time(self) -> datetime:
        return self.__wait_time
    
    @wait_time.setter
    def wait_time(self, wait_time: datetime) -> None:
        if isinstance(wait_time, datetime):
            self.__wait_time = wait_time
    
    def products(self) -> list[Product]:
        return self.__products

    def add_product(self, product: Product) -> None:
        if isinstance(product,Product):
            self.__products.append(product)
    
    def suppliers(self) -> list[Supplier]:
        return self.__suppliers

    def add_supplier(self, supplier: Supplier) -> None:
        if isinstance(supplier,Supplier):
            self.__suppliers.append(supplier)
    
    def client(self) -> Client:
        return self.__client
    
    @client.setter
    def client(self, client: Client) -> None:
        if isinstance(client, Client):
            self.__client = client
