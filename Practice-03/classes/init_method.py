"""
__init__() Constructor Examples
Demonstrates how the constructor initializes object attributes.
"""


# Example 1: __init__ with required arguments
class Person:
    """A class representing a person with a name and age."""

    def __init__(self, name, age):
        self.name = name
        self.age = age


person_one = Person("Aizere", 22)
print(f"{person_one.name} is {person_one.age} years old.")


# Example 2: __init__ with default values
class Pet:
    """A class representing a pet with an optional species."""

    def __init__(self, name, species="dog"):
        self.name = name
        self.species = species


pet_one = Pet("Buddy")
pet_two = Pet("Whiskers", "cat")
print(f"{pet_one.name} is a {pet_one.species}.")
print(f"{pet_two.name} is a {pet_two.species}.")


# Example 3: __init__ with validation logic
class BankAccount:
    """A class representing a bank account with a non-negative balance."""

    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.owner = owner
        self.balance = balance


account = BankAccount("Marat", 1000)
print(f"{account.owner}'s balance is {account.balance}.")


# Example 4: __init__ that calls another method during initialization
class Rectangle:
    """A class representing a rectangle that calculates its area on creation."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.calculate_area()

    def calculate_area(self):
        """Calculates and returns the rectangle's area."""
        return self.width * self.height


rect = Rectangle(4, 5)
print(f"Rectangle area calculated during init: {rect.area}")
