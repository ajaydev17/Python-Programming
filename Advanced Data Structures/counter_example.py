"""
The Counter class is a specialized dictionary for counting hashable objects. Hashable objects
(like strings, numbers, tuples) can be counted with ease by simply creating a Counter from
an iterable (e.g., a list or string). It’s particularly useful for counting occurrences, which is often
needed in applications like word frequency analysis, data summarization, or character
frequency in text analysis.
"""

from collections import Counter

# Example of counting word occurrences
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(words)
print(counter) # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})


# Finding the most common word
most_common_word = counter.most_common(1)
print(most_common_word) # Output: [('apple', 3)]