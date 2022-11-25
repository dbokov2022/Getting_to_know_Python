# Задайте словарь из n чисел последовательности (1 + (1/n))^n
# и выведите на экран их сумму.
#     *Пример:*
#     - Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
#     Необходимо сложить все значения словаря и вывести  сумму на экран.

n = int(input("Введите число N: "))

test_dict = {}
for i in range(1, n+1):
    test_dict[i] = round(((1 + (1/i)) ** i),3)

symm = 0
for key in test_dict.keys():
    symm = symm + test_dict[key]

print(f'Для n = {n}: {test_dict}')
print(f'Сумма значений словаря = {symm}')