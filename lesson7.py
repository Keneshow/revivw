

#list()  # spisok
#
# my_list = [7, 3.14, 'some string', ['some string 2']]
#
# a = "so,me st,ri,ng"
# print(a.split(","))
#
# print(my_list[0:3])

# fruits = ['apple', 'orange', 'strawberry', 'peach']
# print(fruits)
#
# fruits.append('banana')
# print(fruits)
#
#
# fruits = ["apple"]
# vegetables =["potato", "tomato", "carrot","onion"]
# print(fruits)
# fruits.extend(vegetables)
# print(fruits)
#
#
# fruits = ["apple", "banana", "charry"]
# fruits.insert(1,"orange")
# print(fruits)
#
# fruits = ["apple", "banana", "charry"]
# for i in fruits:
#     if i == "banana":
#         fruits.append("orange")
#     elif len(i) < 6:
#         fruits.remove(i)
#     else:
#         print("nothing to see here")
# print(fruits)


# ovens =[]
#
# for i in range(100):
#     if i % 2 == 0:
#         ovens.append(i)
#
# print(ovens)

# ovens = []
#
# for i in range(100):
#     if i % 3 == 0:
#         ovens.append(i)
# print(ovens)

# summa vsex 4isel
#

tri_ovn_num = [i for i in range(100) if i % 3 == 0]
count = sum(tri_ovn_num)
oven = [i for i in tri_ovn_num if i % 2 == 0]
oven_count = sum(oven)
five_onum = [i for i in oven if i % 5 == 0]
five_count = sum(five_onum)

print(tri_ovn_num)
print(count)
print(len(tri_ovn_num))
print(oven)
print(oven_count)
print(len(oven))
print(five_onum)
print(five_count)
print(len(five_onum))


# tri_ovn_num = []
# oven = []
# five_onum = []
# count = 0
# oven_count = 0
# five_count = 0
#
# for i in range(100):
#     if i % 3 == 0:
#         tri_ovn_num.append(i)
#         count += i          # +=1 (tipa_len)
#         if i % 2 == 0:
#             oven.append(i)
#             oven_count += i
#             if i % 5 == 0:
#                 five_onum.append(i)
#                 five_count += i
#
# print(tri_ovn_num)
# print(count)
# print(len(tri_ovn_num))
# print(oven)
# print(oven_count)
# print(len(oven))
# print(five_onum)
# print(five_count)
# print(len(five_onum))

#
fruits = ["apple", "banana", "cherry"]
vegetables = ["potato", "tomato", "carrot", "onion"]

fruits.extend(vegetables)

count = sum(1 for i in fruits if len(i) % 2 == 0)
print(count)
#

fruits = ["apple", "banana", "charry"]
vegetables =["potato", "tomato", "carrot","onion"]
fruits.extend(vegetables)
print(fruits)

count = 0

for i in fruits:
    if len(i) % 2 == 0:
        count += 1
print(count)

# a = ("asda", "sadfas", 25)
# print(type(a))
# a = list(a)
# print(type(a))
#
# print("Python" > "python")

# a = ["01", "02", "03", "04"]
#
# for i in range(0,101):
#     a.append(i)
# print(a)
#
# for i in a:
#     if "0" in str(i):
#         a.remove(i)
# print(a)

num = []
for i in range(0,101):
    if i % 5 == 0:
        num.append(i * 2)
    else:
        num.append(i)
     #   summa = num * 2
print(num)

# block_word = ["какаха", "банан"]
#
# while True:
#     guest_word = input("text:")
#     if guest_word in block_word:
#         print('you banned')
#         break
#     else:
#         print("hmm. interesting!!!")
