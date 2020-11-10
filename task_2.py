"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
class Hexdigit:
    def __init__(self,num ):
        self.base =  {
        "A" : 10,
        "B" : 11,
        "C" : 12,
        "D" : 13,
        "E" : 14,
        "F" : 15,
        "0" :  0,
        "1" :  1,
        "2" :  2,
        "3" :  3,
        "4" :  4,
        "5" :  5,
        "6" : 6 ,
        "7" : 7 ,
        "8" : 8,
        "9" : 9
        }
        self.num = [i.upper() for i in num]

    def __str__(self):
        return str(self.num)
    def todecimal(self, hlist,n=0):
        if len(hlist)<=0:
            return 0

        r=(self.base[hlist.pop()] * 16 ** n)
        return r + self.todecimal(hlist,n = n+1)
    def __add__(self, other):
        res = self.todecimal(self.num.copy()) + other.todecimal(other.num.copy())

        return Hexdigit(hex(res)[2:])
    def __mul__(self, other):
        res = self.todecimal(self.num.copy()) * other.todecimal(other.num.copy())
        return Hexdigit(hex(res)[2:])
    def __sub__(self, other):
        res = self.todecimal(self.num.copy()) - other.todecimal(other.num.copy())
        return Hexdigit(hex(res)[2:])
    def __truediv__(self, other):
        res = self.todecimal(self.num.copy()) / other.todecimal(other.num.copy())
        return Hexdigit(hex(round(res))[2:])


hexone = Hexdigit("C4F")
hextwo = Hexdigit('A2')
print(hexone/hextwo)
print(hexone*hextwo)
print(hexone-hextwo)
print(hexone+hextwo)

########################################################CollectionsWAY#################################################