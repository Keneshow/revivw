#from random import randint
#num = 0
#num_2 = 1
#while num != num_2:
#    num_2 = randint(1,5)
#    num = int(input("numbers: "))
 #   print(num_2)
  #  if num == 2 or num_2 ==2:
  #      break
#print("end process!!!")

#count = 1
#while count < 11:
#   print(count)
#   count += 2

#a = int(input("num: "))
#while a > 1:
 #   a /= 2
 #   print(a)

#
# s = 'jello world'
# while len(s) > 8:
#     word = input("slovo: ")
#     print(word[::-1])

#while True:
#    a = input("slovo: ")
#    if len(a) < 8:
#        break
#    else:
#        print("pretty good")

#a = "slovo"
#b = "stop"
#while True:
#    word = input("slovo: ")
 #   if word == "stop":
  #      break
   # else:
    #    print(word[0:3])

total = 0  # Переменная для хранения суммы

while True:  # Бесконечный цикл
    number = int(input("Введите число (введите 0 для завершения): "))  # Запрос числа у пользователя
    if number == 0:  # Проверка на окончание ввода
        break  # Выход из цикла, если введено 0
    total += number  # Добавляем введенное число к общей сумме

print("Сумма чисел:", total)  # Вывод суммы



a = 'future'

result = ''
for i, s in enumerate(a):
    if i % 2 == 0:           # Если индекс чётный
        result += s.upper()  # Добавить символ в верхнем регистре
    else:
        result += s

print(result)

sum_multiples = 0

for number in range(1, 21):
    if number % 3 == 0 or number % 5 == 0:
        sum_multiples += number

print("Сумма чисел от 1 до 20, кратных 3 или 5:", sum_multiples)
