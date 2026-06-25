n = 7
result = "Чётное" if n % 2 == 0 else "Нечётное"
print(result)  # Нечётное


a, b = 10, 20
maximum = a if a > b else b
print(maximum)  # 20



count = 1
print(f"{count} товар" if count == 1 else f"{count} товаров")


x = -7
abs_x = -x if x < 0 else x
print(abs_x)  # 7





is_premium = True
status = "Premium" if is_premium else "Free"
print("Ваш статус:", status)