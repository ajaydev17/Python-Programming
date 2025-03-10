"""
The requests library in Python handles sessions and cookies using requests.Session(),
which maintains persistent parameters and cookies across multiple requests. Cookies are
automatically stored within a session and sent with subsequent requests to the same
domain, making it useful for authentication and maintaining session data.
"""

import requests

# Create a session object
session = requests.Session()

# logging in to set the session cookies
login_data = {"username": "admin", "password": "admin"}
response = session.post("https://httpbin.org/post", data=login_data)

# Accessing a protected page
response = session.get("https://httpbin.org/cookies")
print("Cookies:", response.json())

# print the cookies
print("Cookies:", session.cookies)