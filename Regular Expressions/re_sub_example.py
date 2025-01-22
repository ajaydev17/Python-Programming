"""
The re.sub function performs substitution, replacing occurrences of a pattern with
a specified replacement string. It takes three parameters: the pattern to find, the
replacement text, and the input string. This function is useful for transforming data, such as
replacing placeholders in text, masking sensitive information, or cleaning up strings by
removing unnecessary characters.
"""

import re

text = "I have 123 apples and 456 oranges."

result = re.sub(r'\d+', 'many', text)
print(result) # Output: "I have many apples and many oranges."

"""
Here, \d+ matches any sequence of digits, and re.sub replaces each match with "many,"
effectively masking the numbers in the text.
"""