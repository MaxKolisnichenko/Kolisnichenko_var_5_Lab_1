#Лаб.1 Рівень 2. Варіант 5.
import random


def generate_series():
    while True:
        series = [random.choice([0, 1, 2]) for _ in range(12)] 
        if sum(series) == 12: 
            return series


for i in range(10):
    series = generate_series()
    print(f"Серія {i+1}: {series}") # - генерація та виведення 10 серій
