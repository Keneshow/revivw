# 1 Возведение чисел в квадрат

nums = [ 1, 2, 3, 4]
print(list(map(lambda x: x ** 2, nums)))

# 2 Преобразование строк в числа

str_nums = ["10", "20", "30"]
print(list(map(int, str_nums)))

# 3 Перевести все строки в верхний регистр

words = ["hello", "world"]
print(list(map(lambda x: x.upper(), words)))

# 4 Удвоение каждого элемента

nums = [1, 5, 7]
print(list(map(lambda x: x * 2, nums)))

# 5 Вычисли длины строк

names = ["Max", "Alex", "John"]
print(list(map(lambda x: len(x), names)))

# 6 Удалить отрицательные числа

nums = [1, -5, 3, -2, 8]
print(list(filter(lambda x: x > 0, nums)))

# 7 Оставить только чётные

nums = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x % 2 == 0, nums)))

# 8 Отфильтровать строки длиннее 4 символов

words = ["hi", "hello", "world", "yes"]
print(list(filter(lambda x: len(x) > 4, words)))

# 9 Преобразовать список к булевым значениям

nums = [-1, 0, 5, 8]
print(list(map(bool, nums)))

# 10 Сложить 5 к каждому числу

nums = [1, 2, 3]
print(list(map(lambda x: x + 5, nums)))

# 11 Преврати числа в строки с префиксом "№"

nums = [1, 2, 3]
print(list(map(lambda x: "№" + str(x), nums )))

# 12 Оставить строки, начинающиеся с большой буквы

names = ["John", "peter", "Mary", "jane"]
print(list(filter(lambda x: x[0].isupper(), names)))

# 13 Преобразовать список цен в формат "Цена: XX.XX"

prices = [10.5, 20, 5.99]
print(list(map(lambda x: f'Цена: {x:.2f}', prices)))

# 14 Перевести градусы из Цельсия в Фаренгейт

celsius = [0, 100, 20]
print(list(map(lambda x: (x * 1.8) + 32, celsius)))
print(list(map(lambda x: (9 / 5 * x) + 32, celsius)))

# 15 Оставить только строки, в которых больше 1 слова

phrases = ["hello world", "hi", "good morning", "yo"]
print(list(filter(lambda x: len(x.split()) > 1, phrases)))

# 16 Отфильтровать только числа

mixed = ["one", 2, "three", 4]
print(list(filter(lambda x: type(x) == int, mixed)))

# 17  Добавить ! к каждой строке

words = ["hi", "hello"]
print(list(map(lambda x: str(x) + "!", words )))

# 18 Оставить только строки, содержащие букву a

words = ["apple", "orange", "kiwi", "grape"]
print(list(filter(lambda x: "a" in x, words)))

# 19 Отфильтровать людей старше 18 лет

people = [{"name": "John", "age": 20}, {"name": "Anna", "age": 15}]
print(list(filter(lambda x: x['age'] > 18, people)))