# Задача: предложить улучшения кода(3-5задач) для уже решённых задач:
#     С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Задача из Lesson_2 \ homeWork_task_2 :
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N =  4 #  int(input('Введите число '))

# Вариант 1: С помощью функции:
# a = 1
# def fun(a,b):
#     return a*b
#
# for i in range(1, abs(N) + 1):
#     a = fun(a, i)
#     print(a, end=' ')
###################################
# Вариант 2: С помощью лямбды-функции:
# a = 1
# f = lambda a, b:  a * b
#
# l = []
# for i in range(1, abs(N) + 1):
#     a = f(a, i)
#     l.append(a)
# print(l)
######################################
# Вариант 3: С помощью использования лямбды:
# a = 1
# f = lambda a, b:  a * b
#
# for i in range(N):
#     i+=1
#     a = f(a,i)
#     print(a, end=' ')
# ##############################
# Вариант 4: С помощью math, лямбды и map:
import math

l  = [ i for i in range(N)]
res = list(map(lambda x: (math.factorial(x+1)),  l))
print(res)
