"""
Regular expressions (regex) provide a way to define patterns for string matching and
validation. The re module in Python offers functions like match, search, and full match to
check if a string conforms to a specific format, such as an email address or phone number.
"""

import re

# validating email addresses
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = 'test@example.com'

if re.match(email_pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")