"""
Lambda with map() Examples
Shows how lambda functions transform data when used with map().
"""

numbers = [1, 2, 3, 4, 5]

# Example 1: Squaring each number in a list using map() and lambda
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")


# Example 2: Converting a list of strings to uppercase
words = ["python", "java", "kotlin"]
uppercase_words = list(map(lambda word: word.upper(), words))
print(f"Uppercase words: {uppercase_words}")


# Example 3: Using map() with two iterables at the same time
list_a = [1, 2, 3]
list_b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, list_a, list_b))
print(f"Element-wise sums: {sums}")


# Example 4: Comparing map() + lambda with an equivalent list comprehension
doubled_map = list(map(lambda x: x * 2, numbers))
doubled_comprehension = [x * 2 for x in numbers]
print(f"map() result: {doubled_map}")
print(f"List comprehension result: {doubled_comprehension}")
