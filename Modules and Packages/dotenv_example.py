"""
To securely access environment variables in Python, use the os.environ dictionary. For
added security and convenience in managing different environments, use a .env file with
the -dotenv library. This approach allows you to load environment-specific values without
exposing sensitive information in code.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the variables
database_url = os.getenv('DATABASE_URL')

api_key = os.getenv('API_KEY')
print("Database URL:", database_url)
print("API Key:", api_key)