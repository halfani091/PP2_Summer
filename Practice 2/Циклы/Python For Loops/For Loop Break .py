nums = [4, 7, -3, 9, -1, 2]
for n in nums:
    if n < 0:
        print("Первый отрицательный:", n)
        break




nums = [5, 12, 8, 20, 3, 15]
total = 0
for n in nums:
    total += n
    if total > 30:
        print("Лимит! Сумма:", total)
        break



words = ["кот", "пёс", "рыба", "хомяк"]
for i, word in enumerate(words):
    if word == "рыба":
        print(f"Найдено на позиции {i}")
        break        