"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""



def know_time(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end - start))

    return wrapper


@know_time
def fullfill_ls(n = 10000000):
    array_py = []
    for i in range(n):
        array_py.append(i)
    return array_py

@know_time
def fullfill_dict(n = 10000000):
    dictionary = {}
    for i in range(n):
        dictionary.setdefault(i)
    return dictionary


print("ls",fullfill_ls())

fullfill_dict()





