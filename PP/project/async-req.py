import asyncio
import aiohttp # make request module async 
import os
import time
from dotenv import load_dotenv
load_dotenv()

api_key = 'LI6F4PSBO2RMZ1Z5'
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}IBM&apikey={}'
symbols = ['APPL', 'GOOG', 'TSLA', 'MSFT','IBM',
            'AADI', 'AAME', 'ABNB', 'AMCX','BZFD',
            'COUR', 'CRI', 'AXP', 'BROS','BYFC',
            'CORS', 'C', 'EVGR', 'EBAY','EA',
            'BTI', 'ANTM', 'UL', 'BAC','DPZ',
            'KHC', 'SBUX', 'SONY', 'TSM','FDX',
            'HSY', 'MTCH', 'HSBC', 'FB','IQ',
            'ZBRA', 'FOX', 'CVS', 'NVDA','NKE',
            'K', 'CMCSA', 'PYPL', 'AACG','AMZN',
            'CSL', 'DIS', 'TMUS', 'HBO','NFLX',
            'CPB', 'CROX', 'MCD', 'HD','CVX',
            'KOF', 'RL', 'QCOM', 'UPS','BABA']
results = []
start = time.time()
async def get_symbols():
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
            print(f'Working on {symbol}')
            response = await session.get(url.format(symbol, api_key), ssl=False)
            results.append(await response.json())

# make event loop
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(get_symbols())
#loop = asyncio.get_event_loop()
#loop.run_until_complete(get_symbols())
#loop.close()
end = time.time()
print(f'it took {end-start} seconds to make {len(results)} API calls')
print('You did it!')

