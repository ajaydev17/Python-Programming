# Python handles exceptions using try-except block, which allows you to catch and handle runtime
# exceptions gracefully. The try block contains the code that might raise an exception and if an exception
# occurs, control is transferred to the exception block where the exception can be handled without crashing
# the program. You can also use else statements (to execute code if no exception occurs) and finally
# (to execute code regardless of whether an exception occurs) with try-except structure.


try:
    # This code might raise a ValueError if the input is not a number
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("The result is:", result)
finally:
    print("This code will always be executed.")