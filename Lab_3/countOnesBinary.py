user_input = input("Введіть додатне ціле число N: ")

if user_input.isdigit() and int(user_input) > 0:
    result = bin(int(user_input)).count('1')
    print("Кількість одиниць у двійковому поданні:", result)
else:
    print("Помилка: потрібно ввести ціле додатне число.")