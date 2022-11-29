# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def InputList():
    list1 = []
    N = int(input('Введите размер списка с клавиатуры:'))
    for x in range(N):
        x = input('Введите значение списка:')
        try:
            list1.append(int(x))
        except ValueError:
            list1.append(x)
    return list1

def calc(lst):
    sum = 0
    for i in range(1, len(lst), 2 ):
        sum += lst[i]
    print(f'Сумма элементов списка, стоящих на нечётных позициях = {sum} ')


lst = InputList()
calc(lst)

