"""
In requests, error handling and retries can be managed using exceptions and custom retry
logic. The requests library raises specific exceptions, such as requests.ConnectionError
and requests.Timeout, for different failure types. Using requests.adapters.HTTPAdapter
with Retry from urllib3, you can configure automatic retries for failed requests.
"""

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


# Retry configuration
session = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount("http://", HTTPAdapter(max_retries=retries))

try:
    response = session.get("https://example.com/api")
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
else:
    print("Request succeeded:", response.text)