"""
Class Methods Examples
Shows how instance methods work and interact with object state.
"""


# Example 1: A basic instance method
class Greeter:
    """A class that greets people."""

    def __init__(self, name):
        self.name = name

    def greet(self):
        """Prints a greeting using the instance's name."""
        print(f"Hello, my name is {self.name}.")


greeter = Greeter("Nursultan")
greeter.greet()


# Example 2: A method that modifies the object's state
class Counter:
    """A class that keeps track of a count."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increases the count by one."""
        self.count += 1


counter = Counter()
counter.increment()
counter.increment()
counter.increment()
print(f"Counter value: {counter.count}")


# Example 3: A method that returns a computed value
class Circle:
    """A class representing a circle with a given radius."""

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        """Returns the area of the circle."""
        return 3.14159 * (self.radius ** 2)


circle = Circle(3)
print(f"Circle area: {circle.get_area():.2f}")


# Example 4: A method calling another method of the same object
class Invoice:
    """A class representing an invoice with tax calculation."""

    def __init__(self, amount):
        self.amount = amount

    def calculate_tax(self):
        """Calculates 12% tax on the amount."""
        return self.amount * 0.12

    def get_total(self):
        """Returns the total amount including tax, using calculate_tax()."""
        return self.amount + self.calculate_tax()


invoice = Invoice(100)
print(f"Total with tax: {invoice.get_total():.2f}")
