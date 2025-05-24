

# 1 Создай класс Animal и от него наследуй Dog

class Animal:


    def speak(self):
        return "Some sound"


class Dog(Animal):


    def speak(self):
        return "woof, woof"

a = Animal()
d = Dog()

print(f'Animal: {a.speak()}')
print(f'Dog: {d.speak()}')


# 2 Расширь Dog, добавив поле breed

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog('Buble', 'Corgy')
print(f"Dog's name: {dog.name}")
print(f"Dog's breed: {dog.breed}")


# 3 Класс Person, от него — Employee

class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

info = Employee('Ivan', '1234566')
print(f"Имя ==> {info.name}")
print(f"Инфо-номер ==> {info.employee_id}")


# 4  Класс Vehicle с методом start_engine()

class Vehicle:
    def start_engine(self):
        print("Vehicle ==> start engine ")


class Car(Vehicle):
    def start_engine(self):
        print("Car ==> start engine ")


class Bike(Vehicle):
    def start_engine(self):
        print("Bike ==> start engine " )


class Truck(Vehicle):
    def start_engine(self):
        print("Truck ==> start engine ")

start = [Vehicle(), Car(), Bike(), Truck()]
for i in start:
    i.start_engine()


# 5 Иерархия User → Admin, Moderator, Guest

class User:
    def access_lvl(self):
        print("Access level ==> User")


class Admin(User):
    def access_lvl(self):
        print("Access level ==> Admin")


class Moderator(User):
    def access_lvl(self):
        print("Access level ==> Moderator")


class Guest(User):
    def access_lvl(self):
        print("Access level ==> Guest")

lvl = [User(), Admin(), Moderator(), Guest()]
for i in lvl:
    i.access_lvl()


# 6 Сделай Logger с методом log(message)

class Logger:
    def log(self, message):
        raise NotImplementedError("Метод log() должен быть переопределён.")


class FileLogger(Logger):
    def log(self, message):
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(message + "\n")
        print("Сообщение записано в файл.")


class ConsoleLogger(Logger):
    def log(self, message):
        print("Сообщение в консоль:", message)

f = FileLogger()
f.log("Это сообщение будет записано в файл.")

c = ConsoleLogger()
c.log("Это сообщение выведено в консоль.")


# 7 Класс Product → Book, Electronics

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author


class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

book = Book("Изучаем Python", 968, "Эрик Метиз")
print(f"Книга: {book.name}, цена: {book.price}, Автор: {book.author}  ")
gadget = Electronics("Смартфон", 15520, "2 ода")
print(f"Электроника: {gadget.name}, Цена: {gadget.price}, Гарантия: {gadget.warranty}")


# 8 Создай BankAccount, наследуй SavingsAccount, CreditAccount

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


    def cash_in(self, amount):
        self.balance += amount
        print(f"{self.owner} Cash in  {amount}. New balance {self.balance} ")


    def cash_out(self, amount):
        if amount <= self.balance:
            print(f"Cash out :{self.owner}, you can't withdraw {amount} more then your balance")


    def get_balance(self):
        return self.balance


class SavingAccount(BankAccount):
    def cash_out(self, amount):
        if self.balance - amount < 0:
            print(f"Cash out: {self.owner}, you can't withdraw {amount} more then your balance")
        else:
            super().cash_out(amount)


class CreditAccount(BankAccount):
    def __init__(self, owner, balance=0, credit_limit=0):
        super().__init__(owner, balance)
        self.credit_limit = credit_limit


    def cash_out(self, amount):
        if amount <= self.balance + self.credit_limit:
            self.balance -= amount
            print(f"{self.owner} cash out {amount}. New balance {self.balance} ")
        else:
            print(f"{self.owner} can't withdraw {amount}. Exceeds credit limit")


savings = SavingAccount("Alice", 800)
savings.cash_in(200)
savings.cash_out(1200)

credit = CreditAccount("Bob", 500)
credit.cash_in(300)
credit.cash_out(900)


# 9 Создай систему животных с методом make_sound

class Animal:
    def make_sound(self):
        print("any sound")


class Dog(Animal):
    def make_sound(self):
        print("Dog's : woof woof")


class Cat(Animal):
    def make_sound(self):
        print("Cat's : meow meow")


class Frog(Animal):
    def make_sound(self):
        print("Frog's : cwag cwag")


class Raven(Animal):
    def make_sound(self):
        print("Raven's : car car")

animals = [Dog(), Cat(), Frog(), Raven()]               # крутая штука
for a in animals:
    a.make_sound()