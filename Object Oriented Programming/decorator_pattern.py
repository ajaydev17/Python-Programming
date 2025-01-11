"""
The decorator pattern allows you to dynamically add responsibilities to objects. In Python, it
can be implemented using functions or classes to wrap additional functionality around a
core object, without modifying its structure directly
"""

class Coffee:

    def cost(self):
        return 5

class MilkDecorator:

    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator:

    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

coffee = Coffee()
coffee_with_milk = MilkDecorator(coffee)
coffee_with_sugar = SugarDecorator(coffee_with_milk)
print(coffee_with_sugar.cost())  # Outputs: 8
