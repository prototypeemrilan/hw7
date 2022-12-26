import colorama
import math,datetime

# MRO

class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'меня зовут {self.name} и мне {self.age} лет'

hum=Human('Бекболот',21)
hum.age=45
print(hum)

class Human2(Human):
    def __init__(self,name,age,nasa=False):
        super().__init__(name,age)
        self.nasa=nasa
    def _n(self):
        self.nasa=True
    def t(self):
        self.age *= 2
    def __orientation(self):
        print(f'{self.name} является Алдияром')
    def year(self):
        print(f'{2023-self.age}')

    def car(self):
        print(f'{self.name} водит машину с 18 лет, его стаж вождения {self.age - 18}')

