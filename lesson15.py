from setuptools.command.alias import alias

a = 5
b = 10


try:
    x = int(input("type something:"))             # какой-то опасный код
    y = int(input("type something:"))
    operand = input("operand: ")
    if operand == "+":
        print(x + y)
    elif operand == "-":
        print(x - y)
    elif operand == "*":
        print(x * y)
    elif operand == "/":
        print(x / y )
except ValueError:
    print("that's a not number")
except ZeroDivisionError:
    print("you can't divide by zero")

#alias  --> as
#
# def hello(name: str):
#     try:
#         print(f"hello {name}")
#     except Exception as e:
#         print(f"Error : {e} ")
#
#
# hello(234, 234, 234)

#
# try:
#     x = int(input("type num: "))
#     y = int(input("type num: "))
#     result = x / y
# except ZeroDivisionError:
#     print("you can't divide zero")
# else:
#     print(f"выполняется блок else: {result}")
# finally:
#     print(f"этот блок выполняется всегда.")             # finally --> завершение процесса
#
# class TooYouong(Exception):
#     pass
#
#
# def register(age: int):
#     if age < 18:
#         raise TooYouong("you are young")
#     else:
#         print(age)
#
#
# register(15)
#



