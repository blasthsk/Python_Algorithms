"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
import math
import random
from statistics import median

def func(m):
    n = 2*m + 1
    ar = list(random.choice(range(n))  for i in range(n))
    return ar

m = 50
ar = func(m)

"Предположим что i в массиве являеться медианой и проверим истинность этого утверждения  для каждого i пока это небудет доказано"
middle = int(len(ar)/2) + 1
my_med = None
for i in range(len(ar)):
    arc = ar.copy()
    maybe_median = arc.pop(i)
    left = m
    right = m
    equal = 0
    for j in arc:
        if j < maybe_median and left > 0:
            left -= 1
        elif j > maybe_median and right > 0:
            right -= 1
        elif j == maybe_median:
            equal += 1
    if ((left + right) - equal) == 0:
        my_med = maybe_median

"""Ура в конце концов!!!"""




print(ar)
print(sorted(ar.copy()))
print(median(ar))
print(my_med)