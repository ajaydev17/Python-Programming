"""
FastAPI uses Pydantic, a data validation library, to validate and parse request data by
defining data models with type hints. These models are Python classes that specify the
expected data structure for incoming requests. Pydantic ensures that data adheres to the
specified types and constraints, raising validation errors automatically when data does not
match the model requirements.
The benefits of using Pydantic with FastAPI include:

    ● Automatic Validation: FastAPI automatically checks incoming data against the
    model, ensuring data consistency and reducing the need for manual checks.
    ● Data Serialization and Parsing: Pydantic parses data into the expected types,
    converting data like strings to integers or dates when necessary.
    ● Enhanced Documentation: The models created with Pydantic are directly used in
    OpenAPI documentation, making the API self-documenting and easier to
    understand.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for request data
class Item(BaseModel):
    name: str
    price: float
    is_in_stock: bool = True


@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price, "is_in_stock": item.is_in_stock}

# Example POST request body:
# {
# "name": "Sample Item",
# "price": 19.99,
# "is_in_stock": true
# }