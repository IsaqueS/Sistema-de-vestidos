import datetime
from .supplier import Supplier
from .suit import Suit
from .client import Client
from random import randint



class Rental:

    def __init__(self, date: datetime, wait_time: datetime, products: list, client: Client) -> None:
        self.__rent_code = randint(0, 2000000)
        #self.__date = None
        #if isinstance(date, datetime):
        self.__date = date
        #self.__products = None
        #if isinstance(products, list):
        self.__products = products
        #self.__wait_time = None
        #if isinstance(wait_time, datetime):
        self.__wait_time = wait_time
        #self.__client = None
        #if isinstance(client, Client):
        self.__client = client

    @property
    def rent_code(self) -> int:
        return self.__rent_code

    @property
    def date(self) -> datetime:
        return self.__date

    @date.setter
    def date(self, date: datetime) -> None:
        if isinstance(date,datetime):
            self.__date = date

    @property
    def wait_time(self) -> datetime:
        return self.__wait_time
    
    @wait_time.setter
    def wait_time(self, wait_time: datetime) -> None:
        #if isinstance(wait_time, datetime):
        self.__wait_time = wait_time

    @property
    def products(self) -> list:
        return self.__products
    @property

    def add_product(self, product: Suit) -> None:
        if isinstance(product,Suit):
            self.__products.append(product)

    @property
    def client(self) -> Client:
        return self.__client
    
    @client.setter
    def client(self, client: Client) -> None:
        if isinstance(client, Client):
            self.__client = client
