number = int(input('num:'))
print('true' if number % 2 == 0 else 'false')

celsius = int(input("C#"))
fahr = (celsius * 1.8) + 32
print(fahr)

text = input("Введите текст : ")
print(len(text))

price_count = int(input("a"))
discount = int(input("b")) / 100
result = price_count - (price_count * discount)
print(result)

num_1 = int(input("a"))
num_2 = int(input("b"))
result = num_1 + num_2
print(result)

num_1 = int(input("x"))
num_2 = int(input("y"))
result = (num_1 + num_2) / 2
print(result)

text = input('Введите текст : ')
times = int(input('n'))
result = text * times
print(result)

num = float(input("number"))
integer = round(num)
print(integer)