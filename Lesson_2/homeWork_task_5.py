# Реализуйте алгоритм нахождения рандомного числа.
# (Не используя библиотеки связанные с рандомом)


import random
n=random.randint(-10, 10)
while True:
    text = input("Введите число или стоп для выхода: ")
    if text == "стоп":
        print("Выход из программы! До встречи! Загадано было", n)
        break # инструкция выхода из цикла
    elif text == n:
        print("Победа")
        break
    else:
        print("Попробуйте еще")