# ============================================================
# Practice 4 — Python Iterators and Generators
# ============================================================

# ----------------------------------------------------------
# Task 1: Generator that yields squares of numbers up to N
# ----------------------------------------------------------
print("=== Task 1: Squares up to N ===")

def squares_up_to(n):
    """Yields squares of numbers from 1 to N."""
    for i in range(1, n + 1):
        yield i * i

N = 7
print(f"Squares up to {N}:")
for sq in squares_up_to(N):
    print(sq, end=" ")
print()

# ----------------------------------------------------------
# Task 2: Even numbers between 0 and n (comma separated)
# ----------------------------------------------------------
print("\n=== Task 2: Even numbers 0..n (comma separated) ===")

def even_numbers(n):
    """Yields even numbers from 0 to n."""
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter n: "))
result = ",".join(str(x) for x in even_numbers(n))
print(result)

# ----------------------------------------------------------
# Task 3: Numbers divisible by 3 AND 4 between 0 and n
# ----------------------------------------------------------
print("\n=== Task 3: Divisible by 3 and 4 in range 0..n ===")

def divisible_by_3_and_4(n):
    """Yields numbers divisible by both 3 and 4 from 0 to n."""
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n2 = 100
print(f"Divisible by 3 and 4 (0 to {n2}):")
print(list(divisible_by_3_and_4(n2)))

# ----------------------------------------------------------
# Task 4: Generator 'squares' from a to b, tested with for loop
# ----------------------------------------------------------
print("\n=== Task 4: Squares from a to b ===")

def squares(a, b):
    """Yields square of each number from a to b (inclusive)."""
    for i in range(a, b + 1):
        yield i * i

a, b = 3, 8
print(f"Squares from {a} to {b}:")
for val in squares(a, b):
    print(val)

# ----------------------------------------------------------
# Task 5: Generator counting down from n to 0
# ----------------------------------------------------------
print("\n=== Task 5: Countdown from n to 0 ===")

def countdown(n):
    """Yields all numbers from n down to 0."""
    while n >= 0:
        yield n
        n -= 1

start = 10
print(f"Countdown from {start}:")
for val in countdown(start):
    print(val, end=" ")
print()
