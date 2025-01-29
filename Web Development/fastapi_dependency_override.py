"""
In FastAPI, dependency overrides allow you to replace dependencies with mock
implementations, making it easier to isolate and test specific functionality without relying on
real services (e.g., databases). This is especially useful for unit tests, where dependencies can
be swapped out for test data.
"""

from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

def get_db():
    return "test_db"

@app.get("/data/")
async def read_data(db: str = Depends(get_db)):
    return {"db": db}


# Dependency override for testing
def override_get_db():
    return "test_db_override"

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# Test the endpoint with the overridden dependency
def test_read_data():
    response = client.get("/data/")
    assert response.status_code == 200
    assert response.json() == {"db": "test_db_override"}