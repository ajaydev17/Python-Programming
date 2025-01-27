"""
: Asynchronous programming in FastAPI allows for non-blocking code execution,
meaning the application can handle multiple tasks concurrently without waiting for each
task to finish before starting the next. This is particularly useful for I/O-bound tasks, such as
database access or network requests, where the application can perform other operations
while waiting.

FastAPI leverages async and await to support asynchronous programming, which improves
performance, reduces latency, and allows for better handling of high-concurrency
applications.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/async_example")
async def async_example():
    await some_io_operation()
    return {"message": "This is an async example"}

async def some_io_operation():
    # Simulate an I/O-bound operation
    import asyncio
    await asyncio.sleep(1)
    return "I/O operation completed"