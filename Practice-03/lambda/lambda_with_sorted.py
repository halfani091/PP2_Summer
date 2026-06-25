"""
Lambda with sorted() Examples
Shows how lambda functions provide custom sort keys with sorted().
"""

# Example 1: Sorting a list of tuples by the second element
pairs = [(1, "banana"), (2, "apple"), (3, "cherry")]
sorted_by_fruit = sorted(pairs, key=lambda pair: pair[1])
print(f"Sorted by fruit name: {sorted_by_fruit}")


# Example 2: Sorting a list of dictionaries by a specific key
employees = [
    {"name": "Tom", "salary": 3000},
    {"name": "Mia", "salary": 5000},
    {"name": "Liu", "salary": 4000},
]
sorted_by_salary = sorted(employees, key=lambda emp: emp["salary"])
print(f"Sorted by salary: {sorted_by_salary}")


# Example 3: Sorting strings by their length
words = ["banana", "kiwi", "fig", "watermelon"]
sorted_by_length = sorted(words, key=lambda word: len(word))
print(f"Sorted by length: {sorted_by_length}")


# Example 4: Sorting in descending order using reverse=True
numbers = [4, 1, 7, 3, 9, 2]
sorted_descending = sorted(numbers, key=lambda x: x, reverse=True)
print(f"Sorted descending: {sorted_descending}")
