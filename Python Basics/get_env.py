"""
Environment variables provide a secure way to manage sensitive configuration data, like
database credentials and API keys. Using os.environ, you can access environment variables,
allowing settings to be configured outside the codebase for security and flexibility.
"""

import os

# Setting environment variables
os.environ['DATABASE_URL'] = 'postgresql://user:password@localhost/dbname"'

# Accessing environment variables
database_url = os.environ.get('DATABASE_URL') # os.getenv('DATABASE_URL') also works
print(database_url)