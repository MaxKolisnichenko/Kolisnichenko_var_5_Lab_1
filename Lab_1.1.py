#Лаб.1 Рівень 1. Варіант 5.
import math

def is_number(value):
    try:
        return float(value)
    except ValueError:
        return None

R = is_number(input("Введіть радіус більшої основи (R): "))
r = is_number(input("Введіть радіус меншої основи (r): "))
H = is_number(input("Введіть висоту (H): "))

if R is None or r is None or H is None:
    print("Помилка: Введені значення повинні бути числами.")
elif R <= 0 or r <= 0 or H <= 0:
    print("Помилка: усі значення повинні бути додатними.")
elif R < r:
    print("Помилка: R має бути більшим або рівним r.")
else:
    l = math.sqrt((R - r) ** 2 + H ** 2)  # - обчислення твірної
    S = math.pi * (R**2 + r**2 + l * (R + r))  # - обчислення площі повної поверхні
    print(f"Площа повної поверхні зрізаного конуса: {S:.3f}")

