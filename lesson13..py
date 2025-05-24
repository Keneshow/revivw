
# def add_(a, b):
#     return a + b

# a = lambda x, y: x + y
#
# #b = a(2, 3)
#
# print(a(2, 3))
#
#
# ff = lambda x: x * 2
# print(ff(7))
#
#
# a = lambda x, y, z: z + y + z
# b = a(7, 9, 5)
# print(b)

# my_list = [(1, 2), (2, 3), (4, 5), (6, 7)]
# a = lambda x: x[1][2]
# print(a(my_list))
#
# a = lambda x: x ** x
# b = a(5)
# print(b)
#
# a = lambda x: x % 2 == 0
# print(a(4))
#
# a = lambda x, y: x if x > y else y
# print(a(12, 24))
#
words = [ 'apple', 'banana', 'apricot']
# # sort = lambda x: sorted(x)
print(sorted(words))
#
# sort = lambda x: sorted(x[::-1])
# print(sorted(words, key=lambda x: x[-1]))

words = [ 'apple', 'banana', 'apricot', 'qiwi']
#len_word = lambda x: len(x)
print(sorted(words, key=lambda x: len(x)))

def multiplier(n):
    return lambda x: x * n


a = multiplier(3)
print(a(5))
######################
#
# words = [ 'apple', 'banana', 'apricot', 'qiwi']
#
# def upper_(x):
#     return x.upper()
# a = map(upper_, words)
# b = map(lambda x: x.upper(), words)
# print(list(a))
# print(list(b))

#a = [i * 2 for i in range(1, 21) if i % 2 == 0]

# num = [i for i in range(1, 21)]
# a = map(lambda x: x * 2, num)
# print(list(a))

# num = [i for i in range(1, 21)]
#
# def sort_(x):
#     if x % 2 == 0:
#         return x
#
# a = filter(lambda x: x % 2 == 0, num)
# b = filter(sort_, num)
# print(list(a))
# print(list(b))

words = [ 'apple', 'banana', 'apricot', 'qiwi']
a = filter(lambda x: len(x) > 5, words)
print(list(a))

num = [i for i in range(1, 21)]
a = map(lambda x: x * 86, num)
print(list(a))

words = [ 'apple', 'banana', 'apricot', 'qiwi', 'carrot', 'potato', 'tomato', 'cherry']
a = filter(lambda x: "a" in x, words)
print(list(a))
b = filter(lambda x: x.startswith('p'), words)
print(list(b))

num = [i for i in range(1, 21)]
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, num))))

words = [ 'apple', '', 'banana', " ", 'apricot', 'qiwi', "", 'carrot', 'potato', 'tomato', 'cherry']
print(list(filter(lambda x: x.replace(" ",''), words)))
print(list(filter(lambda x: x != ' ' and x != "", words)))
print(list(map(lambda x: x[0],filter(lambda x: x != ' ' and x != "", words))))