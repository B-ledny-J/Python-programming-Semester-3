def arith_progression(a1, t, q):
    """
    Обчислює добуток перших q елементів арифметичної прогресії
    з початковим елементом a1 та кроком t.
    """
    product = 1
    current = a1
    for _ in range(q):
        product *= current
        current += t
    return product

result = arith_progression(a1 = 4, t = 8, q = 5)
print("Результат:", result)