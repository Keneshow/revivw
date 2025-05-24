# def hello():
#     print("Hello World")
#
#
# hello()
#
#
# import time
# from random import randint
#
# def outer():
#     def inner():
#         print("inner")
#     return inner()


#outer()
#
# def my_decorater(func):
#     def wrapper():
#         print("before")
#         func()
#         print("after")
#     return wrapper
#
# @my_decorater
# def hello():
#     print("hello")
#
#
# hello()
#
# @my_decorater
# def hello2():
#     print('hello2')
#
#
# hello2()
#
#
#
# from datetime import datetime
#
#
# def decorator(func):
#     def wrapper():
#         print(f"Before {datetime.now()}")
#         func()
#         print(f"After {datetime.now()}")
#     return wrapper
#
#
# @decorator
# def hello():
#     print('Hello')
#
#
# hello()
#
#
# @decorator
# def Steev():
#     print("Steev")
#
#
# Steev()
#
#
# def count(func):
#     count = 0
#     def wrapper():
#         nonlocal count
#         func()
#         count += 1
#         print(f'vizov funcii {count} raz')
#     return  wrapper
#
# @count
# def hello():
#     print("hello")
#
#
# hello()
# hello()
# hello()
#
# @count
# def goodbye():
#     print("good bye")
#
#
# goodbye()
# goodbye()
# goodbye()
# goodbye()
#

def decorator(func):
    def wrapper(*args, **kwargs):
        print("<umk>")
        func(*args, **kwargs)
    return wrapper

@decorator
def hello(name):
    print(f"hello {name}")


hello("Almanbet")


@decorator
def goodbye(name, age, color):
    print(f"good bye {name}, {age}, {color}")

goodbye("Jack", 25, "red")

