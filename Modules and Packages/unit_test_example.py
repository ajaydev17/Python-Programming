"""
The unittest module is a built-in Python library for writing test cases and verifying code
functionality. A unittest.TestCase class can be used to define test methods for a module’s
functions, ensuring they work as expected. Each test method should start with test_, and
assert methods check specific conditions.
"""

import unittest
from my_module import add

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)


if __name__ == "__main__":
 unittest.main()

 """
 Running this script executes the tests and outputs the results. Unit testing helps identify
issues early and ensures your module behaves as expected under different scenarios.
 """