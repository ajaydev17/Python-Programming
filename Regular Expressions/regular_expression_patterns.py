"""
These shorthand character classes are used to match specific types of characters in
a concise way:
    ● \w matches any word character, including uppercase letters (A-Z), lowercase letters
    (a-z), digits (0-9), and the underscore (_). This is useful for matching variable names,
    usernames, or other text patterns with alphanumeric characters.
    ● \W matches any non-word character, which includes punctuation, spaces, and special
    characters (anything except letters, digits, and underscores).
    ● \d matches any digit from 0 to 9, often used when working with numbers or
    validating numeric input.
    ● \D matches any non-digit, including letters, punctuation, and whitespace.
    ● \s matches any whitespace character, like spaces, tabs, and newlines, which is useful
    for separating words or tokens.
    ● \S matches any non-whitespace character.
"""