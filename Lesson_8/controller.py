import view
from import_data import import_data
from export_data import export_data
from search_data import search_data


def telephone_book():
    menu = 0
    while menu != 4:
        menu = view.main_menu()
        match menu:
            case 1:
                sep = choice_sep()
                import_data(view.input_data(), sep)
            case 2:
                data = export_data()
                view.print_data(data)
            case 3:
                word = input("Введите данные для поиска: ")
                data = export_data()
                item = search_data(word, data)
                if item != None:
                    print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
                    print("-" * 85)
                    print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
                else:
                    print("Данные не обнаружены")



def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep