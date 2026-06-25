age = 20
is_adult = age >= 18
not_senior = age < 65
print(is_adult)    # True
print(not_senior)  # True

score = 85
print(score >= 90)  # False
print(score >= 70)  # True
print(score >= 50)  # True

print(1 < 5 < 10)    # True
print(10 < 5 < 20)   # False (10 < 5 — ложь)
print(1 <= 1 <= 1)   # True

print("10 > 5:", 10 > 5)   # True
print("3 == 3:", 3 == 3)   # True
print("7 != 7:", 7 != 7)   # False

print("apple" == "apple")   # True
print("apple" == "Apple")   # False
print("banana" > "apple")   # True (b > a)