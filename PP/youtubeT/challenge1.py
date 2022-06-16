'''create 3 coroutines named t1, t2, t3.
each should print out the name of the coroutine.
call/run the 1st coroutine and using await have t2 
print out first, t1 second, and t3 last'''

import asyncio

async def t1():
    x = await t2()
    print('t1 completed')

async def t2():
    print('t2 completed')

async def t3():
    x = await t1()
    print('t3 completed')

asyncio.run(t3())