# Напишите программу, которая принимает на вход число N и
# выдаёт последовательность из N членов.
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81

num = int(input("Введите число n :"))
a = 1
for i in range(num):
    print (a, end='  ')
    a *= (-3)