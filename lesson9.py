#

#set -- mnojestva
#frozenset -- zamorojenie


# b = [1, 2, 3, 3]
# print(b)
# a = set(b)
#
# print(a)

# s = {1, 2, 3}
# s.add(4)
# print(s)
# s.remove(2)
# print(s)
# s.discard(10)       #like remove
# print(s)

# a = {1, 2, 3}
# b = {4, 5, 3}
# print(a.intersection(b))        # perese4eniee mnojestv
# print(a & b)        # & -- znak perese4enie

# print(a.union(b))                    # ob'edinenie
# print(a | b)                        # znak

# print(a.difference(b))          # uniq ellement iz "a" kot net v "b"
# print(a - b)                    # znak
#
# print(a.symmetric_difference(b))        # uniq zna4eniya krome povtoryaiywihsya
# print(a ^ b)                            # znak


# a =frozenset()


####################


num_format = input("vvedite nomer: ")
hours = int(input("vvedite vremya: "))
price = 30
price = 50
# discount = 0.1
is_old_number = False
is_new_number = False

if len(num_format) == 6 and num_format[0].isalpha() and num_format[1:5].isdigit() and num_format[5].isalpha():
    is_old_number = True
elif len(num_format) == 12 and num_format[:2].isdigit() and num_format[2:4] == KG and num_format[4:7].isdigit() and num_format[7:].isalpha():
    is_new_number == True
if is_old_number:
    price = 30
    type_number = "starii"
elif is_new_number:
    price = 50
    type_number = "novii"
else:
    print("nevernii format nomera...")

total_cost = price * hours
discount = 0
if hours > 5:
    discount = total_cost * 0.1
    total_cost -= discount
print(f"Тип номера: {type_number}")
print(f"Тариф: {price} сом за час")
if discount > 0:
    print(f"Скидка: {discount} сом")
print(f"Итоговая сумма: {total_cost} сом")