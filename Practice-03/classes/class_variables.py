"""
Class Variables vs Instance Variables Examples
Demonstrates the difference between variables shared by all instances
and variables unique to each instance.
"""


# Example 1: A class variable shared across all instances
class Animal:
    """A class representing an animal, with a shared 'kingdom' value."""
    kingdom = "Animalia"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable


cat = Animal("Cat")
dog = Animal("Dog")
print(f"{cat.name} belongs to {cat.kingdom}")
print(f"{dog.name} belongs to {dog.kingdom}")


# Example 2: An instance variable overriding a class variable for one object
class Employee:
    """A class representing an employee with a default department."""
    department = "General"  # class variable

    def __init__(self, name):
        self.name = name


manager = Employee("Olga")
manager.department = "Management"  # creates an instance variable, shadows the class one

print(f"Manager's department: {manager.department}")    # instance value
print(f"Default department: {Employee.department}")     # original class value


# Example 3: Using a class variable to count created instances
class Book:
    """A class representing a book, tracking how many books were created."""
    total_books = 0  # class variable shared by all instances

    def __init__(self, title):
        self.title = title
        Book.total_books += 1  # increment the shared counter


book_one = Book("Python Basics")
book_two = Book("Advanced OOP")
print(f"Total books created: {Book.total_books}")


# Example 4: A common pitfall - using a mutable class variable
class ShoppingCart:
    """Demonstrates why mutable class variables can cause unexpected sharing."""
    items = []  # WARNING: shared mutable list across all instances if not handled carefully

    def __init__(self):
        self.items = []  # instance variable correctly shadows the class variable


cart_one = ShoppingCart()
cart_two = ShoppingCart()
cart_one.items.append("Apple")
print(f"Cart one items: {cart_one.items}")
print(f"Cart two items: {cart_two.items}")  # stays empty, each instance has its own list
