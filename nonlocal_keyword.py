# The keyword allows you to access a variable in the nearest enclosing scope that is not global.
# This is useful in nested functions, where a variable in the outer function needs to be modified
# by the inner function. Without nonlocal keyword, the inner function would treat any re-assignment
# of the variable as local.

def outer_function():
    outer_var = 10

    def inner_function():
        # Using nonlocal keyword to access outer_var
        nonlocal outer_var

        # if we directly do this without using nonlocal keyword count is treated as a local variable here
        # and throws UnboundLocalError: local variable 'count' referenced before assignment
        # you cant use global keyword here as outer_var is not defined globally.
        outer_var += 5
        print(f"Inner function: outer_var = {outer_var}")

    inner_function()
    print(f"Outer function: outer_var = {outer_var}")