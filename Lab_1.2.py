#Лаб.1 Рівень 2. Варіант 5.

def is_number(value):
    try:
        return float(value)
    except ValueError:
        return None

a = is_number(input("Введіть довжину сторони a: "))
b = is_number(input("Введіть довжину сторони b: "))
c = is_number(input("Введіть довжину сторони c: "))

if a is None or b is None or c is None:
    print("Помилка: Введені значення повинні бути числами.")
elif a <= 0 or b <= 0 or c <= 0:
    print("Помилка: Сторони трикутника повинні бути більше 0.")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Помилка: Трикутника з такими сторонами не існує.")
else:
    if a == b == c:
        print(1)  # рівносторонній
    elif a == b or a == c or b == c:
        print(2)  # рівнобедрений
    else:
        print(3)  # різносторонній
