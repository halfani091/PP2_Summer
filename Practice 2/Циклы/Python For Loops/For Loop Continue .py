nums = [3, 0, 5, 0, 9, 0, 1]
for n in nums:
    if n == 0:
        continue
    print(n)




for char in "hello world":
    if char not in "aeiou":
        continue
    print(char)



    

for i in range(1, 16):
    if i % 2 == 0:
        continue
    print(f"{i}² = {i**2}")        