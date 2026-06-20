"""
Basic Functions Examples
This file demonstrates fundamental function definition and calling in Python.
"""


# Example 1: A simple function with no parameters
def greet():
    """Prints a simple greeting message."""
    print("Hello! Welcome to Python functions.")


greet()


# Example 2: A function with one parameter
def greet_person(name):
    """Greets a specific person by name."""
    print(f"Hello, {name}! Nice to meet you.")


greet_person("Aigerim")


# Example 3: A function with multiple parameters
def describe_pet(animal_type, pet_name):
    """Prints information about a pet using two parameters."""
    print(f"I have a {animal_type} named {pet_name}.")


describe_pet("cat", "Whiskers")
describe_pet("dog", "Rex")


# Example 4: A function with a docstring and an internal calculation
def calculate_area(width, height):
    """
    Calculates the area of a rectangle.

    Parameters:
        width (float): the width of the rectangle
        height (float): the height of the rectangle

    Returns:
        float: the area of the rectangle
    """
    area = width * height
    return area


rectangle_area = calculate_area(5, 3)
print(f"The area of the rectangle is: {rectangle_area}")
