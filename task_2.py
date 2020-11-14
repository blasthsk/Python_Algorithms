"""
Задание 2.
Предложить еще какие-гибудь варианты (механизмы, библиотеки) оптимизации и
доказать (наглядно, кодом) их эффективность
"""
from numpy import array
from pympler import asizeof
a = [i for i in range(100)]
b = array([i for i in range(100)])

print("Just list - ",asizeof.asizeof(a))
print("Numpy array - ",asizeof.asizeof(b))
"Разница в четыре раза Just list -  4096 Numpy array -  912 "

import sys

import collections
Color = collections.namedtuple("Color",["red","blue","green"])
white  = Color(255,255,255)
wi = Color(255,255,255)
whi  = Color(255,255,255)
whit  = Color(255,255,255)
l = [white,whi,whit,wi]

d={"white":[255,255,255],
    "whte":[255,255,255],
    "hite":[255,255,255],
    "hte":[255,255,255],
   }
"NamedTumle - Алтернатива словарю если нужен доступ по имени экономия памяти в несколько раз"
"""l>>>  88
d>>>   232"""
print("l>>> ",sys.getsizeof(l))
print("d>>>  ",sys.getsizeof(d))