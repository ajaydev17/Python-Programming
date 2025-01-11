"""
Inheritance allows a class to inherit attributes and methods from another class, promoting
code reuse and enabling a hierarchy. Types of inheritance in Python include:
"""

"""
Single Inheritance
In single inheritance, a child class inherits from a single parent class.
"""

class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child!")

obj = Child()
obj.greet()  # Output: Hello from Parent!
obj.greet_child()  # Output: Hello from Child!

"""
Multiple Inheritance
In multiple inheritance, a child class can inherit from more than one parent class.
"""

class Parent1:
    def greet_parent1(self):
        print("Hello from Parent1!")

class Parent2:
    def greet_parent2(self):
        print("Hello from Parent2!")

class Child(Parent1, Parent2):
    def greet_child(self):
        print("Hello from Child!")

obj = Child()
obj.greet_parent1()  # Output: Hello from Parent1!
obj.greet_parent2()  # Output: Hello from Parent2!
obj.greet_child()    # Output: Hello from Child!

"""
Multilevel Inheritance
In multilevel inheritance, a child class inherits from a parent class, and another child class inherits from this child class.
"""

class Grandparent:
    def greet_grandparent(self):
        print("Hello from Grandparent!")

class Parent(Grandparent):
    def greet_parent(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child!")

obj = Child()
obj.greet_grandparent()  # Output: Hello from Grandparent!
obj.greet_parent()       # Output: Hello from Parent!
obj.greet_child()        # Output: Hello from Child!


"""
Hierarchical Inheritance
In hierarchical inheritance, multiple child classes inherit from the same parent class.
"""

class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child1(Parent):
    def greet_child1(self):
        print("Hello from Child1!")

class Child2(Parent):
    def greet_child2(self):
        print("Hello from Child2!")

obj1 = Child1()
obj2 = Child2()

obj1.greet()       # Output: Hello from Parent!
obj1.greet_child1()  # Output: Hello from Child1!
obj2.greet()       # Output: Hello from Parent!
obj2.greet_child2()  # Output: Hello from Child2!


"""
Hybrid Inheritance
Hybrid inheritance is a combination of two or more types of inheritance. It can include combinations like hierarchical + multilevel.
"""

class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child1(Parent):
    def greet_child1(self):
        print("Hello from Child1!")

class Child2(Parent):
    def greet_child2(self):
        print("Hello from Child2!")

class Grandchild(Child1, Child2):
    def greet_grandchild(self):
        print("Hello from Grandchild!")

obj = Grandchild()
obj.greet()           # Output: Hello from Parent!
obj.greet_child1()    # Output: Hello from Child1!
obj.greet_child2()    # Output: Hello from Child2!
obj.greet_grandchild()  # Output: Hello from Grandchild!

"""
Diamond Problem in Multiple Inheritance
The Diamond Problem occurs when a child class inherits from two classes that have a common parent. Python resolves this using the Method Resolution Order (MRO).
"""

class A:
    def greet(self):
        print("Hello from A!")

class B(A):
    def greet(self):
        print("Hello from B!")

class C(A):
    def greet(self):
        print("Hello from C!")

class D(B, C):
    pass

obj = D()
obj.greet()  # Output: Hello from B! (follows MRO: D -> B -> C -> A)
print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]





