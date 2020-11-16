"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import random
from timeit import timeit

rand_list = [(random()*50) for i in range(500)]    #random() * 50
print(rand_list)


def merge_sort(ar):
    if len(ar) > 1:
        center = len(ar)//2
        left = ar[:center]
        right = ar[center:]
        merge_sort(left)
        merge_sort(right)
        i, j, k, = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                ar[k] = left[i]
                i += 1
            else:
                ar[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            ar[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            ar[k] = right[j]
            j += 1
            k += 1
        return ar


print(merge_sort(rand_list))
print(timeit('merge_sort(rand_list)',"from __main__ import merge_sort,rand_list",number=10000))