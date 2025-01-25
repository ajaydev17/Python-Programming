"""
: FastAPI is a modern, high-performance web framework for building APIs with
Python 3.6+ based on standard Python type hints. It is designed to be fast and efficient,
providing support for asynchronous programming with async/await, and it includes
automatic OpenAPI documentation and JSON Schema support.
FastAPI is popular due to its high performance, ease of use, and strong typing support, which
improves code quality and allows for automatic validation of input data using Pydantic.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):