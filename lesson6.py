#цикл for

# a = "abcdefg"
# count = 1     #s4et4ik
# for i  in a:
#     print(f"Итерация № {count} Элемент который я взял {i}")
#     count += 1            # s4et4ik + 1


# nums = range(0,101)
# for i in nums:
#     # print(i)


#for i in range(1,11):
#    print(i)

# for i in range(0,101):
#     if i % 2 == 0:
#         if i == 50:
#             break
#         elif i == 24:
#             continue
#         print(i)
#
# for i in range(0,101):
#     if i % 2 != 0:
#         print(i)




# # while True:
# #     num_1 = int(input("a: "))
# #     num_2 = int(input("b: "))
# #     operand = input("x: ")
# #
# #     if num_1 == 'c' or num_2 == 'c' or operand == 'c':
# #         print("stop!!!")
# #         break
# #
# #     if operand == "+":
# #         print(num_1 + num_2)
# #     elif operand == "-":
# #         print(num_1 - num_2)
# #     elif operand == "*":
# #         print(num_1 * num_2)
# #     elif operand == "/":
# #         print(num_1 / num_2)
# #     elif operand == "%":
# #         print(num_1 % num_2)
# #     elif operand == "//":
# #         print(num_1 // num_2)
# #     elif operand == "**":
# #         print(num_1 ** num_2)
# #     else:
# #         print("wrong operation")
#

# a = int(input("TN:"))
# sum = 0
# for i in range(1, a+1):
#     sum += i
#     print(sum)

# word = input("slovo: ")
# count = 0
# for i in word:
#     if i == "a":
#         count += 1
# print(count)

fruits = ["apple", "banana", "charry"]
vegetables =["potato", "tomato", "carrot","onion"]
fruits.extend(vegetables)
print(fruits)

count = 0

for i in fruits:
    if i % 2 == 0:
        count += 1
print(count)