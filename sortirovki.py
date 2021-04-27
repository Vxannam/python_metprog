import random

def selection_sort(array): # функция сортировки выбором
    for i in range(len(array) - 1):
        min_id = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_id]:
                min_id = j
        array[i], array[min_id] = array[min_id], array[i]
    return array

def merge_sort(array): # функция сортировки слиянием
    if len(array) > 1:
        middle = len(array) // 2
        left_half = array[:middle]
        right_half = array[middle:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i = i + 1
            else:
                array[k] = right_half[j]
                j = j + 1
            k = k + 1
        while i < len(left_half):
            array[k] = left_half[i]
            i = i + 1
            k = k + 1
        while j < len(right_half):
            array[k] = right_half[j]
            j = j + 1
            k = k + 1
        return array
    return array


def quick_sort(array):  # функция быстрой сортировки
    if len(array) <= 1:
        return array
    else:
        q = random.choice(array)
    less_array = [n for n in array if n < q]
    equal_array = [q] * array.count(q)
    more_array = [n for n in array if n > q]
    return quick_sort(less_array) + equal_array + quick_sort(more_array)