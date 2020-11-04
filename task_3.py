"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import cProfile
import timeit

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

print(cProfile.run('revers_3(123456789)'),">>>3")
print(cProfile.run('revers_2(123456789)'),">>>2")
print(cProfile.run('revers(123456789)'), ">>>1")

print(timeit.timeit('revers_3(123456789)', setup="from __main__ import revers_3", number=10000),">>>3")
print(timeit.timeit('revers_2(123456789)', setup="from __main__ import revers_2", number=10000),">>>2")
print(timeit.timeit('revers(123456789)', setup="from __main__ import revers", number=10000),">>>1")
#САМЫЙ БЫСТРЫЙ - revers_3 ТАК КАК ЗДЕСЬ ВЫПОЛНЯЕТЬСЯ ТОЛЬКО ОПЕРАЦИЯ ПРЕОБРАЗОВАНИЯ В СТРОКУ И ОБРАТНЫЙ СРЕЗ
#САМЫМ МЕДЛЕННЫМ ЯВЛЯЕТЬСЯ revers ТАК КАК ЗДЕСЬ ПРИМЕНЕНА РЕКУРСИЯ И ФУНКЦИЯ ВЫЗЫВАЕТ СЕБЯ 10 РАЗ ЕСЛИ ЧИСЛО СОСТОИТ ИЗ 9 ЦИФР
#СРЕДНИЙ АЛГОРИТМ ЯВЛЯЕТЬСЯ ЦИКЛОМ ПО ВИДИМУ НЕ ТАКИМ БЫСТРЫМ ЧТОБЫ БЫТЬ БЫСТРЕЕ СРЕЗОВ