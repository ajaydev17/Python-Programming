"""
A session in Python’s requests library is a way to persist parameters, such as headers or
cookies, across multiple requests. A session is helpful in scenarios where you need to
maintain a logged-in state or reuse configurations across requests. Sessions are managed
using requests.Session(), reducing redundancy and improving performance
"""

import requests

# Create a session
session = requests.Session()

# Define custom headers
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "Authorization": "Bearer <token>"
}

# Set custom headers for the session
session.headers.update(headers)

# Making multiple requests with the same session
response1 = session.get("https://api.example.com/profile")
response2 = session.get("https://api.example.com/settings")

# Displaying responses
print("Profile Data:", response1.json())
print("Settings Data:", response2.json())

# Make a GET request using the session
response = session.get("https://httpbin.org/headers")

print(response.json())

