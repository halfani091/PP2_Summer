i = 1
while True:
    if i % 7 == 0:
        print("Первое кратное 7:", i)
        break
    i += 1




n = 100
while n <= 200:
    if n % 7 == 0 and n % 11 == 0:
        print("Найдено:", n)
        break
    n += 1    



total = 0
i = 0
while True:
    i += 1
    total += i
    if total > 50:
        print("Последнее число:", i)
        print("Сумма:", total)
        break    