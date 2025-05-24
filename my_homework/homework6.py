
# 1

person = {
    "name" : "Alice",
    "age" : 25,
    "city" : "Moscow"
}
print(person)
person["profession"] = "develop"
person["age"] = 26
person.pop("city")
print(person)
print(person.get("name"))
print(person.items())

# 2

students = {
    "Анна" : 85,
    "Борис" : 90,
    "ВИктор" : 78,
    "Галина" : 92
}
max_score = 0
top_student = ""
for k, v in students.items():
    if v > max_score:
        max_score = v
        top_student = k

print("Студент с максимальным баллом:", top_student, "с баллом", max_score)
count_80 = 0

for v in students.values():
    if v > 80:
        count_80 += 1
print("Количество студентов с баллом выше 80:", count_80)



# 3

a = {}

for i in range(1, 6):
    a[i] = i ** 2
print(a)

# 4

words = ["cat", "dog", "cat", "bird", "dog", "cat"]
a = {}

for i in words:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
print(a)

# 5

info = {}

keys = ['name', 'age', 'city']
values = ['Ivan', 30, 'Moscow']
for i in range(len(keys)):
    info[keys[i]] = values[i]

print(info)
