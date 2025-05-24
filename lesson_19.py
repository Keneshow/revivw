#
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#
# obj = Human('Almanbet', 31)
#
# print(obj.name)
# print(obj.age)
from random import randint


#
# class Marker:
#     size = 'round'
#
#     def __init__(self, color, brand='green'):
#         self.color = color
#         self.brand = brand
#
#
# green_marker = Marker('green', 'Green')
#
# red_marker = Marker('red', 'Red')
#
# print(green_marker.size)
# print(red_marker.size)
#
# print(green_marker.color)
# print(green_marker.brand)
#
#
# from random import randint
#
# class Auto:
#     def __init__(self, model, years, brand):
#         self.model = model
#         self.years = years
#         self.brand = brand
#         self.size = randint(1, 10)
#
#
#
#
# Bmw_auto = Auto('cupe', 2020,'BMW')
#
# benz_auto = Auto('4wd', 2019, 'Mercedes')
#
# benz_auto.model = 'AMG'   # izmenit (model, color, )
#
# print(f'Bmw_model: {Bmw_auto.model}, BMW_years: {Bmw_auto.years}')
# print(f'BMW_years: {Bmw_auto.years}')
#
# print(benz_auto.model)
#
# print(Bmw_auto.size)
# print(benz_auto.size)

#
# class Car:
#     def __init__(self, name):
#         self.name = name
#         self.engine = False
#
#
#     def check_engine(self):
#         if self.engine:
#             print('Engine is runing')
#         else:
#             print('Engine is not runing')
#
#
#
#     def start(self):
#         self.engine = True
#
#
#     def stop(self):
#         self.engine = False
#

# toyota = Car('Toyota')
# toyota.check_engine()
# toyota.start()
# toyota.check_engine()
# toyota.stop()
# toyota.check_engine()



class BankAccount:
    def  __init__(self, owner, num_card, balance=0):
        self.num_card = num_card
        self.balance = balance
        self.owner = owner
        self.transfers = []

    def check_balance(self):
        print(f"{self.owner}'s balance = {self.balance}")


    def cash_in(self, amount):
        self.balance += amount
        self.transfers.append(f"Cash in {amount}")
        print(self.balance)


    def cash_out(self, amount):
        self.balance -= amount
        self.transfers.append(f"Cash out {amount}")
        print(self.balance)


    def transactions_history(self):
        print(f"{self.num_card}'s transaction_history = {self.transfers}")

my_acc = BankAccount("Ivan", '1234345455555')
my_acc.check_balance()
my_acc.cash_in(100)
my_acc.check_balance()
my_acc.cash_out(49)
my_acc.check_balance()