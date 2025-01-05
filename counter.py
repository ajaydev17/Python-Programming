from collections import Counter

text = 'Hello, world, hello'
words = text.lower().split(' ')
word_counts = Counter(words)

print(word_counts)