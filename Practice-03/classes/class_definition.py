"""
Class Definition Examples
Demonstrates how to define classes and create objects in Python.
"""


# Example 1: A basic class with no methods, attributes set after creation
class Car:
    """A simple class representing a car."""
    pass


my_car = Car()
my_car.brand = "Toyota"
my_car.color = "blue"
print(f"My car is a {my_car.color} {my_car.brand}.")


# Example 2: A class with a method
class Dog:
    """A class representing a dog that can bark."""

    def bark(self):
        """Makes the dog bark."""
        print("Woof! Woof!")


my_dog = Dog()
my_dog.bark()


# Example 3: Creating multiple objects from the same class
class Student:
    """A class representing a student."""

    def say_hello(self):
        """Prints a greeting from the student."""
        print("Hello, I am a student.")


student_one = Student()
student_two = Student()
student_one.say_hello()
student_two.say_hello()


# Example 4: A class used purely as a data holder
class Point:
    """A simple data holder class representing a 2D point."""
    pass


point_a = Point()
point_a.x = 10
point_a.y = 20
print(f"Point A is located at ({point_a.x}, {point_a.y})")
