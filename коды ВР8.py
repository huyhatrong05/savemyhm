def array_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + array_sum(arr[1:])

# Пример использования
print(array_sum([1, 2, 3, 4, 5]))  # Вывод: 15
