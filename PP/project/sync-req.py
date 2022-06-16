import requests
import os
import time

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}IBM&apikey=demo{}'
symbols = ['APPL', 'GOOG', 'TSLA', 'MSFT','IBM',
            'APPL', 'GOOG', 'TSLA', 'MSFT','IBM',
            'APPL', 'GOOG', 'TSLA', 'MSFT','IBM',
            'APPL', 'GOOG', 'TSLA', 'MSFT','IBM',
            'APPL', 'GOOG', 'TSLA', 'MSFT','IBM',
            'APPL', 'GOOG', 'TSLA', 'MSFT','IBM',
            'APPL', 'GOOG', 'TSLA', 'MSFT','IBM',
            'APPL', 'GOOG', 'TSLA', 'MSFT','IBM',
            'APPL', 'GOOG', 'TSLA', 'MSFT','IBM',
            'APPL', 'GOOG', 'TSLA', 'MSFT','IBM',
            'APPL', 'GOOG', 'TSLA', 'MSFT','IBM',
            'APPL', 'GOOG', 'TSLA', 'MSFT','IBM']
results = []

start = time.time()
for symbol in symbols:
    #print(f'Working on symbol {symbol}')
    response = requests.get(url.format(symbol, api_key))
    results.append(response.json())
print('You did it!')
end = time.time()
print(f'it took {end-start} seconds to make {len(symbols)} API calls')