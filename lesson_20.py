
#
# class Animal:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#
#     def speak(self):
#         print(f'{self.name} says: {self.color}')
#
#
# class Dog(Animal):
#     def __init__(self,age, name, color):
#         super().__init__(name, color)
#         self.age = age
#
#
#     def speak(self):
#         print(f'{self.name} says: {self.age} years old')
#
#
#
# animal = Animal('Animal', 'green')
# print(animal.name)
#
#
# dog = Dog(23, 'dog', 'red')
# print(dog.age, dog.name, dog.color)
#
# animal.speak()
# dog.name
#
# class Shape:
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#
#     def area(self):
#         return 3.14 * (self.radius ** 2)
#
#
#
# circle = Circle(2)
# print(isinstance(circle, Circle))
#
#
# ##################
#
#
# class Transport:
#     def __init__(self, age, color):
#         self.age = age
#         self.color = color
#
#
# class Auto(Transport):
#     def __init__(self, model, age, color):
#         super().__init__(age, color)
#         self.model = model
#
#
#     def move(self):
#         pass
#
#
# class Moto(Transport):
#     def __init__(self, model, age, color):
#         super().__init__(age, color)
#         self.model = model
#
#
# ############
#
# class Computer:
#     class CPU:
#         def info(self):
#             return "intel core i7"
#
# cpu = Computer.CPU()
# print(cpu.info())
#
#
# #############
#
#
# class Flyer:
#     def fly(self):
#         return 'flying'
#
#
# class Walker:
#     def walk(self):
#         return 'walking'
#
#
# class Bird(Flyer, Walker):
#     pass
#
# bird = Bird()
# print(bird.fly())
# print(bird.walk())

#################################3333

#
# class Hero:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     def take_damage(self, damage):
#         self.health = damage
#
# class Mana(Hero):
#     def __init__(self, name, health, mana):
#         super().__init__(name, health)
#         self.mana = mana
#
#
#     def cast_spell(self, target):
#         damage = 30
#         if self.mana <= 0:
#             raise Exception("You can't cast spell")
#         else:
#             self.mana -= 20
#         return self.mana
#
#
#
# hero = Mana("Necr", 100, 100)
# ogr = Hero('Ogr', 100)
#
# hero.cast_spell(ogr)
# print(ogr.health)
# hero
# print(hero.cast_spell())
# print(hero.cast_spell())
# print(hero.cast_spell())
# print(hero.cast_spell())
# print(hero.cast_spell())
#


class User:
    def __init__(self, username):
        self.username = username


    def role(self):
        return 'admin'


class Company(User):
    def __init__(self, username, company_name):
        super().__init__(username)
        self.company_name = company_name

p = User('Almanbet')
c = Company("Almanbet", "Almanbet Company")
a = Admin(p.username, 'admin permission')

print(a.role())
print(p.role())
print(c.role())