def is_in_shaded_area(x, y):
    r = 2
    return x**2 + y**2 <= r**2 and -1 <= y <= 1

x = float(input("Введіть координату x: "))
y = float(input("Введіть координату y: "))
if is_in_shaded_area(x, y):
    print("Точка належить затіненій області.")
else:
    print("Точка не належить затіненій області.")