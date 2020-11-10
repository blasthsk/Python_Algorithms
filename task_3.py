"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
import timeit
from  timeit import Timer
from collections import deque
import cProfile
d = deque(range(101))
l = list(range(101))

def deqappright(d):
    for i in range(100):
        d.append(i)
def deqappleft(d):

    for i in range(100):
        d.appendleft(i)
def  deqpopright(d):
    for i in range(100):
        d.pop()
def deqpopleft(d):

    for i in range(100):
        d.popleft()
################################
def lappright(l):

    for i in range(100):
        l.append(i)

def lappleft(l):

    for i in range(100):
        l.insert(0,i)
def lpopright(l):

    for i in range(100):
        l.pop()
def lpopleft(l):

    for i in range(100):
        l.pop(0)

def middeqapp(d):
    for i in range(100):
      d.insert(int(len(d)/2),i)
def middeqpop(d):
       #d.pop(int(len(d) / 2)) doesn't work
    for j in range(len(d)):
        if d[j] == len(d) / 2:
            d.remove(d[j])

def midlapp(l):
    for i in range(100):
        l.insert(int(len(l) / 2), i)
def midlpop(l):
    l.pop(int(len(l) / 2))
tionary = {
    "Вставка справа deque --" : timeit.timeit("deqappright(d)","from __main__ import deqappright,d",number=100),
    "Вставка справа list --": timeit.timeit("lappright(l)", "from __main__ import lappright,l", number=100),
    "Вставка слева deque --" : timeit.timeit("deqappleft(d)","from __main__ import deqappleft,d",number=100),
    "Вставка слева list --": timeit.timeit("lappleft(l)", "from __main__ import lappleft,l", number=100),
    "Удаление справа deque --" : timeit.timeit("deqpopright(d)","from __main__ import deqpopright,d",number=100),
    "Удаление справа list --": timeit.timeit("lpopright(l)", "from __main__ import lpopright,l", number=100),
    "Удаление слева deque --": timeit.timeit("deqpopleft(d)", "from __main__ import deqpopleft,d", number=100),
    "Удаление слева list --": timeit.timeit("lpopleft(l)", "from __main__ import lpopleft,l", number=100),

    "Вставка в середину deque --": timeit.timeit("middeqapp(d)", "from __main__ import middeqapp,d", number=100),
    "Вставка в середину list --": timeit.timeit("midlapp(l)", "from __main__ import midlapp,l", number=100),

    "Удаление из середины list --": timeit.timeit("midlpop(l)", "from __main__ import midlpop,l", number=1000),
    "Удаление из серидины deque --": timeit.timeit("middeqpop(d)", "from __main__ import middeqpop,d", number=1000)

}
for i in tionary:
    print(i,tionary[i])
"""Сделав замер времени с помощью тайм ит увидел что операции вставки и удаления слева ожидаемо 
эффективней в дэке а удаление из середиины коллекцие проще и эффективней в списке также как и добавление в середину """ \
"""Вставка справа deque -- 0.0009897589999999998
Вставка справа list -- 0.0010900160000000061
Вставка слева deque -- 0.0009160939999999992
Вставка слева list -- 0.064402772
Удаление справа deque -- 0.00045572199999999174
Удаление справа list -- 0.0004352320000000076
Удаление слева deque -- 0.0004852139999999977
Удаление слева list -- 0.12485669299999999
Вставка в середину deque -- 0.022648732999999976
Вставка в середину list -- 0.011516432999999993
Удаление из середины list -- 0.012544718999999982
Удаление из серидины deque -- 2.2047095519999997"""

#       USELESS
#cProfile.run("deqappright(d)")
#cProfile.run("deqappleft(d)")
#cProfile.run("deqpopright(d)")
#cProfile.run("deqpopleft(d)")
#cProfile.run("lappright(l)")
#cProfile.run("lappleft(l)")
#cProfile.run("lpopright(l)")