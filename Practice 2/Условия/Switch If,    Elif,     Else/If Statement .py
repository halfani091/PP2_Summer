temperature = 35
if temperature > 30:
    print("Жарко!")

    
number = 8
if number % 2 == 0:
    print("Число чётное")


    balance = 1000
price = 500
if balance >= price:
    print("Покупка совершена")
    print("Остаток:", balance - price)


correct_password = "python123"
entered = "python123"
if entered == correct_password:
    print("Доступ разрешён")


age = 20
has_ticket = True
if age >= 18:
    if has_ticket:
        print("Добро пожаловать!")