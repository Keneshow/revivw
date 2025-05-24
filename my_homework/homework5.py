# 1

my_list = [1, 10,3,7]
max_num = max(my_list)
print(max_num)


# 2

nums = [1,2,3,4,5]
nums.reverse()
print(nums)

# 3

num = [ -5, 3, 0, -2, 8]
for i in num:
    if i < 0:               # if "-" in str(i):
        num.remove(i)
print(num)

#(list comprehension
num = [-5, 3, 0, -2, 8]
num = [i for i in num if i >= 0]
print(num)


# 4

num = [1,7,3]
n_max = num.index(max(num))
print(n_max)

# 5

num = [10, 20, 30, 40, 50]
result = 0
for i in range(len(num)):
    if i % 2 == 0:
        result += num[i]
print(result)

#(list comprehension

num = [10, 20, 30, 40, 50]
result = sum(num[i] for i in range(len(num)) if i % 2 == 0)
print(result)


# 6

words = ['Hello', ' ', 'world', '!']
result = ''.join(words)
print(result)
