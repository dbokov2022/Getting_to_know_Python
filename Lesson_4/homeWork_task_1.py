# Вычислить число Пи c заданной точностью d
# Пример:
#     - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10

import  math

d = 0.0001
k = len(str(d))
# print(f'd = {d};  k = {k}')

# p = math.pi

p = 0
for i in range(0, 1000000):
    p += 4/(2*i+1)*(-1)**i

print(f'Число π = {p}')

# т.к. в комментарии к заданию прозвучало "поработать со строкой":
if 1 > d > 0.00001 and str(d)[:2] == '0.':
    p = round((math.floor(p / d) * d), k-2)  # округление вниз
    print(f'Число π = {p}   (c заданной точностью d = {d}) ')
elif d == 1:
    print(f'Число π = {p}   (c заданной точностью d = {d})')
else:
    print('Расчет с такой точностью в настоящее время невозможен ')




# логичный вариант:
# ost = p % d
# if ost < d/2:
#   p = (math.floor(p / d) * d) # округление вниз
# else:
#   p = (math.ceil(p / d) * d)  # округление вверх
#
# print(f'Число π = {p}   (c заданной точностью d = {d})')