n = 7
if n % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")

age = 16
if age >= 18:
    print("Совершеннолетний")
else:
    print("Несовершеннолетний, осталось лет:", 18 - age)


a = 15
b = 23
if a > b:
    print("Максимум:", a)
else:
    print("Максимум:", b)


username = "admin"
entered = "user"
if username == entered:
    print("Вход выполнен")
else:
    print("Неверный логин. Введено символов:", len(entered))



total = 1500
if total >= 1000:
    discounted = total * 0.9
    print("Цена со скидкой:", discounted)
else:
    print("Цена без скидки:", total)