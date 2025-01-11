# A closure in python is a function that retains access to its enclosing environment, even after the
# outer function has finished executing. Closure occur when an inner function references variables
# from outer function and the outer function returns the inner function. This retained access to the
# outer function's variables enables the inner function to 'remember' the environment in which it was
# created

# Closures are commonly used for data encapsulation, as they allow inner functions to access and modify
# the outer function's variables without exposing them globally.

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Create a closure
closure = outer_function(10)  # 'x' is set to 10

# Call the inner function through the closure
print(closure(5))  # Output: 15
print(closure(7))  # Output: 17