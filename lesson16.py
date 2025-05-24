#
file = open('teaching.txt', 'r')
file_content = file.read()
print(file_content)
file.close()

import pprint
from importlib.resources import contents
#
# try:
#     file = open("test.txt", 'r')            # r -> "read"
#     contents = file.read()
#     print(file.read())
# except Exception as e:
#     print(e)
# finally:
#     file.close()
#
#
#
# try:
#     file = open("test.txt", 'w')            # w -> "write"
#     file.write('hello world')
#     file.close()
# except Exception as e:
#     print(e)
# # finally:
# #     file.close()
#
#
# try:
#     file = open("lesson.txt", 'a')            # a -> "add"
#     file.write('hello world')
#     file.close()
# except Exception as e:
#     print(e)


# file = open('lesson.txt', 'r')
# content = file.read()
# file.close()
# print(type(content))
# print(content)
# print("------" * 20)
#
# file = open('lesson.txt', 'r')
# line = file.readlines()
# file.close()
# print(type(line))
# print(line)
# print('----' * 20)

#
# with open('lesson.txt', 'r') as f:
#     content = f.readlines()
#     for line in content:
#         print(line)
#     pprint.pprint(content)
#

#
#
# with open('test.txt', 'w') as f:
#     nums = [i for i in range(20)]
#     for num in nums:
#         f.write(str(num))
#
#
# with open('lesson.txt', 'r') as f:
#     a = f.readline()
#     print(a)
#     b = f.readline()
#     print(b)
#
#
#
# nums = [str(i) for i in range(1, 100)]
# with open('test.txt', 'a') as f:
#     f.writelines(nums)              # iteration
#
#
# nums = [str(i) for i in range(1, 100)]
# with open('test.txt', 'a') as f:
#     f.write('asdasdada')            # omly one object add

#
# a = {"a": "a", "b": "b", "c": "c"}
# with open('test.txt', 'a') as f:
#     for k, v in a.items():
#         f.write(f"{k}: {v}\n")
#
#

nums = [i for i in range(1, 50)]
with open('test.txt', 'a') as f:
   f.writelines(f"{num}\n" for num in nums)

nums = [i for i in range(1, 50)]
file = open('text.txt', 'w')
for i in nums:
    file.write(i + '\n')







############################



file = open("new_file.txt")

lines = 0
words = 0
symbols = 0

for line in file:
    lines += 1
    words += len(line.split())
    symbols += len(line)

print("Lines:", lines)
print("Words:", words)
print("Symbols:", symbols)
