# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
#                     - x=34; y=-30 -> 4
#                     - x=2; y=4-> 1
#                     - x=-34; y=-30 -> 3

x = float(input("Введите координату точки по Х:"))
y = float(input("Введите координату точки по Y:"))

if (x > 0 and y > 0):
    print("Точка находится в первой координатной четверти")
elif (x < 0 and y > 0):
    print("Точка находится во второй координатной четверти")
elif (x < 0 and y < 0):
    print("Точка находится в третьей координатной четверти")
elif (x > 0 and y < 0):
    print("Точка находится в четверой координатной четверти")
else:
    print("Введена нулевая координата по X и/или Y")
