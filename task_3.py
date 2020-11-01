"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
st = input("input word>>> ").lower()
dsd=set()
import itertools
import hashlib

items = st
for i in range(1,len(items)):
    for combination in itertools.combinations(st, i):
        if ''.join(list(combination)) in st:
            dsd.add(hashlib.sha256(''.join(list(combination)).encode()).hexdigest())
print(len(dsd))
print(dsd)


########################way2########################################

def cut_and_dig(word,ls):
    if len(word) == 1:
        ls.append(word)
        return None
    ls.append(word[1:])
    ls.append(word[:-1])
    one = word[1:]
    two = word[:-1]
    return  cut_and_dig(one,ls), cut_and_dig(two,ls)
ls = []
cut_and_dig(st,ls)
print(set(hashlib.sha256(i.encode()).hexdigest() for i in ls ))
