a = float(input("Введите выручку фирмы "))  # выручка
b = float(input("Введите издержки фирмы ")) # издержки
if a > b:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {a / b:.2f}")
    c = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {a / c:.2f}")
elif a == b:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")