# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции + ,- ,/ ,*. приоритет операций стандартный.
# Пример:
# 2 + 2 => 4;
# 1 + 2 * 3 = > 7;
# 1 - 2 * 3 = > -5;

# n = '1-2*3'
# print(eval(n))  # преобразует строку в числа и считает

# num = '1 - 2 * 3 / 5'
num = '1 + 2 * 3'
print(num)

num = num.split()
# print(num)

while len(num) > 1:
    while '*' in num or '/' in num:
        if num.count('*') > 0 and num.count('/') > 0:
            if num.index('/') > num.index('*'):
                num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                num.pop(num.index('*') + 1)  # удаляем
                num.pop(num.index('*'))     # удаляем
                # print(num)
            else:
                num[num.index('/') - 1] = int(num[num.index('/') - 1]) * int(num[num.index('/') + 1])
                num.pop(num.index('/') + 1)
                num.pop(num.index('/'))
                # print(num)
        else:
            if '*' in num:
                num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                num.pop(num.index('*') + 1)
                num.pop(num.index('*'))
                # print(num)
            else:
                num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
                num.pop(num.index('/') + 1)
                num.pop(num.index('/'))
                # print(num)

    while '+' in num or '-' in num:
        if num.count('+') > 0 and num.count('-') > 0:
            if num.index('-') > num.index('+'):
                num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
                num.pop(num.index('+') + 1)
                num.pop(num.index('+'))
                print(num)
            else:
                num[num.index('-') - 1] = int(num[num.index('-') - 1]) + int(num[num.index('-') + 1])
                num.pop(num.index('-') + 1)
                num.pop(num.index('-'))
                print(num)
        else:
            if '+' in num:
                num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
                num.pop(num.index('+') + 1)
                num.pop(num.index('+'))
            else:
                num[num.index('-') - 1] = int(num[num.index('-') - 1]) - int(num[num.index('-') + 1])
                num.pop(num.index('-') + 1)
                num.pop(num.index('-'))
print(num)


