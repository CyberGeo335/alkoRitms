"""
Главное для бинарного поиска:
    - гранциы + mid
    - если:
        - guess > target, то  mid - 1
        - guess < target, то  mid + 1

"""

def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None




if __name__ == '__main__':
    my_list = list(range(0, 100+1))
    print(my_list)
    #my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(my_list, 3))
