def sum_geometric_progression(a1, t, alim):
    """
    Обчислює суму елементів зменшуваної геометричної прогресії
    a(k+1) = a(k) * t, де 0 < t < 1,
    поки елементи більші за alim.
    """
    if not (0 < t < 1):
        raise ValueError("Крок прогресії t повинен бути між 0 та 1 (0 < t < 1).")
    if alim >= a1:
        raise ValueError("Границя alim повинна бути меншою за початковий елемент a1.")
    total = 0
    current = a1
    while current > alim:
        total += current
        current *= t
    return total

result = sum_geometric_progression(a1 = 40, t = 0.5, alim = 8)
print("Сума елементів, більших за alim:", result)
