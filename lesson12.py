# def hello(name, age):
#     return f"Hello, {name}! You are {age} years old..."
#
#
# print(hello("John", 20))
#
#
# hello(name="JOhn", age=21)
# def hello(name, age):
#     return

#
# def add_(num_1, num_2):
#     return num_1 + num_2
# add_()
#
# def hello(name:str, age:int):
#     return f"Hello, {name}! You are {age} years old..."
#
#
# a = [i for i in range(1, 11)]

#
# x = 10
#
# def my_func():
#     global x
#     x += 5
#
#
# my_func()
# print(x)
#
#
# def outer():
#     x = "outer"
#     def inner():
#         nonlocal x
#         x = "inner"
#     inner()
#     print(x)
#
# outer()

#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# print(factorial(5))


# def summ_(*args):
#     total = summ_(args)
#     return total
#
# print(summ_(1, 2, 3, 4))
#
#
# def summ_(*args):
#     return  [i for i in args if i % 2 == 0 ]
#
# print(summ_(1, 2, 3, 4))
#
#
# def summ_(*args):
#     for i in args:
#         if i % 2 == 0:
#             # zapisat v bazy dannix
#             pass
#
# print(summ_(1,2,3,4,5,6,7,8,9,10))

#
# def sums(**kwargs):
#     return kwargs
#
#
# print(sums(name="Almanbet", age=31))
#

def students(*args):
    return [i for i in args if len(i) >= 4]
print(students("Alice", "Anna", "Olya", "Nat", "Dima", "Den", "Ben", "Bob"))

# filter_stud = ["Alice", "Anna", "Olya", "Nat", "Dima", "Den", "Ben", "Bob"]
# result = students(*filter_stud)
# print(result)

def filtr(*args):
    a = [i for i in args if type(i) == str]
    b = [i * 2 for i in args if type(i) == int]
    return a, b
x = [1, 2, 3, "sdfsdf", 4, 5, 6, "efwefw", 8, 9, 10, "sfsdfsf", "fdsdgdg"]
result = filtr(*x)
print(result)
