"""
Futures in Python represent a placeholder for a result that will be available in the
future. They are especially useful in asynchronous programming for handling results that
aren’t immediately available. In asyncio, futures can be awaited, allowing the program to
perform other tasks until the result is ready.

The asyncio.Future class is often used to represent results of asynchronous computations
and can be awaited, making it ideal for non-blocking operations.
"""

import asyncio

async def set_future_result(future):
    await asyncio.sleep(2)
    future.set_result("Future is complete")


async def main():
    future = asyncio.Future()
    asyncio.create_task(set_future_result(future))
    result = await future
    print(result)


asyncio.run(main())