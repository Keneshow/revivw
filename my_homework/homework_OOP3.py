

# 1 Простой приватный атрибут

class User:
    def __init__(self, password):
        self._password = password


    def check_password(self, password):
        if self._password == password:
            return "password accept"
        else:
            return "wrong password"

user = User("qwerty123")

print(user.check_password("qwerty123"))
print(user.check_password("ksdfksfkjsfa"))


# 2 Геттер и сеттер для balance

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance


    def get_balance(self):
        return self.__balance


    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance can't be negative")

acc = BankAccount(1000)
print(acc.get_balance())

acc.set_balance(1200)
print(acc.get_balance())

acc.set_balance(-500)
print(acc.get_balance())


# 3

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Баланс не может быть отрицательным.")

acc = BankAccount(1000)                 # @property
print(acc.balance)

acc.balance = 1200                      # @setter
print(acc.balance)

acc.balance = -700                      # @setter
print(acc.balance)


# 4

class Person:
    def __init__(self, age):
        self.__age = age


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age > self.__age:
            self.__age = new_age
        else:
            print("возраст нельзя уменьшать")

p = Person(25)              # @property
print(p.age)

p.age = 30                  # @setter
print(p.age)

p.age = 20                  # @setter
print(p.age)


# 5

class Employee:
    def __init__(self, salary):
        self.__salary = salary


    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 30000:
            self.__salary = new_salary
        else:
            print("Зарплата не может быть меньше 30000")

emp = Employee(37000)               #@property
print(emp.salary)

emp.salary = 44000                  #@setter
print(emp.salary)

emp.salary = 28000                  #@setter
print(emp.salary)


# 6

class Freelancer:
    def __init__(self, income):
        self.__income = income

    @property
    def income(self):
        return self.__income

    @property
    def tax(self):
        return self.__income * 0.13

worker = Freelancer(75219)
print(f"Доход: = {worker.income}")
print(f"Налог: (13%) = {worker.tax:.2f}")


# 7 Защита email от перезаписи

class User:
    def __init__(self, email):
        self.__email = email

    @property
    def email(self):
        return self.__email

u = User("unknownuser@gmail.com")
print(f'Mail: ==> {u.email}')


# 8

class Article:
    def __init__(self, title):
        self.__title = ''         # без этого не срабатывает Else решил ток с помощью GPT , не могли бы оставить коммент )))
        self.title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        if len(new_title) <= 20:
            self.__title = new_title
        else:
            print("Заголовок не может быть длиннее 20 символов.")
            self.__title = new_title[:20]           # для себя

art = Article("Somebody's write this aaaaaaaaaaaaaaaaaaaaaaaaa title")
print(art.title)
art = Article("qwerty")
print(art.title)


# 9

class Order:
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

num = Order("12423412")
print(num.id)


# 10

class Person:
    def __init__(self, birth_year):
        self.__birth_year = birth_year


    @property
    def birth_year(self):
        return 2025 - self.__birth_year

age = Person(1993)
print(f"Your age ==> {age.birth_year}")
