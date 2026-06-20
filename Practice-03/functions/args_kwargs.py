"""
*args and **kwargs Examples
Demonstrates variable-length arguments in Python functions.
"""


# Example 1: Using *args to accept any number of positional arguments
def sum_all(*numbers):
    """Sums an arbitrary number of numeric arguments."""
    total = 0
    for number in numbers:
        total += number
    return total


print(f"Sum: {sum_all(1, 2, 3)}")
print(f"Sum: {sum_all(10, 20, 30, 40)}")


# Example 2: Using **kwargs to accept any number of keyword arguments
def print_profile(**details):
    """Prints arbitrary keyword arguments as a profile."""
    for key, value in details.items():
        print(f"{key}: {value}")


print_profile(name="Dana", age=21, city="Almaty")


# Example 3: Combining *args and **kwargs in the same function
def build_report(title, *sections, **metadata):
    """Builds a report title, a list of sections, and extra metadata."""
    print(f"Report: {title}")
    print("Sections:", sections)
    print("Metadata:", metadata)


build_report("Sales Report", "Intro", "Numbers", "Summary", author="Alex", year=2026)


# Example 4: Unpacking lists/dicts when calling a function
def create_user(username, email, role):
    """Creates a user profile from individual fields."""
    print(f"User '{username}' ({email}) registered as {role}.")


user_data_list = ["jdoe", "jdoe@example.com"]
create_user(*user_data_list, role="admin")  # unpacking a list with *

user_data_dict = {"username": "asmith", "email": "asmith@example.com", "role": "editor"}
create_user(**user_data_dict)  # unpacking a dict with **
