import asyncio
import time
# Coroutine = asynchronous function
async def task1(): 
    print('send first email')
    asyncio.create_task(task2()) # create and start another task 
    await asyncio.sleep(5) # simulating how long until a reply is received
    print('first email reply')

async def task2():
    print('send second email')
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print('second email reply')

async def task3():
    print('send third email')
    await asyncio.sleep(1)
    print('third email reply')

start = time.time()
asyncio.run(task1())
end = time.time()
print(f"{end-start} seconds")