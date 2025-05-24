from abc import ABC, abstractmethod


# class Shape(ABC):               # po ymol4aniy default zna4eniys
#     @abstractmethod
#     def area(self):
#         pass
#
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
#
# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
#
#
#     @abstractmethod
#     def walk(self):
#         pass
#
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#
#     def eat(self):
#         print("Dog's eats")
#
#
#     def walk(self):
#         print("dog's walk")
#
#
#     def make_sound(self):
#         print("Dog's make sound")
#
#
#

# class BAnkAccount:
#     def __init__(self, card_nummber, balance, cvv):
#         self.card_number = card_nummber
#         self._balance = balance
#         self.__cvv = cvv
#
#     def get_cvv(self):
#         return self.__cvv
#
#     @property
#     def abc(self):
#         return self.__cvv
#
#     @aaa.setter
#     def aaa(self):
#         self.__cvv = cvv
#
# b = BAnkAccount("1234566", 12344, "345")
# print(b.card_number)
# print(b._balance)
# print(b.get_cvv())
#
# print(b.abc)
#
# b.aaa = 333
#
# print(b.abc)


#
# class Person:
#     def __init__(self, name, age ):
#         self.name = name
#         self.age = age
#
#
#     def __str__(self):          # 4 user
#         return f'{self.name}, {self.age}'
#
#
#     def __repr__(self):         # 4 1 b
#         return f'User = {self.name}, Age = {self.age}'
#
# p = Person("John", 34)
# print(type(p))            #возвращает строковое свойство а не строку
# print([p])                # recall coments for R'n'B
#
#

# class Book:
#     def __init__(self, pages):
#  #       self.title = title
# #        self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f'{self.pages}'
#
#     def __add__(self, other):       # +
#         return Book(self.pages + other.pages)
#
#     def __div__(self, other):   # *
#         pass
#
#     def __truediv__(self, other):   # /
#         pass
#
#     def __sub__(self, other):       # -
#         pass
#
#     def __pow__(self, power, modulo=None):  # **
#         pass
#
#     def __floordiv__(self, other):          # //
#         pass
#
#     def __mod__(self, other):       # %
#         pass
#
#     def __iadd__(self, other):
#         self.pages += other.pages
#         return self
#
#     def __isub__(self, other):
#         self.pages -= other.pages
#         return self
#
#     def __idiv__(self, other):
#         self.pages *= other.pages
#         return self
#
#     def __itruediv__(self, other):
#         self.pages /= other.pages
#         return self
#
#     def __ipow__(self, other):
#         self.pages **= other.pages
#         return self
#
#
#     def __len__(self):
#         return self.pages
#
#
#     def __eq__(self, other):
#         return self.pages == other.pages
#
#
#     def __le__(self, other):
#         return self.pages == other.pages
#
#     def __gt__(self, other):
#         return self.pages == other.pages
#
#     def __ge__(self, other):
#         return self.pages == other.pages
#
#     def __ne__(self, other):
#         return self.pages == other.pages
#
#
#
#
# b1 = Book(12)
# b2 = Book(21)
#
# c = b1 + b2
#
# b1 += b2
# print(b1.pages)

#print(b1 == b2)

#print(len(b1))
#
# print(b1 + b2)          # временый вывод юез сохранения в памяти
# print(c)
# print(b2)


class Auto:
    def __init__(self, model, year):
        self.model = model
        self.year = year


    def __str__(self):
        return f'{self.model}, {self.year}'


    def __repr__(self):
        return f'Auto for bying {self.model} his year will be {self.year}'


a = Auto('BMWW', 2020)

print(a)
print([a])

