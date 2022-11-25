# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр. (Сделать для строки)
#     *Пример:*
#     - 6782 -> 23
#     - 0,56 -> 11

def calc(string):
    i = 0
    summ = 0
    while i < len(string):
        if  string[i].isdigit():
            print(string[i])
            summ = summ + int(string[i])
        i += 1
    return summ

chislo = input("Введите число: ")
print(f'Сумма цифр строки =  {calc(chislo)}')

################################

#для целых чисел:
# chislo = int(input("Введите число: "))
# summa = 0
# while chislo > 0:
#     ostatok = chislo % 10
#     summa += ostatok
#     chislo //= 10
# print(summa)

#для вещественных чисел:
# chislo = float(input("Введите число: "))
# while chislo % 1 !=0:
#     chislo *= 10
# summa = 0
# while chislo > 0:
#     ostatok = chislo % 10
#     summa += ostatok
#     chislo //= 10
# print(int(summa))

