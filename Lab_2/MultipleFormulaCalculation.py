import math
import sys

def calculate_Y(x, a):
    if x < 0:
        if (a > 0 and x < -2*a) or (a < 0 and x < 2*a):
            return None
        return -a * math.sqrt(1 - (x**2) / (4 * a**2))
    else:
        return (a / 2) * (math.exp(x / a) + math.exp(-x / a))

x = float(input("Введіть x: "))
a = float(input("Введіть a: "))
if a == 0: sys.exit("Помилка: ділення на 0 неможливе.")
Y = calculate_Y(x, a)
if Y is None:
    print("Помилка: підкореневий вираз від’ємний. Обчислення неможливе.")
else:
    print("Y =", Y)