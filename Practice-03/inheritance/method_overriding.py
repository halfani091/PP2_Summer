"""
Method Overriding Examples
Demonstrates how a child class can replace or extend a parent method.
"""


# Example 1: Overriding the built-in __str__ method
class Item:
    """A class representing a generic item."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Item: {self.name}"


item = Item("Notebook")
print(item)  # uses the overridden __str__ method


# Example 2: Overriding a method to change its behavior completely
class Shape:
    """A general shape class."""

    def area(self):
        """Default area calculation, returns 0 for a generic shape."""
        return 0


class Square(Shape):
    """A square that overrides area() with its own formula."""

    def __init__(self, side):
        self.side = side

    def area(self):
        """Overridden area calculation specific to a square."""
        return self.side ** 2


square = Square(4)
print(f"Square area: {square.area()}")


# Example 3: Overriding a method but still calling the parent's version
class Employee:
    """A general employee class."""

    def get_salary(self):
        """Returns the base salary."""
        return 3000


class Manager(Employee):
    """A manager that overrides get_salary() but builds on the parent's value."""

    def get_salary(self):
        """Overridden salary calculation that adds a bonus to the base salary."""
        base_salary = super().get_salary()
        return base_salary + 1000


manager = Manager()
print(f"Manager salary: {manager.get_salary()}")


# Example 4: A complete override with no call to the parent method
class Bird:
    """A general bird class."""

    def move(self):
        """Describes how a generic bird moves."""
        print("The bird flies.")


class Penguin(Bird):
    """A penguin that completely overrides move() since penguins cannot fly."""

    def move(self):
        """Overridden move method describing penguin movement."""
        print("The penguin swims instead of flying.")


penguin = Penguin()
penguin.move()
