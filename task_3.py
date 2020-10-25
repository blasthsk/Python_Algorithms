"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""
def mesuare(n, count=0):
    if not n:
        return count
    count += 1
    return mesuare(n//10, count)

def reveresed_num(n):

    if n // 10 == 0:
        digit = n % 10
        return digit * 10**(mesuare(digit)-1)
    digit = n % 10
    return digit * 10**(mesuare(n)-1) + reveresed_num(n//10)


number = int(input("Input your number>>> "))
print(reveresed_num(number))