# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21, 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


fibo = int(input('Введите число = '))
lst = []
for i in range(fibo+1):
    if i==0:
        lst.append(i)
    elif i==1:
        lst.append(i)
        lst.insert(0, i)
    else:
        lst.append(lst[len(lst) - 1] + lst[len(lst) - 2])
        lst.insert(0, (-1) ** (i - 1) * lst[len(lst) - 1])
print(lst)