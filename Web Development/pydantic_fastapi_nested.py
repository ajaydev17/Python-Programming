"""
Pydantic is a data validation library used in FastAPI to ensure that data structures
conform to specified types. Pydantic models define fields with type annotations, and FastAPI
automatically validates incoming data against these models, raising errors for any
mismatches.

For complex nested data structures, Pydantic supports nested models, allowing developers
to define hierarchical schemas for handling JSON objects with embedded objects or lists.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic model for nested data

class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class Person(BaseModel):
    name: str
    age: int
    addresses: List[Address]

# fastapi route
@app.post("/person/")
async def create_person(person: Person):
    return {"name": person.name, "age": person.age, "addresses": person.addresses}