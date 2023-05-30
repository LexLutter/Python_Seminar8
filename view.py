def user_input():
    ask = int(input("-------------------------\n Выбери ниже: \n 1 - записать пользователя \n 2 - поиск имени \n"
                    " 3 - отсортировать справочник по имени \n 4 - сортировка по дате рождения \n"
                    " 5 - вывод только имён абонентов \n 6 - вывод справочника \n 7 - удалить запись по имени и фамилии \n 8 - изменить запись по имени и фамилии \n 9 - выход \n"))
    print('-------------------------')
    return ask

def man():
    name = input("Введите имя: ")
    family = input("Введите фамилию: ")
    father = input("Введите отчество: ")
    date = input("Введите дату рождения: ")
    telephone = input("Введите номер телефона: ")
    data = name + ";" + family + ";" + father + ";" + date + ";" + telephone + ";" + "\n"
    return data

def search():
    str_search = input("Введите строку для поиска: ")
    return  str_search

def search_name():
    str_search = input("Введите искомое имя: ")
    return  str_search

def search_family():
    str_search = input("Введите искомую фамилию: ")
    return  str_search