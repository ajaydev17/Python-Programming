# Generators are special type of iterables, similar to a function, that allows you to iterate through
# sequence values lazily, meaning that they generate values only when required. instead of returning
# all the values at once, generators use the yield keyword to produce a value and pause execution.
# When the generator is iterated over again, it resumes from where it left off saving memory and
# improving performance for large data sets.

def count_up_to(n):
    count = 1

    while count <= n:
        yield count
        count += 1

# using the generator
# the for loop automatically handles the generator by calling next() of generators
for number in count_up_to(10):
    print(number)


# large data processing
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for lines in file:
            yield lines.strip()

# Usage
for line in read_large_file("large_file.txt"):
    print(line)  # Processes one line at a time


# Infinite Sequences
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Usage
fib_gen = fibonacci()
for _ in range(10):  # Print the first 10 Fibonacci numbers
    # next() method will generate the next value
    # When the generator is exhausted (no more values to yield), calling next() raises a StopIteration exception.
    print(next(fib_gen))


# Implementing a custom generator
# We can implement a custom generator by creating a class that overrides the __iter__() and __next__() methods.
# This allows you to have more control over the behavior of your generator.

class NumberGenerator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # The generator is its own iterator

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration  # Signal that the generator is done

# Using the custom generator
gen = NumberGenerator(1, 5)

for num in gen:
    print(num)
    

# Fibonacci series

class FibonacciGenerator:
    def __init__(self, limit):
        self.a, self.b = 0, 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.a < self.limit:
            value = self.a
            self.a, self.b = self.b, self.a + self.b
            return value
        else:
            raise StopIteration

# Using the custom generator
fib_gen = FibonacciGenerator(100)

for fib in fib_gen:
    print(fib)



