"""
To handle secure HTTP requests in Python, you can use the requests library, which supports
HTTPS out of the box. For more advanced SSL configurations, such as custom certificates or
disabling verification, use the verify parameter in requests. For self-signed certificates, you
can pass the path to the certificate or set verify=False (only in a controlled, non-production
environment).
"""

import requests

# Making a secure HTTPS request with SSL verification
response = requests.get("https://example.com", verify=True)

# Handling requests with a custom certificate
response = requests.get("https://self-signed.com", verify="/path/to/cert.pem")

# Disabling verification (not recommended for production)
response = requests.get("https://example.com", verify=False)
print("Response:", response.text)
