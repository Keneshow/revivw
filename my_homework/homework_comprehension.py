# 1 Квадраты чисел (list comprehension)

nums = [i ** 2 for i in range(1, 11)]
print(nums)

# 2 Только чётные (list comprehension + фильтрация)

filtred = [i for i in range(0, 21) if i % 2 == 0]
print(filtred)

# 3 Уникальные буквы (set comprehension)

uniq_chars = {i for i in "Hello world" if i != " "}
print(uniq_chars)

# 4 Только положительные (list comprehension)

numbers = [-5, 3, -1, 0, 2, -7]
positive_nums = [i for i in numbers if i > 0]
print(positive_nums)

# 5 Слово — длина (dict comprehension)

fruits = ['apple', 'banana', 'kiwi']
len_fruits = {i: len(i) for i in fruits}
print(len_fruits)

# 6 Уникальные длины (set comprehension)

words = ['hi', 'hello', 'ok', 'yes', 'no']
unique_lengths = {len(i) for i in words}
print(unique_lengths)

# 7 Округление чисел (list comprehension)

float_nums = [3.2, 4.8, 5.5, 6.9]
int_nums = [round(i) for i in float_nums]
print(int_nums)

# 8 Ключ — число, значение — чётность (dict comprehension)

dict_num = {i: 'true' if i % 2 == 0 else 'false' for i in range(1, 6)}
print(dict_num)

# 9 Список квадратов, только если число нечётное (list comprehension + условие)

sqr_num = [i ** 2 for i in range(1, 11) if i % 2 != 0]
print(sqr_num)

# 10 Инвертирование словаря (dict comprehension)

a = {'a': 1, 'b': 2, 'c': 3}
b = {v: k for k, v in a.items()}
print(b)
