i = 1
while i <= 5:
    print(i)
    i += 1



n = 10
while n > 0:
    print(n)
    n -= 1
print("Пуск!")    



i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print(total)  # 5050


secret = 7
guess = 1
attempts = 0
while guess != secret:
    guess += 1
    attempts += 1
print(f"Найдено: {secret} за {attempts} попыток")
