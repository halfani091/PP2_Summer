"""
Return Values Examples
Shows different ways functions can return data to the caller.
"""


# Example 1: Returning a single value
def square(number):
    """Returns the square of a number."""
    return number ** 2


result = square(6)
print(f"Square of 6 is: {result}")


# Example 2: Returning multiple values as a tuple
def get_min_max(numbers):
    """Returns both the minimum and maximum value from a list."""
    return min(numbers), max(numbers)


smallest, largest = get_min_max([4, 8, 1, 9, 3])
print(f"Smallest: {smallest}, Largest: {largest}")


# Example 3: A function with no explicit return (returns None by default)
def log_message(message):
    """Prints a message but does not return any value."""
    print(f"LOG: {message}")


output = log_message("System started")
print(f"Function output is: {output}")  # None, because there is no return statement


# Example 4: Conditional return statements
def check_age(age):
    """Returns a category string based on the given age."""
    if age < 13:
        return "child"
    elif age < 18:
        return "teenager"
    else:
        return "adult"


print(check_age(10))
print(check_age(15))
print(check_age(25))
