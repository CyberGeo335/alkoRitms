import random
"""
Главное для сортировки выбором:
    - нициализируем минимальное значение
    - сортируем по мнимуму и добавляем ещё один for лоя сортировки всего массива
"""


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr




if __name__ == '__main__':
    my_list = [random.randint(0, 100) for _ in range(100)]
    print(my_list)
    print(selection_sort(my_list))
