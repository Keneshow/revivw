# # function
#
# def hello_world():
#     print("hello world!")
#
#
# hello_world()
#
#
# def hello(name, age):
#     print(f"hello {name}, your age {age} year old? ")
#
# hello("John", 25)
#
# a = "Almanbet"
# b = 31
#
# hello(a, b)
#
#
# def add_(num_1, num_2):
#     return num_1 + num_2
#
#
# def minus(num_1, num_2):
#     return num_1 - num_2
#
#
# def devide(num_1, num_2):
#     return num_1 / num_2
#
#
# def multipy(num_1, num_2):
#     return num_1 * num_2
#
#
# def calculate(num_1, num_2, operand):
#     if operand == "+":
#         return add_(num_1, num_2)
#     elif operand == "-":
#         return minus(num_1, num_2)
#     elif operand == "/":
#         return devide(num_1, num_2)
#     elif operand == "*":
#         return multipy(num_1, num_2)
#     else:
#         "wrong operand"
#
# while True:
#     a = int(input("num_1"))
#     b = int(input("num_2"))
#     c = input("tp operand (+/-/*//):")
#     if c == "stop":
#         break
#     else:
#         a = calculate(a, b, c)
#         print(a)

a = ""
"But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"
def count_of_vowels(text):
    vowels = "aeiou"
    count = 0
    num_count = 0
    symbol = ",/./?"
    count_sym = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
            if char.isdigit():
                num_count += 1
            if symbol in text:
                count_sym += 1
        return f"vowels {count} numbers {num_count} symbol {count_sym} "

print(count_of_vowels(a))