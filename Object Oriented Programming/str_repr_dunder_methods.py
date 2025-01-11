"""
__str__ provides a user-friendly string representation for an object, typically used when
printing it. __repr__ offers a detailed, unambiguous representation for debugging, and
ideally, it should be a valid expression that could recreate the object.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author})"