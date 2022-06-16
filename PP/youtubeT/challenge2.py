'''
build a coroutine called fetch_data which simulates the collection
of data from a network database. assume that takes a few secs. it
should return a dict {"data":100}. next, build a new coroutine which
counts down from 10 to 1. using await, have each number print to
the screen every 2 sec. finally build a coroutine called main()
and run fetch_data and the countdown concurrently. print the data 
thah is returned from fetch_data whilst also counting down from 10
'''

import asyncio

# Task 1
async def fetch_data():
    print("fetching data...")
    await asyncio.sleep(2)
    print('data returned...')
    return {"data":100}

# Task 2
async def countdown():
    for i in range(10, 0, -1):
        print(i)
        await asyncio.sleep(2)

async def main():
    x = asyncio.create_task(fetch_data())
    y = asyncio.create_task(countdown())

    data = await x
    print(data)
    await y

asyncio.run(main())