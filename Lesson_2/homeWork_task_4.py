# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите целое число N = '))

for i in range(-abs(N), abs(N) + 1, 1):
    a = []
    for i in range(-abs(N), abs(N) + 1, 1):
        a.append(i)
print(f'Список элементов от -N до N: {a}')

# b = []
# b = [2,5,6]


# try:
#     file = open("file.txt")
#     try:
#         s = file.readlines()
#         print(s)
#     finally:
#         file.close()
# except FileNotFoundError:
#     print("Невозможно открыть файл")


# with open('filename') as f:
#     lines = [line.rstrip('\n') for line in f]

# path = 'file.txt'
# data = open(path, 'r')
# print(data.read())
# # b = data.read()
# for line in data:
# #     print(line)
#     b.append(line)
# data.close()
# print(f'Список элементов b: {b}')
b = []
# with open("file.txt") as f:
#     line = f.read().splitlines()
#     for i in line:
    #     print(line)
    #     b.append((i).splitlines(","))
    # b= list(f)
    # lines = [line.rstrip('\n') for line in f]
    # lines = f.read().splitlines()  # List with stripped line-breaks
    # for line in f:
    #     b.append(f.strip())

# inp = "file.txt"
# data = open(inp)
# dat = data.read()
# b = dat.splitlines()
# print( b)
    # print(lst) # for python 3
b: ['2', '5', '6']

print(f'Список элементов b: {b}')

c = []  # пустой список, в него будем добавлять нужные элементы из списка a с индексом из списка b
for i in range(len(a)):
    for j in range(len(b)):
        if i == b[j]:
            c.append(a[i])   # добавляем в список
print(f'Список элементов c: {c}')

p = 1
for i in range(len(c)):
    p *= c[i]
print(f'Произведение элементов на указанных позициях : {p}')