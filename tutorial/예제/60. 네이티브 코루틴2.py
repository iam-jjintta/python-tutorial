
import asyncio


async def f(x):
    y = x ** 2
    return y

async def g(x):
    y = await f(x)
    print(y)


x = 10
loop = asyncio.new_event_loop()
loop.run_until_complete(g(10))
loop.close()
