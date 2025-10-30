order_dict = {'ascending': 0, 'descending': 1}

def check_sorted_array(arr, order_key):
    """
    Перевіряє, чи всі елементи arr є цілими числами
    та чи відсортовані у заданому порядку.

    arr: список чисел
    order_dict: {'ascending': 0, 'descending': 1}
    order_key: ключ словника (0 або 1), що вказує порядок
    """
    if not all(isinstance(x, int) for x in arr):
        return False
    order = order_dict.get(order_key)
    if order not in (0, 1):
        raise ValueError("Неправильний ключ порядку сортування")
    match order:
        case 0:
            return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
        case 1:
            return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

def transform_sorted_array(arr, order_key):
    """
    Замінює значення кожного елемента масиву сумою елемента та його індекса,
    якщо масив відсортований у заданому порядку.
    """
    if not check_sorted_array(arr, order_key):
        return arr
    return [value + index for index, value in enumerate(arr)]

asc_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 20]
print(transform_sorted_array(asc_arr, 'ascending'))
print(transform_sorted_array(asc_arr, 'descending'), "\n")

desc_arr = [20, 17, 15, 13, 11, 9, 7, 5, 3, 1]
print(transform_sorted_array(desc_arr, 'ascending'))
print(transform_sorted_array(desc_arr, 'descending'), "\n")

unorg_arr = [20, 1, 17, 3, 15, 5, 13, 7, 11, 9]
print(transform_sorted_array(unorg_arr, 'ascending'))
print(transform_sorted_array(unorg_arr, 'descending'))