"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib
from uuid import  uuid4
class CashImitation:
    def __init__(self):
        self.cash = {}

    def addurl(self,url):
        salt = uuid4().hex
        self.cash[url] = self.createhash( url,salt),salt
        return f'{url} was added to cash'
    def checkurl(self,url):
        if url in self.cash and self.createhash(url,self.cash[url][1]) == self.cash[url][0]:
            return True
        return self.addurl(url)
    def createhash(self,url,salt):
        obj = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
        return obj

"""
Чесно говоря я здесь не совсем понял смысл задания
зачем в одном хранилище хранить и ЮРЛ и ее ХЕШ
я имею в виду зачем задумываться о том что в ХЕШЕ если у нас есть ЮРЛ (то есть при запросе if URL in cash мы так и так получим TRUE)
и где сама страница должна быть НЕПОНЯТНО

и НЕПОНЯТНО еще то что мы генерируем случайное число для соли то есть мы должны хранить полученную однажды соль в 
 хранилище рядом чтобы проверить ХЕШ?
Эти соленные операции пока не совсем понятны
"""

onecash = CashImitation()
onecash.addurl("www.google.com")
print(onecash.cash)
print(onecash.checkurl("www.google.com"))
print(onecash.checkurl("www.google.com/query"))
print(onecash.cash)
print(onecash.checkurl("www.google.com/query"))
print(onecash.checkurl("www.google.com/query"))
print(onecash.cash)
