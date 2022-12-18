# Функция главного меню
def main_menu():
    print('-' * 85 )
    print('Главное меню')
    mode = input('1. Импорт данных(записать данные в книгу)\n2. Экспорт данных(показать всю книгу)\n3. Поиск\n4. Выход\nВведите 1, 2, 3 и 4: ')
    if mode in '1234':
        return int(mode)
    else:
        print('Ошибка! Введите 1, 2, 3 или 4!')


def input_data():
    last_name = input("Введите Фамилию: ")
    first_name = input("Введите Имя: ")
    phone_number = input("Введите Телефон: ")
    note = input("Введите примечание: ")
    return [last_name, first_name, phone_number, note]


def print_data(data):
    if len(data) > 0:
        print("\nФамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
        print("-"*85)

        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
            if item == len(data):
                break
                # return

    else:
        print("Справочник пуст!")