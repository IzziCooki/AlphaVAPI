from abc import ABC, abstractmethod
from AlphaVAPI.controllers.UrlSetup import CreateUrl
import requests 


class Stock_Params(ABC):

    @abstractmethod
    def print_stock(self): pass

    @abstractmethod
    def raw_data(self): pass

    
class SetStock(Stock_Params):
    def __init__(self, stock):
        self.__stock = stock
   
        self.__url = CreateUrl(self.__stock)
        self.__r = requests.get(self.__url)
 
    def price(self): 
        data = self.__r.json()
        print(data)
        return data["Global Quote"]['05. price']
    

    def raw_data(self):
        data = self.__r.json()
        return data
    
    def print_stock(self):
        print(self.__stock)







