from fractions import Fraction

def get_value():
    value = input('Введите число: ')
    try:
        value = Fraction(value)
        return value
    except ValueError:
        value = complex(value)
        return value

def get_operator():
    oper = input('Введите оператор вычисления (+, -, *, / ) : ')
    flag = False
    while not flag:
        if oper == '+' or oper == '-' or oper == '*' or oper == '/':
            flag = True
            return oper
        else:
            print('Неверный оператор, повторите ввод')
            oper = input('Введите оператор вычисления (+, -, *, / ) : ')

def get_result(res):
    print(f'Результат: {res}')