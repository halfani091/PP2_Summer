"""
super() Function Examples
Demonstrates how super() is used to call methods from the parent class.
"""


# Example 1: Using super().__init__() to call the parent constructor
class Person:
    """A general person class."""

    def __init__(self, name):
        self.name = name


class Student(Person):
    """A student class that extends Person using super()."""

    def __init__(self, name, student_id):
        super().__init__(name)  # calls Person's __init__
        self.student_id = student_id


student = Student("Dias", "S12345")
print(f"{student.name} has student ID {student.student_id}")


# Example 2: Using super() to call a parent method and then extend it
class Printer:
    """A general printer class."""

    def print_info(self):
        """Prints basic information."""
        print("Printer is ready.")


class ColorPrinter(Printer):
    """A color printer that extends the parent's print_info() method."""

    def print_info(self):
        super().print_info()  # call the parent's version first
        print("Color printing is supported.")


printer = ColorPrinter()
printer.print_info()


# Example 3: Extending parent behavior without fully overriding it
class Account:
    """A general bank account class."""

    def __init__(self, balance):
        self.balance = balance


class SavingsAccount(Account):
    """A savings account that extends Account with an interest rate."""

    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        """Adds interest to the balance."""
        self.balance += self.balance * self.interest_rate


savings = SavingsAccount(1000, 0.05)
savings.add_interest()
print(f"New balance after interest: {savings.balance}")


# Example 4: A chain of super() calls across multiple inheritance levels
class A:
    """The base class."""

    def show(self):
        print("A.show()")


class B(A):
    """Middle class extending A."""

    def show(self):
        super().show()
        print("B.show()")


class C(B):
    """Top class extending B, which extends A."""

    def show(self):
        super().show()
        print("C.show()")


c = C()
c.show()  # prints A.show(), then B.show(), then C.show()
