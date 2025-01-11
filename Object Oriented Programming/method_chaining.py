"""
Method chaining allows multiple method calls in a single line by having each method return
self. This technique is commonly used in libraries to make code more concise.
"""

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, number):
        self.result += number
        return self

    def subtract(self, number):
        self.result -= number
        return self


calc = Calculator()
result = calc.add(5).subtract(3).result
print(result)  # Output: 2