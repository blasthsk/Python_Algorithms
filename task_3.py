"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""
from memory_profiler import profile
@profile()
def fibseq(n):
    if n<=1:
        return 1
    return fibseq(n-1) + fibseq(n-2)


#print(fibseq(10))
""""Создаеться отдельная таблица для каждого вызова функции(20 для чисел фибоначи с n=10)
 поэтому обычный способ профилирования памяти не эффективен"
"""
@profile()
def recurtion(n):
    l =[]
    def fibseq(n):
        if n <= 1:
            return 1
        return fibseq(n-2)+fibseq(n-1)

    for i in range(n):
        l.append(fibseq(i))
    return l

"""Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    18     13.1 MiB     13.1 MiB           1   @profile()
    19                                         def recurtion(n):
    20     13.1 MiB      0.0 MiB           1       l =[]
    21     13.1 MiB      0.0 MiB       35401       def fibseq(n):
    22     13.1 MiB      0.0 MiB       35400           if n <= 1:
    23     13.1 MiB      0.0 MiB       17710               return 1
    24     13.1 MiB      0.0 MiB       17690           return (fibseq(n - 1) + fibseq(n - 2))
    25                                         
    26     13.1 MiB      0.0 MiB          21       for i in range(n):
    27     13.1 MiB      0.0 MiB          20           l.append(fibseq(i))
    28     13.1 MiB      0.0 MiB           1       return l


[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]"""
print(recurtion(20))
"""Определив и вызвав рекурсивную функцию внутри профилируемой получил одну таблицу. Изменений нет так как массив получился небольшой
 но очень много вызовов функции при n = 30  компьютер зависает на долго"""
