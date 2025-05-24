
# 🧠 1. Уникальные книги в библиотеке

books = set()

while True:
    name_book = input("введите название книги (или стоп для завершения): ")
    if name_book.lower() == "стоп":
        break
    if name_book.lower() in books:
        print("такая книга уже есть...")
    else:
        books.add(name_book.lower())
sort_books = sorted(books)
print("Список книг в алфавитном порядке:")
for i in sort_books:
    print(i)

8 🛒 Корзина с ограничением

basket = []

while True:
    if len(basket) == 5:
        print("Корзина полна!!!")
        break
    item = input("Что хотите добавить в корзину? ")
    basket.append(item)
    print("В корзине сейчас:", basket)


# 9 🕓 Посещение спортзала

guest = {}
price = 100
discount = 0

while True:
    time_in = int(input("Введите время начало (в часах): "))
    time_exit = int(input("Введите время завершения (в часах): "))

    hours = time_exit - time_in
    if hours > 3:
        discount = hours * price * 0.15
    else:
        discount = 0

    total = hours * price - discount

    print(f"Общая сумма: {total} сом")
    if discount > 0:
        print(f'Скидка: {discount} сом')

    exit_program = input("Хотите продолжить? (да/нет): ")
    if exit_program.lower() != 'да':
        break

# 📱 10. Проверка номера телефона

phone_num = input("Введите номер для проверки и (стоп чтобы завершить) : ")
numbers = False

if len(phone_num) == 13 and phone_num.startswith("+996") and phone_num[4:].isdigit():
    numbers = True
    print("Все верно... ")
else:
    print("Не верный формат ввода!!!")

# 🎲 6. Генератор промокодов

import random
import string

codes = []
guest = int(input("введите количество: "))
for i in range(guest):
    mix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    codes.append(mix)
print("Список промокодов:", codes)

💼 7. Отчёт о сотрудниках

employees = []  # Список для хранения сотрудников

while True:
    entry = input("Введите имя и зарплату (например, Айбек 120000) или 'стоп' для выхода: ")

    if entry.lower() == 'стоп':
        break  # Выходим из цикла, если ввели 'стоп'

    name, salary = entry.split()  # Разделяем ввод на имя и зарплату
    salary = int(salary)  # Преобразуем зарплату в число

    if salary > 100000:
        role = "Руководитель"
    else:
        role = "Сотрудник"

    employees.append({"Имя": name, "Зарплата": salary, "Роль": role})  # Добавляем сотрудника в список

# Выводим таблицу
print("\nТаблица сотрудников:")
for emp in employees:
    print(f"Имя: {emp['Имя']}, Зарплата: {emp['Зарплата']}, Роль: {emp['Роль']}")

📦 5. Склад товаров

sqlad = dict()
while True:
    name_tovar = input("navanie i kolvo tovara: ")
    if name_tovar.lower() == "стоп":
        break
    name, kolvo = name_tovar.split()
    kolvo = int(kolvo)
    if name in sqlad:
        sqlad[name] += kolvo
    else:
        sqlad[name] = kolvo
print("\nИтоговый остаток по товарам:")
for name, kolvo in sqlad.items():
    print(f"{name}: {kolvo}")



💸 2. Банкомат

balance = 10000
withdraw_count = 0

while True:
    amount = float(input("Введите сумму для снятия (или 0 для выхода): "))

    if amount == 0:
        break

    if amount > balance:
        print("Ошибка: недостаточно средств.")
    else:
        balance -= amount
        withdraw_count += 1
        print(f"Снято: {amount}. Остаток: {balance}")

print(f"Осталось на счёте: {balance}. Количество снятий: {withdraw_count}.")

# 3

purchases = {}
total_sum = 0

while True:
    line = input("Введите название и цену (или 'готово' для завершения): ")

    if line == "готово":
        break

    name, price = line.split()
    price = int(price)

    purchases[name] = price
    total_sum += price

print("Ваши покупки:")
for name, price in purchases.items():
    print(f"{name}: {price}")

print(f"Общая сумма: {total_sum}")

# 4


movies = {
    "astral": 18,
    "cartoon": 4,
    "avatar": 12,
    "saw": 18,
    "ralf": 0,
    "titanic": 12
}

age = int(input("Введите Ваш возраст: "))

print("Доступные фильмы:")
for name, limit in movies.items():
    if age >= limit:
        print(name)
