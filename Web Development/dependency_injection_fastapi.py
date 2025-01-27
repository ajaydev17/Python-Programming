"""
Dependency injection in FastAPI allows developers to define reusable dependencies
that can be injected into routes and functions. It is implemented using the Depends class,
which specifies the required dependencies for a function.
Dependency injection is beneficial because it helps manage shared resources, ensures that
dependencies are consistently injected, and promotes modular and testable code by
enabling dependency isolation.
"""

from fastapi import FastAPI, Depends

app = FastAPI()

def get_db_connection():
    # Simulate getting a database connection
    return "DB Connection"

@app.get("/items/")
async def read_items(db: str = Depends(get_db_connection)):
    return {"db_connection": db}