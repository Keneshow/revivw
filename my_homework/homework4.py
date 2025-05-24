# 1

for i in range(1,31):
    if i % 3 == 0:
        print(i)

# 2

for i in range(10,21):
    if i % 2 == 0:
        print(i)


# 3

word = input("введите слово:")
skip = 'аеёиоуыэюя'
for i in word:
    if i in skip:
        print(i)


# 4
sum_numbers = 0
count = 0
for i in range(1,11):
    sum_numbers += i
    count += 1
    result = sum_numbers / count
print("Среднее арифметическое чисел от 1 до 10:", result)



# 5

text = " я люблю python"
for i in text:
    text = text.replace(" ","")
    print(text)

# 6

for i in range(1, 11):
    result = 5 * i
    print(f"5 x {i} = {result}")

# 7

a = "hello in python"
for i in a:
    print(i.upper())

# 8

result = ""
for i in range(1, 6):
    result += str(i) + " "

result = result.strip()

print(result)


# 9

for i in range(1,11):
    print("*" * i)

# 10
sum = 0
for i in range(1,21):
    if i % 3 == 0 or i % 5 == 0:
       sum += i
print(sum)


