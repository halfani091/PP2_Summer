# ============================================================
# Practice 4 — Python Math Library
# ============================================================

import math

# ----------------------------------------------------------
# Task 1: Convert degrees to radians
# ----------------------------------------------------------
print("=== Task 1: Degree to Radian ===")
degree = float(input("Input degree: "))
radian = math.radians(degree)
print(f"Output radian: {radian:.6f}")

# ----------------------------------------------------------
# Task 2: Area of a trapezoid
# Area = ((base1 + base2) / 2) * height
# ----------------------------------------------------------
print("\n=== Task 2: Area of a Trapezoid ===")
height = float(input("Height: "))
base1  = float(input("Base, first value: "))
base2  = float(input("Base, second value: "))
area_trapezoid = ((base1 + base2) / 2) * height
print(f"Expected Output: {area_trapezoid}")

# ----------------------------------------------------------
# Task 3: Area of a regular polygon
# Area = (n * s^2) / (4 * tan(pi / n))
# ----------------------------------------------------------
print("\n=== Task 3: Area of a Regular Polygon ===")
n_sides = int(input("Input number of sides: "))
side_len = float(input("Input the length of a side: "))
area_polygon = (n_sides * side_len ** 2) / (4 * math.tan(math.pi / n_sides))
print(f"The area of the polygon is: {area_polygon:.0f}")

# ----------------------------------------------------------
# Task 4: Area of a parallelogram
# Area = base * height
# ----------------------------------------------------------
print("\n=== Task 4: Area of a Parallelogram ===")
base   = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area_parallelogram = base * height
print(f"Expected Output: {area_parallelogram}")
