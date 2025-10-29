N = 5
numbers = list(range(1, N + 11))

print("Початковий список:", numbers)

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("Змінений список:", numbers)