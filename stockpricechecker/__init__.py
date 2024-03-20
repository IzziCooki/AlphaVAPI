from abc import ABC, abstractmethod
from AlphaVAPI.main import SetStock
import json



    
stock = SetStock("VMW")
print(stock.price())
print(stock.raw_data())