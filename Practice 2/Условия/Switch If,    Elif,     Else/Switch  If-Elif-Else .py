day = 3
if day == 1: print("Понедельник")
elif day == 2: print("Вторник")
elif day == 3: print("Среда")
elif day == 4: print("Четверг")
elif day == 5: print("Пятница")
elif day == 6: print("Суббота")
elif day == 7: print("Воскресенье")
else: print("Неверный день")





command = "start"
if command == "start":
    print("Запуск")
elif command == "stop":
    print("Остановка")
elif command == "pause":
    print("Пауза")
elif command == "status":
    print("Проверка статуса")
else:
    print("Неизвестная команда")





day = 3
match day:
    case 1: print("Понедельник")
    case 2: print("Вторник")
    case 3: print("Среда")
    case 4: print("Четверг")
    case 5: print("Пятница")
    case 6: print("Суббота")
    case 7: print("Воскресенье")
    case _: print("Неверный день")






category = "gold"
price = 1000
if category == "bronze": discount = 0.05
elif category == "silver": discount = 0.10
elif category == "gold": discount = 0.20
elif category == "platinum": discount = 0.30
else: discount = 0
print("Цена:", price * (1 - discount))