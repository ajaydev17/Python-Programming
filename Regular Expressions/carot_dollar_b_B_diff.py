"""
Anchors ^ and $ control where the pattern appears in the string, while \b and \B
manage word boundaries:
    ● ^ matches the start of the string, ensuring the pattern only matches at the beginning.
    ● $ matches the end of the string, ensuring the pattern only matches at the end.
    ● \b represents a word boundary and is useful for matching standalone words or
    patterns that occur at the edge of a word.
    ● \B represents a non-word boundary, meaning the pattern occurs within a word or
    character sequence, not at the start or end.
    Using these in combination helps control the placement and context of matches.
"""

import re

text = "apple applesauce apple"

pattern = r'\bapple\b'
matches = re.findall(pattern, text)
print(matches) # Output: ['apple']