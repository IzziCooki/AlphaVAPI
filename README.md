# AlphaVAPI
Python wrapper for Alpha Vantage API

# How to run
## Step 1
```
Download zip and extract working directory 
```

## Step 2
## Import the package
```
from AlphaVAPI.main import SetStock
```

## Step 3
## Set the stock you want the price of (VMWare is the example in this case)
```
from AlphaVAPI.main import SetStock
stock = SetStock("VMW")
```

## Step 4
## You can now use this object to either get the stock price or the raw stock price data
```
from AlphaVAPI.main import SetStock
stock = SetStock("VMW")
print(stock.price())
print(stock.raw_data())
```
