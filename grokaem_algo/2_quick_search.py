import random
"""
Главное для быстрой сортировки:
    - создаём массив меньше 2
    - инициализируем опорное значение и по нему будем сравнивать элементы
    - создаём массив less и greater
    - less: i < pivot -> append в less
    - greater: i < pivot -> append в greater
    - потом рекурсивно проходим
"""

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        # опорный алгоритм
        pivot = array[0]
        # создаём массив less
        less = []
        # идём от первого элемента
        for i in array[1:]:
            # добавляем
            if i < pivot:
                less.append(i)
        # создаём массив greater
        greater = []
        for i in array[1:]:
            if i > pivot:
                greater.append(i)
        return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    my_list = [random.randint(0, 100) for _ in range(100)]
    print(my_list)
    print(quicksort(my_list))
