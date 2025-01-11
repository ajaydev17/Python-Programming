"""
Assertions are debugging tools that help you verify assumptions in code by testing if
specific conditions hold true. The assert statement takes a condition, and if the condition is
True, the program continues. If it’s False, an AssertionError is raised, which helps in
identifying bugs or unexpected conditions during development. Assertions are useful in
testing as they automatically stop execution if an unexpected scenario is detected, allowing
the developer to fix the issue early.
"""

x = -10

# raises AssertionError with message
assert x >= 0, "x must be non-negative"

"""
When an assertion fails, Python raises an AssertionError with an optional message
if provided. The program stops executing immediately unless the error is handled in a try-except block. 
Although assertions are mostly used in testing and debugging, they can be
included in production code but are often disabled for performance reasons. Assertions are
especially useful for validating assumptions in critical areas of code.
"""

try:
    x = -5
    assert x >= 0, "x must be non-negative"
except AssertionError as e:
    print(f"Assertion error: {e}")