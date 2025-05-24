# dictionary изменяемый не упорядочный тип данных

# dict{}
#
# a = {}
#
# b = dict{}

#a = { key : value}

# a = {
#     "Natasha" : 50,
#     "Ivan" : 30,
#     "george" : 40
#    # "Natasha" : 100     # last work
# }
# print(a)
# a["Sergey"] = 50
# print(a)
# a["Natasha"] = 80
# print(a)
# a["Natasha"] = a["george"]
# print(a)
#
# print(a.get("Talgat", "такого ключа нет"))      #check
#
#
a = {
    "Natasha" : 50,
    "Ivan" : 30,
    "george" : 40
}
print(a.items())
print(a.keys())
print(a.values())

# a.pop("Natasha")
#print(a)

# books = {}
#
# books["Пушкин"] = "дети капитана гранта"
# books["Достоевский"] = "сборник стихов"
# books["Щедрин"] = "Сказаки на ночь"
# books["Лев толстой"] = "преступление и наказание"
# books["Тютче и Фет"] ="том рассказов"
# print(books)



# a = {
#     "Natasha" : 50,
#     "Ivan" : 30,
#     "george" : 40
# }
# for k, v in a.items():               # k, v == like "i"
#     if k == "Natasha":
#      #   v = v * 2
#         print(v)
# print(a)
#
# for k in  a.keys():
#     if k == "Natasha":
#         print("sdasasds")
#
# for v in a.values():
#     print(v)

# students = {
#     "Mike": {"age": 15, "grade": 5},
#     "Greg": {"age": 13, "grade": 4},
# }
# print(students["Mike"]["grade"])

# students = {
#     "Mike": {"Math": 5, "physics": 3},
#     "Greg": {"Math": 5, "physics": 4, "History": 3},
# }
#
# for k,v in students.items():
#     avg = sum(v.values()) / len(v)
#     print(f"student {k} has average is: {avg}")

# students = {
#     "Mike" : 5,
#     "Greg" : 3,
#     "Nat" : 4,
#     "Max" : 5
# }
#
# n_stud["Tony"] = [4]
# for k, v in students:
#     if k != "Tony":
#         students.update(n_stud)
# print(students)

# text = "hello"
# freq = {
#     "h": 1,
#     "e": 1,
#     "l": 2,
#     "o": 1
# }
# freq = {}
# for letter in text:
#     if letter in freq:
#         freq[letter] += 1
#     else:
#         freq[letter] = 1
# print(freq)

a = {"x": 2, "y": 3, "z": 4}
b = {"x": 5, "y": 6, "z": 7, "d": 8}
c = {}
for i in a:
    c[i] = a[i]
for i in b:
    if i in c:
        c[i] += b[i]
    else:
        c[i] = b[i]
print(c)