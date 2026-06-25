"""
Multiple Inheritance Examples
Demonstrates how a class can inherit from more than one parent class.
"""


# Example 1: Basic multiple inheritance from two classes
class Flyer:
    """A class that gives flying ability."""

    def fly(self):
        print("I can fly.")


class Swimmer:
    """A class that gives swimming ability."""

    def swim(self):
        print("I can swim.")


class Duck(Flyer, Swimmer):
    """A duck that inherits abilities from both Flyer and Swimmer."""
    pass


duck = Duck()
duck.fly()
duck.swim()


# Example 2: Demonstrating Method Resolution Order (MRO)
class Base1:
    def greet(self):
        print("Hello from Base1")


class Base2:
    def greet(self):
        print("Hello from Base2")


class Combined(Base1, Base2):
    """Inherits from both; Python uses MRO to decide which greet() runs."""
    pass


combined = Combined()
combined.greet()  # uses Base1's greet() because it comes first in the MRO
print(f"MRO: {[cls.__name__ for cls in Combined.__mro__]}")


# Example 3: Combining different functionality from multiple parents
class Logger:
    """Provides logging functionality."""

    def log(self, message):
        print(f"LOG: {message}")


class Validator:
    """Provides validation functionality."""

    def validate(self, value):
        return value is not None and value != ""


class FormHandler(Logger, Validator):
    """Combines logging and validation behavior in a single class."""

    def submit(self, value):
        if self.validate(value):
            self.log(f"Submitted value: {value}")
        else:
            self.log("Submission failed: invalid value")


form = FormHandler()
form.submit("Some input")
form.submit("")


# Example 4: Awareness of the "diamond problem"
class Animal:
    def speak(self):
        print("Animal speaks")


class Mammal(Animal):
    def speak(self):
        print("Mammal speaks")


class Bird(Animal):
    def speak(self):
        print("Bird speaks")


class Bat(Mammal, Bird):
    """
    A class facing the diamond inheritance problem:
    both Mammal and Bird inherit from Animal, and Bat inherits from both.
    Python's MRO resolves the conflict by choosing Mammal's speak() first.
    """
    pass


bat = Bat()
bat.speak()  # resolved by MRO: Mammal.speak() wins
print(f"MRO: {[cls.__name__ for cls in Bat.__mro__]}")
