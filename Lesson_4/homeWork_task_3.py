# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# - Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]

a = [1,1,2,4,5,6,7,7,8]
b = list(set(a))
# print(f'b = : {b} ')

c = []
for i in a:
    for j in b:
        if i != j:
            c.append(j)
    break

print(f'Ввод: {a}, результат: {c}')