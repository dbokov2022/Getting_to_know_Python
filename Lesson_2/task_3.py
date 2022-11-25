# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

# str_arr = str1.split()
# count = 0
# for i in str_arr:
#     if i.lower() == str2.lower():
#         count += 1
# print(count)

print(str1.count(str2))


