# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

def InputList():
    # lst = [2, 3, 4, 5, 6]
    # lst = [2, 3, 5, 6]

    lst = []
    N = int(input('Введите размер списка с клавиатуры:'))
    for x in range(N):
        x = input('Введите значение списка:')
        try:
            lst.append(int(x))
        except ValueError:
            lst.append(x)

    print(f'\nВведен список: {lst} ')
    return lst

def calc(lst):
    lst2 = []
    n = len(lst)
    for i in range(len(lst) ):
        try:
            while i < len(lst) / 2 and n > len(lst) / 2:
                n = n - 1
                p = lst[i] * lst[n]
                lst2.append(p)
                i += 1
        except ValueError:
            lst2.append(i)

    print(f'Произведение пар чисел списка: {lst2} ')

lst = InputList()
calc(lst)