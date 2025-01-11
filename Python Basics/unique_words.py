import string

def get_unique_words(words):
    words = words.split(' ')

    unique_words = {word.strip(string.punctuation).lower() for word in words}

    return unique_words