# # tri_ovn_num = []
# # oven = []
# # five_onum = []
# # count = 0
# # oven_count = 0
# # five_count = 0
# #
# # for i in range(100):
# #     if i % 3 == 0:
# #         tri_ovn_num.append(i)
# #         count += i          # +=1 (tipa_len)
# #         if i % 2 == 0:
# #             oven.append(i)
# #             oven_count += i
# #             if i % 5 == 0:
# #                 five_onum.append(i)
# #                 five_count += i
# #
# # print(tri_ovn_num)
# # print(count)
# # print(len(tri_ovn_num))
# # print(oven)
# # print(oven_count)
# # print(len(oven))
# # print(five_onum)
# # print(five_count)
# # print(len(five_onum))
#
# # data = [2.71, 3.14, 1.41, 1.62]
# # total = 0
# # for i in data:
# #     total = total + i
# #     print(total)
# #
# # numbers = []
# #
# # while True:
# #     value = int(input("Введите целое число (0 для завершения ввода): "))
# #     if value == 0:
# #         break
# #     numbers.append(value)
# #
# # numbers.sort()  # Сортируем список в порядке возрастания
# #
# # #print("Введенные числа в порядке возрастания:")
# # for number in numbers:
# #     print(number)
#
# # import copy
# # list = [1,2,4,3,5]
# # deep_copy = copy.deepcopy(list)
# # deep_copy[2][0] = '3'
# # print(deep_copy)
# # print(list)
#
# nums = [-5, 3, 0, -2, 8]
# filtered_nums = [num for num in nums if num >= 0]
# print(filtered_nums)
#
# nums = [-5, 3, 0, -2, 8]
# filtered_nums = []
#
# for num in nums:
#     if num >= 0:
#         filtered_nums.append(num)
#
# print(filtered_nums)
#
# students = { "Анна": 85, "Борис": 90, "Виктор": 78, "Галина": 92 }
#
# # Ищем студента с максимальным баллом
# max_score = 0
# top_student = ""
#
# for student, score in students.items():
#     if score > max_score:
#         max_score = score
#         top_student = student
#
# print("Студент с максимальным баллом:", top_student, "с баллом", max_score)
#
# # Считаем количество студентов с баллом выше 80
# # count_above_80 = 0
# #
# # for score in students.values():
# #     if score > 80:
# #         count_above_80 += 1
# #
# # print("Количество студентов с баллом выше 80:", count_above_80)



################

# Запрашиваем номер машины
number_plate = input("Введите номер машины: ")

# Запрашиваем количество часов
hours = int(input("Введите количество часов: "))

# Определяем тип номера
is_old_number = False
is_new_number = False

# Проверяем формат старого номера
if len(number_plate) == 6 and number_plate[0].isalpha() and number_plate[1:5].isdigit() and number_plate[5].isalpha():
    is_old_number = True
# Проверяем формат нового номера
elif len(number_plate) == 1 and number_plate[:2].isdigit() and number_plate[2:4] == "KG" and number_plate[4:7].isdigit() and number_plate[7:].isalpha():
    is_new_number = True

# Определяем стоимость
if is_old_number:
    rate = 30
    type_of_number = "Старый номер"
elif is_new_number:
    rate = 50
    type_of_number = "Новый номер"
else:
    print("Неверный формат номерного знака.")
    exit()

# Рассчитываем стоимость
total_cost = rate * hours

# Применяем скидку, если больше 5 часов
discount = 0
if hours > 5:
    discount = total_cost * 0.1
    total_cost -= discount

# Выводим результаты
print(f"Тип номера: {type_of_number}")
print(f"Тариф: {rate} сом за час")
if discount > 0:
    print(f"Скидка: {discount} сом")
print(f"Итоговая сумма: {total_cost} сом")

