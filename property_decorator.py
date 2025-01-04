"""
Properties in Python allow you to define getter, setter, and deleter methods for private
attributes. Using the @property decorator, you can control access to private attributes,
making it possible to enforce data validation or restrictions while maintaining a simple
attribute-like syntax for the user.
"""

class Product:

    def __init__(self, price):
        self._price = price

    # @property getter method for price
    @property
    def price(self):
        return self._price

    # @price setter method for price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


product = Product(50)
print(product.price)  # Output: 50

product.price = 20
print(product.price)  # Output: 20

# This approach encapsulates the private _price attribute, allowing controlled access with
# validation via the price property.