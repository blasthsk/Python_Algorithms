"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

"""

from collections import OrderedDict
import timeit
cd = OrderedDict()
ud = {}

for i in range(100000):
    cd[i] = i**2
    ud[i] = i**2


print(timeit.timeit("cd.get(4)","from __main__ import cd",number=100000))
print(timeit.timeit("ud.get(4)","from __main__ import ud",number=100000))
print( "GEET IT")
def cd_check(cd):
    cd.pop(len(cd)-2)
def ud_check(ud):
    ud.pop(len(ud)-2)

print(timeit.timeit("cd_check(cd)","from __main__ import cd,cd_check",number=5000))
print(timeit.timeit("ud_check(ud)","from __main__ import ud,ud_check",number=5000))
print( "POP IT")
import  random
x = random.random()
def cd_chec(cd):
    cd[x]= x**2
def ud_chec(ud):
    ud[x] = x**2
print(timeit.timeit("cd_chec(cd)","from __main__ import cd_chec,cd,x",number=50000))
print(timeit.timeit("ud_chec(ud)","from __main__ import ud_chec,ud,x",number=50000))
print( "Assign new")

print(timeit.timeit("cd.update(x=x**2)","from __main__ import cd_chec,cd,x",number=50000))
print(timeit.timeit("ud.update(x=x**2)","from __main__ import ud_chec,ud,x",number=50000))
print( "update it")

"После многократной проверки разных методов добавления получения и удаления элементов я заметил что обычный словарь(ud)"
"быстрее чем словарь `упорядочный` из коллекций"