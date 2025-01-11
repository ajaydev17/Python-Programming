# It is an anonymous function, simple, single line function that are defined using the lambda keyword
# instead of def keyword. They can have any number of parameters but are limited to a single expression,
# which is automatically returned.

square = lambda x: x ** 2
print(square(5))

# Commonly used in functional programming constructs such as map(), filter(), and reduce()

# using map()
numbers = [1, 2, 3]
squares = map(lambda x: x ** 2, numbers)
print(list(squares))

# using filter()
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

# using reduce()
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# lambda functions in sorting
students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 95},
]

# Sort students by score in descending order
sorted_students = sorted(students, key=lambda student: student['score'], reverse=True)
print(sorted_students)

# lambda functions in list comprehension
numbers = [1, 2, 3, 4]
squared = [(lambda x: x**2)(n) for n in numbers]
print(squared)  # Output: [1, 4, 9, 16]


