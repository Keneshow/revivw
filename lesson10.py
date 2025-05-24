# list comprehennsion

# from datetime import datetime
# start = datetime.now()
# ovens = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         ovens.append(i)
# end = datetime.now() - start
# print(ovens)
# print(end)
# ovens_1 = [i for i in range(1, 21) if i % 2 == 0]
# print(ovens_1)
#

# ovens = [i for i in range(1, 10)]
# print(ovens)

# set_ovens = {i for i in range(1, 11)}
# print(set_ovens)
# print(type(set_ovens))


#
# uniq_chars = {i for i in "Hello world" if i != " "}
# print(uniq_chars)
#
# a = "Hello world"
# up_words = [ i.upper() for i in a]
# up_word = [i for i in a.upper()]
# print(up_word)
# print(up_words)
#
# my_tuple = tuple(i for i in range(10))
# print(my_tuple)

# my_tuple = tuple(i * 2 for i in range(10))
# print(my_tuple)
#
# double = []
# for i in my_list:
#     i *= 2
#     double.append(i)
# print(double)

fruits = ['banana', 'apple', 'watermelon', 'peach', 'cherry']
len_fruits = [len(i) for i in fruits]
long_word = [len(i) for i in fruits if len(i) > 5]
print(len_fruits)
print(long_word)

a = {x: len(x) for x in fruits}
print(a)

a = {x: x ** 2 for x in range(10)}
print(a)



nums = [3, -7, 0, 3.12, 57, -5, -26, 14]
pos_num = [i for i in nums if i >= 0]
pos_num_2 = [i >= 0 for i in nums]
print(pos_num)
print(pos_num_2)

num = {i ** 2 for i in range(20) if i % 2 == 0}
print(num)

num_2 = [i for i in num if i % 4 == 0]
print(num_2)