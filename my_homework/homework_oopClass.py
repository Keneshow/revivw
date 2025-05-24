# 1. 📦 Создание объекта из строки (@classmethod)

class Product:
    def __init__(self, name, count):
        self.name = name
        self.count = float(count)

    @classmethod
    def from_string(cls, d):
        name, count = d.split(';')
        return cls(name, count)

    def __str__(self):
        return f'Товар: {self.name}, цена: {self.count}'

prod = Product.from_string("snikers;55.59")
print(prod)


# 2 ⏱ Проверка времени (@staticmethod)

from datetime import datetime as dt

class Store:
    @staticmethod
    def is_store_open():
        time = dt.now().hour
        return 9 <= time < 18

print("Store open" if Store.is_store_open() else "Store close")


# 3 📘 Отслеживание количества экземпляров (@classmethod)


class Book:
    total = 0
    def __init__(self, name):
        self.name = name
        Book.total += 1

    @classmethod
    def total_books(cls):
        return cls.total

b1 = Book("Harry Potter")
b2 = Book("Sherlock Holmes")

print(Book.total_books())


# 4 💡 Валидация email (@staticmethod)

class Invalid:

    @staticmethod
    def is_valid_email(email):
        return  "@" in email and "." in email

login = Invalid.is_valid_email('qwerty@gmail.com')
print(login)


# 5. 🏗 Создание объекта через @classmethod

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def from_square(cls, side):
        return cls(side, side)

    def area(self):
        return self.width * self.height

square = Rectangle.from_square(7)

print(square.width)
print(square.height)
print(square.area())


# 6 🌡 Перевод температур (@staticmethod)

class Temperature:
    @staticmethod
    def cels_to_fahr(c):
        return c * 1.8 +32

    @staticmethod
    def fahr_to_cels(f):
        return (f - 32) / 1.8

print(Temperature.cels_to_fahr(32))
print(Temperature.fahr_to_cels(222))


# 7 Создание объекта из словаря (@classmethod)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d['name'],d['age'])

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'

data = {"name": "Viola", "age": 25}
user = User.from_dict(data)

print(user)


# 8 🎂 Проверка совершеннолетия (@staticmethod)

class Person:
    @staticmethod
    def is_adult(age):
        return age >= 18

a = Person.is_adult(17)
b = Person.is_adult(23)

print(a)
print(b)


# 9 🔐 Генерация пароля (@staticmethod)

import random
import string

class PasswordGenerator:
    @staticmethod
    def generate(length=8):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

print(PasswordGenerator.generate())
print(PasswordGenerator.generate(15))


# 10 Создание нескольких объектов (@classmethod)

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def bulk_create(cls, list_to_dict):
        return [cls(d["name"], d["price"]) for d in list_to_dict]

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}'

data = [
    {"name": "Book", "price": 12.99},
    {"name": "Pen", "price": 1.50},
    {"name": "Notebook", "price": 5.75}
]

items = Item.bulk_create(data)

for item in items:
    print(item)


# 11 🛍 Скидка на продукт (@staticmethod

class Price:
    @staticmethod
    def apply_discount(price, percent):
        return price - (price * percent / 100)

print(Price.apply_discount(1000, 32))


# 12 Создание объекта из JSON (@classmethod)


import json

class MathTask:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return  f"Вопрос: {self.question}\n{self.answer}"

    @classmethod
    def from_json(cls, json_string):
        try:
            data = json.loads(json_string)
            question = data.get("question")
            answer = data.get('answer')
            if question is None or answer is None:
                raise ValueError("JSON должен содержать 'question' и 'answer'")
            return cls(question, answer)

        except json.JSONDecodeError:
            raise ValueError("Неверный формат JSON-строки")

json_data = '{"question": "2 + 2", "answer": 4}'

task = MathTask.from_json(json_data)
print(task)

# 13 📅 Создание из даты (@classmethod)

from datetime import datetime

class Event:
    def __init__(self, date: datetime):
        self.date = date

    def __str__(self):
        return f"Событие запланировано на {self.date.strftime('%d.%m.%Y')}"

    @classmethod
    def from_date_string(cls, date_string: str):

        try:
            date = datetime.strptime(date_string, "%Y-%m-%d")
            return cls(date)
        except ValueError:
            raise ValueError("Дата должна быть в формате 'YYYY-MM-DD'")

event = Event.from_date_string("2025-05-15")
print(event)


# 14  🕹 Проверка правильного формата (@staticmethod)

class Number:
    @staticmethod
    def is_valid_coordinates(x, y):
        return isinstance(x, int) , isinstance(y, int)

num = Number.is_valid_coordinates(4, 5)
print(num)


# 15  🔁 Смена текущего режима (@classmethod)

class AppMode:
    mode = "light"

    @classmethod
    def set_mode(cls, mode):
        cls.mode = mode

    @classmethod
    def get_mode(cls):
        return cls.mode

print(f'Standart mode: {AppMode.get_mode()}')
AppMode.set_mode("dark")
print(f'Change mode: {AppMode.get_mode()}')


# 16  📂 Генерация пути к файлу (@staticmethod)

class File:
    @staticmethod
    def get_path(file_name, folder='tmp'):
        return f'{folder}/{file_name}'

print(File.get_path("logic.txt"))
print(File.get_path("poem_new.txt"))


# 17 🔎 Поиск пользователя по email (@classmethod)

class User:
    users = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.users.append(self)

    @classmethod
    def find_by_email(cls, email):
        for user in cls.users:
            if user.email == email:
                return user
        return None


u1 = User('Vannesa', 'Vannes@gmail.com')
u2 = User("Bred", "Bred@mail.ru")
u3 = User("Bob", "spon@gmail.com")

found = User.find_by_email("spon@gmail.com")
if found:
    print(f'His name is: {found.name}\n' f'email: {found.email}')
else:
    print("User not found")


# 18 ⚙️ Создание экземпляра из конфигурации (@classmethod)

class ConfigurableBot:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    @classmethod
    def from_cfg_file(cls, path):
        with open(path, 'r') as f:
            name = f.readline().split('=')[1].strip()
            version = f.readline().split('=')[1].strip()
            return cls(name, version)

bot = ConfigurableBot.from_cfg_file('Bot_cfg.txt')
print(f'Name:{bot.name}\n' f'Version :{bot.version} ')


# 19 🔄 Конвертация единиц (@staticmethod)

class Convert:
    @staticmethod
    def km_to_miles(km):
        return km * 0.621371

    @staticmethod
    def miles_to_km(miles):
        return miles / 0.621371

print(f'{Convert.km_to_miles(15):.4f} miles')
print(f'{Convert.miles_to_km(7.79):.4f} km')


# 20  💬 Логгер (@staticmethod)

class Logger:
    @staticmethod
    def log(message, level='INFO'):
        print(f'[{level}] {message}')

Logger.log("Система запущена")
Logger.log("Низкий заряд батареи", "WARNING")
Logger.log("Критическая ошибка", "ERROR")