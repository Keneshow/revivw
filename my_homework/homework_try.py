# 1
from sys import excepthook

try:
    x = float(input("Введите число : "))
    y = float(input("Введите число : "))
    result = x / y
    print(f"Вывод деления: {result:.2f}")             # для себя
except ZeroDivisionError:
    print("Ошибка -> деление на ноль!!!")
finally:
    print(f"этот блок выполняется всегда.")



# 2

try:
    user_num = int(input("Введите число: "))
    result = user_num ** 2
    print(f"Число в квадрате: {result} ")
except ValueError:
    print("Ошибка -> это не число")
finally:
    print(f"этот блок выполняется всегда.")


# 3

nums = [10, 7, 25, 1, 98, 53]

try:
    index = int(input("Введите индекс от 0 - 5: "))
    print(f"Элемент с индексом {index}: это число {nums[index]}")
except ValueError:
    print("Ошибка -> ужно ввести целое число.")
except IndexError:
    print("Ошибка -> индекс вне диапазона списка.")
finally:
    print(f"этот блок выполняется всегда.")


# 4

try:
    x = float(input("Введите число: "))
    y = float(input("Введите число: "))
    result = x / y
except ZeroDivisionError:
    print("Ошибка -> Вы не можете разделить на ноль!!!")
except ValueError:
    print("Ошибка -> нужно ввести целое число.")
else:
    print(f"Результат делния: {result:.3f}")               # для себя
finally:
    print(f"этот блок выполняется всегда.")


# 5

try:
    user_num = int(input("Введите число: "))
    print(user_num)
    if user_num < 0:
        raise ValueError("Ошибка -> введено отрицательное число ")     # NegativeNumberError: не смог с этим разобраться напишите ваше решение в коментарии чтобы знать
except ValueError as e:
    print(e)

# 6

def calculator(x, y, operand):
    if operand == "+":
        return x + y
    elif operand == "-":
        return x - y
    elif operand == "*":
        return x * y
    elif operand == "/":
        if y == 0:
            return "Ошибка: деление на ноль"
        return x / y
    else:
        return "Ошибка: неверный оператор"

try:
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    operand = input("Введите оператор (+, -, *, /): ")
    result = calculator(x, y, operand)
    print(f"Результат: {result}")
except ValueError:
    print("Ошибка: введите корректное число")
except ZeroDivisionError:
    print("Ошибка -> Вы не можете разделить на ноль!!!")
finally:
    print(f"этот блок выполняется всегда.")


# 7

def divide_pairs(numbers):
    results = []
    for i in range(0, len(numbers) - 1, 2):
        try:
            result = numbers[i] / numbers[i + 1]
            results.append(result)
        except ZeroDivisionError:
            results.append("Error: Division by zero")
        except TypeError:
            results.append("Error: Invalid type")
    return results


numbers = [10, 2, 8, 0, 6, 'a', 4]
results = divide_pairs(numbers)
print(results)


# 8

def str_len(word):
    try:
        if type(word) == str:
            return len(word)
        else:
            return -1
    except TypeError:
        return -1

print(str_len("Hello, world!"))
print(str_len(123))
print(str_len(None))


# 9

def risky_operation():
    return 10 / 0

try:
    risky_operation()
except Exception as e:
    print(f"Произошла ошибка: {type(e)}")


# 10

from math_utils import *

print(add_(4, 7))
print(sub(19,14))
print(mul(4, 5))
print(div(32, 8))


import my_packages.math_1

print(my_packages.math_1.add_(4, 5))
print(my_packages.math_1.sub(10, 5))
print(my_packages.math_1.mul(5,9))
print(my_packages.math_1.div(100,10))


from my_packages.math_1 import *

print(mul(4, 5))
print(sub(49, 7))
print(add_(10, 6))
print(div(100,25))


# 11

from greeting import hello

hello("Almanbet")
hello("Maria")
hello("John")

from greeting import bye

bye("Amanbet")
bye("Maria")
bye("John")


# 12

from my_packages.area import circle_area

print(circle_area(4))


from my_packages.area import square_area

print(square_area(7))


# 13

from my_packages.randomizer import get_random_number

print(f"Случайное число от 1 до 100: {get_random_number()}")


# 14

from my_packages.temperature import cels_to_fahr

print(cels_to_fahr(45))


from my_packages.temperature import fahr_to_cels

print(fahr_to_cels(58))


# 15

from caclulator import basic, advance

print(add_(9, 9))
print(sub(90, 9))

print(mul(24, 7))
print(div(99, 9))


# 16

from geometry.shapes import rectangle_perimeter, circle_perimeter
from geometry.areas import rectangle_area

def main():
    length = 5
    width = 3
    radius = 4

    print(f"Периметр прямоугольника: {rectangle_perimeter(length, width)}")
    print(f"Площадь прямоугольника: {rectangle_area(length, width)}")
    print(f"Периметр круга: {circle_perimeter(radius)}")
    print(f"Площадь круга: {circle_area(radius)}")


# 17

from utils.str_utils.operations import reverse_str

x = input("Введите фразу: ")
reverse = reverse_str(x)

print(f"Развернутое слово: {reverse}")


from utils.math_utils.operations import square

x = int(input("Введите число: "))
sqr_int = square(x)

print(f"Квадрат числа: {sqr_int}")


# 18

from animals.dogs import bark
from animals.cats import meow

print("Давайте послушаем, как лают собаки и мяукают кошки!")

bark()
meow()


# 19

from convert.lenght import metr_to_km, km_to_metr
from convert.weight import kg_to_gram, gram_to_kg

choice = input("Выберите конвертацию (1 - метры в километры, 2 - километры в метры, 3 - килограммы в граммы, 4 - граммы в килограммы): ")

if choice == '1':
    metr = float(input("Введите метры: "))
    print(f"{metr} метров = {metr_to_km(metr)} километров")
elif choice == '2':
    km = float(input("Введите километры: "))
    print(f"{km} километров = {km_to_metr(km)} метров")
elif choice == '3':
    kg = float(input("Введите килограммы: "))
    print(f"{kg} килограммов = {kg_to_gram(kg)} граммов")
elif choice == '4':
    gram = float(input("Введите граммы: "))
    print(f"{gram} граммов = {gram_to_kg(gram)} килограммов")
else:
    print("Неверный выбор.")