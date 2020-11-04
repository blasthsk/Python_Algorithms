"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
from timeit import Timer

def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g
@memorize
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f"{str(number % 10)}{recursive_reverse(number // 10)}"


t1 = Timer("recursive_reverse(123)", "from __main__ import recursive_reverse")
print(t1.timeit(number=100000))
#Добавив мемоизацию получил результат лучше в 7-8 раз