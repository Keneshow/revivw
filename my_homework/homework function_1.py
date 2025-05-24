# 1 Площадь прямоугольника

def rectangle_area(length, width):
    return length * width
print(rectangle_area(5,6))

# 2 Время в секундах

def to_second(hours, minutes):
    return hours * 3600 + minutes * 60
print(to_second(3,28))

# 3 Возведение в квадрат

def square(x):
    return x ** 2
print(square(6))

# 4 Проверка на чётность

def is_even(number):
    return number % 2 == 0
print(is_even(5))

# 5 Первая и последняя буква

def first_and_last(text):
    return text[0] + text[-1]
print(first_and_last("hello"))

# 6 Сравнение двух чисел

def compare(a, b):
    if a > b:
        return "Больше"
    elif a < b:
        return "Меньше"
    else:
        return "Равны"
print(compare(5,8))

# 7 Обратная строка

def reverse_string(text):
    return text[::-1]
print(reverse_string(""))

# 8 Сколько символов в слове

def count_letters(word):
    return len(word)
print(count_letters("hello world"))