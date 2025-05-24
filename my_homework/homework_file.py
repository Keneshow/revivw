from importlib.resources import contents


# 1

with open('new_text.txt', 'r') as f:
    content = f.readlines()
    for line in content:
        print(line)                  # по строчно
#    print(content)                  # в строку


# 2

with open('new_data.txt', 'r') as f:
    line_count = sum(1 for line in f)
    print(f"Количество строк: {line_count}")


# # 3


with open('new_data.txt', 'r') as f:
    symbol = sum(len(line) for line in f)
print(f"Количество символов: {symbol}")


# # 4

lines = ['Привет, мир!', 'Как дела?', 'Python — это круто!']     # Ошибка декодинга выходит но добавляет
a = ['Hello world', 'How are you?', 'Python is cool!']
with open('new_output.txt', 'w', encoding='utf-8') as f:         # нашел в гугле решение
    f.writelines(f'{i}\n' for i in lines)
    f.writelines(f'{i}\n' for i in a)


# 5

import shutil

shutil.copy('new_input.txt', 'new_copy.txt')


## какой из вараинтов более часто используемый и правильный , можете написать в коментариях
#shutil.copyfile
#shutil.copymode
#shutil.copy2

# 6

with open('new_data.txt', 'r') as f:
    word_count = sum(len(line.split()) for line in f)
print(f"Количество слов: {word_count}")


# 7

with open('new_data.txt', 'r', encoding='utf-8') as f:
    longest_line = max(f, key=len)

print(f"Самая длинная строка: {longest_line.strip()}")
print(f"Длина: {len(longest_line)} символов")


# 8

with open('new_poem.txt', 'r', encoding='utf-8') as f:
    text = f.read()

new_text = text.replace('Любовь', 'Радость')

with open('poem_new.txt', 'w', encoding='utf-8') as f:
    text = f.write(new_text)


# 9

with open('new_numbers.txt', 'r') as f:
    lines = f.readlines()
result = sum(int(line.strip()) for line in lines)
print(f'Сумма всех чисел: {result}')


# 10

try:
    with open('new_none.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        print("Файл успешно открыт.")
except FileNotFoundError:
    print("Файл отсутствует!")
