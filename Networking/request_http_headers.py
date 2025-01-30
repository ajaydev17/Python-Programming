"""
HTTP headers provide additional context and metadata with HTTP requests and responses.
Headers are key-value pairs, commonly used for authentication (Authorization), data
format (Content-Type), and cookies. In the requests library, headers are set using the
headers parameter, typically as a dictionary.
"""

import requests

# Define the URL
url = "https://httpbin.org/headers"

# Define custom headers
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json"
}

# Make a GET request with custom headers
response = requests.get(url, headers=headers)
print(response.json())

# query parameters
url = "https://httpbin.org/get"

# Define query parameters
params = {
    "key1": "value1",
    "key2": "value2"
}

# Make a GET request with query parameters
response = requests.get(url, params=params)
print(response.json())