from datetime import datetime as dt


def get_log(res, oper, num1, num2):
    dtime = dt.now().strftime('%d.%m.%Y %H:%M:%S')
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write('{}; калькуляция: {} {} {} = {}\n'
                     .format(dtime, num1, oper, num2,  res))