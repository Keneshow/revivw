num = int(input("число: "))
print(float(num))
print(bool(num))

import math

r = float(input("Введите радиус круга: "))
s = math.pi * (r ** 2)  # Используем math.pi и возводим r в квадрат
print(f"Площадь круга: {s:.2f}")  # Округляем до 2 знаков после запятой

a = input("name:")
b = a[::-1]
if a == b:
    print('true')
else:
    print('false')

login = input("adress: ")
if "@" in login and "." in login:
    print("true")
else:
    print("false")

number = int(input('num:'))
if number % 2 == 0:
    print("true")
else:
   print("false")

num = int(input("число: "))
if num > 0:
   print('положительное число')
elif num < 0:
   print('отрицательное число')
else:
   print("равно нулю")


price = int(input("цена:"))
discount = 0.1
result = price - (price * discount)
if price > 1000:
    print(result)
else:
    print(price)

year = int(input("date:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("true")
else:
    print("false")

age = int(input("возраст: "))
if age > 18:
    print("вход разрешен")
else:
    print("вход запрещен")

num = int(input("число: "))
if num % 2 == 0 and num % 5 == 0:
    print("true")
else:
   print("false")