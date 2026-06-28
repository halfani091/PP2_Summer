"""
Lambda Basics Examples
Introduces lambda syntax and compares it with regular functions.
"""


# Example 1: A simple lambda that doubles a number
double = lambda x: x * 2
print(f"Double of 7: {double(7)}")


# Example 2: A lambda with multiple arguments
add = lambda a, b: a + b
print(f"Sum of 4 and 5: {add(4, 5)}")


# Example 3: Using a lambda directly without assigning it to a variable
print(f"Direct lambda call: {(lambda x, y: x * y)(3, 4)}")


# Example 4: Comparing a lambda to an equivalent regular function
def square_regular(x):
    """Regular function that squares a number."""
    return x ** 2


square_lambda = lambda x: x ** 2

print(f"Regular function result: {square_regular(5)}")
print(f"Lambda function result: {square_lambda(5)}")
