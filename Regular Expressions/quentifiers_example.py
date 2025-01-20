"""
Quantifiers control how many times a specific pattern should match:
    ● {n} specifies exactly n occurrences. For instance, \d{3} will match exactly three
    digits, making it useful for fixed-length patterns like area codes or three-digit codes.
    ● {n,} specifies n or more occurrences. This is helpful when you want a minimum
    count without an upper limit, such as {3,} to require at least three characters.
    ● {n,m} specifies between n and m occurrences. This allows for a variable number of
    matches within a range, ideal for situations like variable-length IDs or codes.
"""

import re

text = "123 4567 89"
pattern = r'\d{2,4}'

matches = re.findall(pattern, text)
print(matches) # Output: ['123', '4567', '89']
