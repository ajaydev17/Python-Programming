"""
Encapsulation restricts access to certain attributes and methods, protecting an object’s
internal state. In Python, attributes can be made "protected" by prefixing them with a single
underscore (_protected) or "private" with double underscores (__private). Protected
attributes signal that they shouldn’t be accessed directly outside the class, and private
attributes are name-mangled, making it difficult to access them outside the class.
"""

class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number # protected attribute
        self.__balance = balance # private attribute

    def get_balance(self):
        return self.__balance