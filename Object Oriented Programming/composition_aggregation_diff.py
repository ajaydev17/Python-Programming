"""
Composition and aggregation are both relationships between classes but differ in ownership:

● Composition: If the containing object is destroyed, so are the contained objects
(strong relationship).

● Aggregation: The contained objects can exist independently of the containing object
(weak relationship).
"""

class Engine:
    pass


class Car:
    def __init__(self):
        self.engine = Engine()    # composition


class Department:
    def __init__(self, employees):
        self.employees = employees  # aggregation


engine = Engine()
car = Car()
employees = ["John", "Jane"]
department = Department(employees)
print(car.engine) # Engine is part of Car (Composition)
print(department.employees) # Employees exist independently of Department (Aggregation)