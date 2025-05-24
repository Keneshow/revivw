#1
a = 1
while a <= 10:
     print(a)
     a += 1

#2
i = 10
while i >= 1:
    print(i)
    i -= 1
print("Пуск!")

#3
x = 1
while x < 1000:
      x *= 2
      print(x)

#4
#
from random import randint

secret_num = randint(1,100)
my_num = 0
print("Угадай мое число")

while my_num != secret_num:
    my_num = int(input("введи число: "))
    if my_num < secret_num:
        print("больше")
    elif my_num > secret_num:
        print("меньше")
    else:
        print("поздравляю ты угадал!!!")

# #5

orel_count = 0
reshka_count = 0

while True:
     word = input("Введите 'орел', 'решка' или 'стоп' для завершения: ")

     if word == "стоп":
          break
     elif word == "орел":
          orel_count += 1
     elif word == "решка":
          reshka_count += 1
     else:
          print("Пожалуйста, введите 'орел', 'решка' или 'стоп'.")

print(f"Количество 'орел': {orel_count}")
print(f"Количество 'решка': {reshka_count}")

#######
words = []

while True:
    word = input("Введите 'орел', 'решка' или 'стоп' для завершения: ")

    if word == "стоп":
        break
    elif word in ["орел", "решка"]:
        words.append(word)
    else:
        print("Пожалуйста, введите 'орел', 'решка' или 'стоп'.")

orel_count = sum(1 for w in words if w == "орел")
reshka_count = sum(1 for w in words if w == "решка")

print(f"Количество 'орел': {orel_count}")
print(f"Количество 'решка': {reshka_count}")

#6
palindrom = 0                   #для себя
no_palindrom = 0                #для себя

while True:
    num = input("Введите число (или '0' для завершения): ")

    if num == '0':
        break
    if num == num[::-1]:
        print("палиндром")
        palindrom += 1
    else:
        print("не палиндром")
        no_palindrom += 1
print(f"палиндром: {palindrom}")
print(f"не палиндром: {no_palindrom}")