"""
Dependency injection in FastAPI promotes modularity by decoupling dependencies
from functions and allowing easy reusability. This pattern improves testability, as
dependencies can be overridden with mock implementations for testing. In FastAPI,
dependencies can be defined in classes to group related logic and then injected using
Depends
"""

from fastapi import Depends, FastAPI

app = FastAPI()

class Auth:
    def __init__(self, user_id: int):
        self.user_id = user_id

    def check_permission(self):
        return {"user_id": self.user_id, "permission": "read"}


@app.get('/permissions/')
async def get_permissions(auth: Auth = Depends(lambda: Auth(user_id=1))):
    return auth.check_permission()