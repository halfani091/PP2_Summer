"""
Lambda with filter() Examples
Shows how lambda functions select data when used with filter().
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Example 1: Filtering even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")


# Example 2: Filtering strings longer than a given length
words = ["cat", "elephant", "dog", "hippopotamus", "ant"]
long_words = list(filter(lambda word: len(word) > 3, words))
print(f"Words longer than 3 letters: {long_words}")


# Example 3: Filtering out None values from a mixed list
mixed_values = [1, None, 3, None, 5]
clean_values = list(filter(lambda x: x is not None, mixed_values))
print(f"Values without None: {clean_values}")


# Example 4: Filtering a list of dictionaries based on a custom condition
students = [
    {"name": "Anna", "score": 85},
    {"name": "Bob", "score": 45},
    {"name": "Cara", "score": 92},
]
passing_students = list(filter(lambda student: student["score"] >= 60, students))
print(f"Passing students: {passing_students}")
