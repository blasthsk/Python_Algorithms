"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
from timeit import timeit
import random
testlist = [random.randint(-100, 100) for i in range(1000)]
testlisttwo = [i for i in range(1000,0,-1)]

def bubble(ls):
    n = 1
    while n < len(ls):
        for i in range(len(ls)-n):
            if ls[i] < ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
        n += 1
    return ls

def bubble_m(ls):
    n = 1
    while n < len(ls):
        c = 0
        for i in range(len(ls)-n):

            if ls[i] < ls[i+1]:
                ls[i], ls[i+1] = ls[i+1],ls[i]
                c = 1
        if c == 0:
            break
        n += 1
    return ls
"""Оптипизация с прошла успешно функция понимает если список уже отсортирован при каждой итерации цикла while """
#print(bubble_m(testlist.copy()))
#print(testlist)
print(timeit("bubble(testlisttwo.copy())","from __main__ import bubble,testlisttwo",number=100),"---Already sorted")
print(timeit("bubble_m(testlisttwo.copy())","from __main__ import bubble_m,testlisttwo",number=100),"---Already sorted")
#
print(timeit("bubble(testlist.copy())","from __main__ import bubble,testlist",number=100),"---Randomed list")
print(timeit("bubble_m(testlist.copy())","from __main__ import bubble_m,testlist",number=100),"---Randomed list")