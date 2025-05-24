


class My_math:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    @staticmethod
    def add(a, b):
        return a + b


a = My_math(1, 3)

print(My_math.add(1, 3))        # staticmethod print



class Weather:
    def __init__(self, gradus, wind):
        self.gradus = gradus
        self.wind = wind


    @staticmethod
    def f_to_cels(faren):
        return (faren - 32) / 1.8

print(Weather.f_to_cels(500))

from abc import *


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def area(width, height):
        return width + height

print(Rectangle.area(10, 5))

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'])

    def __str__(self):
        return f'User{self.name}, {self.age}'

u1 = User('John', 32)

user_data = {'name': 'Axat', 'age': 29}


print(u1)


class Math:
    def __init__(self):
        pass

    @staticmethod
    def even(num):
        if num % 2 == 0:
            return 'True'
        else:
            return 'false'

print(Math.even(5))



class User:
    def __init__(self, name):
        self.name = name


    def __str__(self):
        return f'User {self.name}'

    @classmethod
    def from_obj(cls, name):
        return cls(name)


a = User("Ivan")

print(a)

#######3        SOLID           #############
Single Responsibility Principle
Open Closed principle
Liscow
Interface Segration Principle
D


class Report:
    def __init__(self, data):
        self.data = data

class FileSaver:
    @staticmethod
    def save(data):
        with open('report.txt', 'a') as file:
            file.write(data)

################

class Payment:
    def pay(self):
        print()

class CreditCard(Payment):
    def pay(self):
        print()

class PayPall:
    def pay(self):
        print()

########################

class Bird:
    def fly(self):
        print('bird fly')

class Pinguin(Bird):
    def fly(self):
        print('pinguin fly')

#########

class Bird:
    def move(self):
        print('bird fly')


class Pinguin(Bird):
    def move(self):
        print('pinguin fly')

##############

class Plane:
    def fly(self):
        print('fly')

class Tank:
    def fly(self):
        print('fly')

    def shoot(self):
        print('shooting target')