"""
The requests library in Python simplifies making HTTP requests. It provides a
straightforward way to interact with web services via methods like GET, POST, PUT, and
DELETE, allowing data retrieval or submission over the internet. This library manages the
complexities of HTTP headers, cookies, and sessions.
"""

import requests

# Make a GET request
response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())

# Make a POST request
response = requests.post("https://httpbin.org/post", data={"key": "value"})
print(response.status_code)
print(response.json())

