# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#
# Примеры:
#      - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

lst = [1, 4, 988, 7, 5]
max = lst[0]

for i in range(1, len(lst)):
    if lst[i] > max:
        max = lst[i]
print(f'Максимальное число {max}')