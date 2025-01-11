"""
Asynchronous programming allows functions to be paused and resumed, making it useful
for managing I/O-bound operations without blocking the main thread. asyncio is Python’s
library for writing concurrent code using async and await syntax, providing a framework for
coroutines that run in an event loop.
"""

"""
With asyncio, multiple tasks can run "concurrently" within a single thread, improving
efficiency without the need for multi-threading.
"""

"""
This code will run fetch_data twice concurrently
"""

import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    print("Data fetched")

async def main():
    await asyncio.gather(fetch_data(), fetch_data())

asyncio.run(main())