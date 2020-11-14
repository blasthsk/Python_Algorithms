"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile
import random
@profile()
def mem_mesure_one(n,m):
    array = []
    for i in range(n):
        array.append([random.random() for j in range(m)])
    return array


#mem_mesure_one(500,500)
"""Создавая двоичный массив 500х500 c рандомными числами внутри получил прирост к использованию памяти на 9.9 Mib 
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    18     13.3 MiB     13.3 MiB           1   @profile()
    19                                         def mem_mesure_one(n,m):
    20     13.3 MiB      0.0 MiB           1       array = []
    21     23.1 MiB      0.0 MiB         501       for i in range(n):
    22     23.1 MiB      9.9 MiB      251500           array.append([random.random() for j in range(m)])
    23     23.1 MiB      0.0 MiB           1       return array
    Заметил что прирост отображаеться на втором цикле  """

@profile()
def fack(n):
    f=1
    i = 1
    while i < n:
        f += f * i
        i+=1
    return f

#fack(50000)

"""Вычитывая факториал от 50000 можно получить прирост 1.7 Mib Возвращая только одно число
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    38     13.3 MiB     13.3 MiB           1   @profile()
    39                                         def fack(n):
    40     13.3 MiB      0.0 MiB           1       f=1
    41     13.3 MiB      0.0 MiB           1       i = 1
    42     15.0 MiB      0.0 MiB       50000       while i < n:
    43     15.0 MiB      1.7 MiB       49999           f += f * i
    44     15.0 MiB      0.0 MiB       49999           i+=1
    45     15.0 MiB      0.0 MiB           1       return f
"""
@profile()
def new_words(n):
    s = "abcdefghijklmnopqrstuvwxyz"
    dictionary = {i : [] for  i in s}
    for i in range(n):
       word = ''.join([random.choice(s) for i in range(random.randint(2,30))])
       dictionary[word[0]].append(word)
    return dictionary
new_words(5000)
"""Создав 5 тысяч новых слов из английского алфавита путем рандомных выборов букв и записав их в словарь побуквенно
получил небольшой прирост памяти размером 0,4 Mib
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    61     13.2 MiB     13.2 MiB           1   @profile()
    62                                         def new_words(n):
    63     13.2 MiB      0.0 MiB           1       s = "abcdefghijklmnopqrstuvwxyz"
    64     13.2 MiB      0.0 MiB          29       dictionary = {i : [] for  i in s}
    65     13.6 MiB      0.0 MiB        5001       for i in range(n):
    66     13.6 MiB      0.3 MiB       94662          word = ''.join([random.choice(s) for i in range(random.randint(2,30))])
    67     13.6 MiB      0.1 MiB        5000          dictionary[word[0]].append(word)
    68     13.6 MiB      0.0 MiB           1       return dictionary
"""
