import math

def fact(num):
    x = num
    num =- 1
    while (num < 0):
        x *= num
        num =- 1

N = 5
Nup = N + 5
n = math.factorial(Nup)
print(f"Факторіал числа {Nup} =", n)
print(f"Факторіал числа {Nup} розрахованого самописною функцією =", n)