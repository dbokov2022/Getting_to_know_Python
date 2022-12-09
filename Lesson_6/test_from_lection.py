data = '1 2 3 5 8 15 23 38'.split()

res = list(map(int, data))  # преобразуем в список
print(res)

res = list(filter(lambda x: not x % 2, res))  # выбраны четные
print(res)

res = list(map(lambda x: (x, x**2), res))  # x**2
print(res)

