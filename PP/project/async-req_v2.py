import asyncio
import aiohttp
import os
import time
# To work with the .env file
#from dotenv import load_dotenv
#load_dotenv()

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
results = 0

start = time.time()

def get_tasks(session):
    tasks = []
    for symbol in symbols:
        #print(f'Working on {symbol}')
        tasks.append(asyncio.create_task(session.get(url.format(symbol, api_key), ssl=False)))
    return tasks

async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        # you could also do
        # tasks = [session.get(URL.format(symbol, API_KEY), ssl=False) for symbol in symbols]
        responses = await asyncio.gather(*tasks)
        results = len(responses)
        # for response in responses:
        #     results.append(await response.json())

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(get_symbols())

end = time.time()
print(f'it took {end-start} seconds to make {len(symbols)} API calls')
print('You did it!')