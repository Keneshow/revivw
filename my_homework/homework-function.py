# 1 Площадь прямоугольника

def rectangle_area(length, width):
    return length * width


while True:
    a = int(input("ввведите длину: "))
    b = int(input("ввведите ширину: "))
    result = rectangle_area(a, b)
    print("Площадь прямоугольника: ", result)
    c = input("contineu: yes/no? ")
    if c == "no":
        break

# 2 Время в секундах

def to_second(hours, minutes):
    return hours * 3600 + minutes * 60


while True:
    a = int(input("ввведите число в часах: "))
    b = int(input("ввведите число в минутах: "))
    result = to_second(a,b)
    print("В секундах это: ", result)
    c = input("contineu: yes/no? ")
    if c == "no":
        break

# 3 Возведение в квадрат

def square(x):
    return x ** 2


while True:
    a = int(input("Введите число или 0 для завершения: "))
    if a == 0:
        break
    result = square(a)
    print("Квадрат числа:", result)


# 4 Проверка на чётность

def is_even(number):
    return number % 2 == 0


while True:
    a = int(input("Введите число для проверки или 0 для завершения: "))
    if a == 0:
        break
    print(f"{a} является четным: {is_even(a)}")

# 5 Первая и последняя буква

def first_and_last(text):
    return text[0] + text[-1]

while True:
    word = input("Введите сллово или 'стоп' для завершения: ")
    if word.lower() == "стоп":
        break
    print(first_and_last(word))

# 7 Обратная строка

def reverse_string(text):
    return text[::-1]


while True:
    word = input("Введите сллово или 'стоп' для завершения: ")
    if word.lower() == "стоп":
        break
    print(reverse_string(word))

# 8 Сколько символов в слове

def count_letters(word):
    return len(word)


while True:
    word = input("Введите сллово или 'стоп' для завершения: ")
    if word.lower() == "стоп":
        break
    print(count_letters(word))

# 6

def compare(a, b):
    if a > b:
        return "Больше"
    elif a < b:
        return "Меньше"
    else:
        return "Равны"

# Примеры использования
print(compare(10, 5))  # ➝ "Больше"
print(compare(3, 9))   # ➝ "Меньше"
print(compare(7, 7))   # ➝ "Равны"
