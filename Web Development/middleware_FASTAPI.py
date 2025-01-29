"""
Middleware in FastAPI is a function that runs before or after each request and
response. Middlewares can be used for logging, authentication, handling errors, or modifying
requests and responses globally across the application. In FastAPI, middlewares are
implemented as classes that inherit from BaseHTTPMiddleware.

A middleware processes requests as they come into the application and can modify
responses before they are sent back to the client.
"""

from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

# Custom middleware class
class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # Code to run before the request is processed
        print("Before request processing")

        response = await call_next(request)

        # add custom headers to the response
        response.headers["X-Custom-Header"] = "Custom Value"

        # Code to run after the response is processed
        print("After response processing")

        return response


app.add_middleware(CustomMiddleware)