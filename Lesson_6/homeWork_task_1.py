# Задача: предложить улучшения кода(3-5задач) для уже решённых задач:
#     С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Задача из Lesson_2 \ homeWork_task_3
# Задайте словарь из n чисел последовательности (1 + (1/n))^n
# и выведите на экран их сумму.
#     *Пример:*
#     - Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
#     Необходимо сложить все значения словаря и вывести  сумму на экран.

n = 3   # int(input("Введите число N: "))

# с помощью использования map:
mydict  = dict(map(lambda x: (x, round(((1 + (1/x)) ** x),3)), [i for i in range(1, n+1)] ))
# print(mydict )

symm = 0
for key in mydict.keys():
    symm = symm + mydict[key]

print(f'Для n = {n}: {mydict}')
print(f'Сумма значений словаря = {symm}')