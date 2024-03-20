import os

    
def CreateUrl(stock_symbol):
    __apiKey = os.getenv("APIKEY")

    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey={__apiKey}'

    return url
