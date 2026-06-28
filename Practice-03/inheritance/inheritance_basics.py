"""
Inheritance Basics Examples
Demonstrates how child classes inherit attributes and methods from parents.
"""


# Example 1: A simple parent-child relationship
class Vehicle:
    """A general vehicle class."""

    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    """A car class that inherits from Vehicle."""
    pass


my_car = Car("Honda")
print(f"My car brand is {my_car.brand}")  # inherited attribute access


# Example 2: A child class using an inherited method without overriding it
class Animal:
    """A general animal class."""

    def make_sound(self):
        """Prints a generic animal sound."""
        print("Some generic animal sound")


class Cat(Animal):
    """A cat class that inherits make_sound() from Animal."""
    pass


cat = Cat()
cat.make_sound()  # uses the parent's method as-is


# Example 3: A child class that adds a new method of its own
class Shape:
    """A general shape class."""

    def describe(self):
        """Describes the shape."""
        print("This is a shape.")


class Circle(Shape):
    """A circle class that adds its own method in addition to inherited ones."""

    def roll(self):
        """A method unique to Circle."""
        print("The circle is rolling.")


circle = Circle()
circle.describe()  # inherited method
circle.roll()      # new method


# Example 4: Multiple children inheriting from the same parent
class Employee:
    """A general employee class."""

    def __init__(self, name):
        self.name = name


class Developer(Employee):
    """A developer, inherits from Employee."""
    pass


class Designer(Employee):
    """A designer, inherits from Employee."""
    pass


dev = Developer("Yerlan")
designer = Designer("Saniya")
print(f"{dev.name} is a developer")
print(f"{designer.name} is a designer")
