import math

def Y_value(a, x, alpha):
    if x + a <= 0: raise Exception("Вираз x + a має бути більший за нуль")
    if x < 0.5 * 10 ** (-1.5): raise Exception("Вираз x - 0.5 * 10 ** (-1.5) має бути більшим за нуль")

    num = math.cos(4 * alpha) - (math.log(x + a)) ** 2 * math.exp(x) * x ** 3 - 1.7 * 10 ** 5 * a
    den = x * (x ** 3 + 5) + x ** (a ** 2) - a * math.sqrt(x - 0.5 * 10 ** (-1.5))
    return num / den

print(Y_value(0.5, 3.4, 1.65))