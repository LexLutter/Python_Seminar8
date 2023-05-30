def add_dat(data):
    with open("db.txt", "a") as file:
        file.write(data)
    print("Телефонная книга обновлена.\n")

def search_name(name):
    with open("db.txt", "r") as file:
        data = file.readlines()
        flag = False
        for i in data:
            if name in i:
                print(i)
                flag = True
        if flag == False:
            print("Абонента по заданным данным не найдено.\n")

def sort_db_name():
    with open("db.txt", "r") as file:
        data = file.readlines()
        data.sort()
    with open("db.txt", "w") as file:
        file.writelines(data)

def sort_db_data():
    with open("db.txt", "r") as file:
        data = file.readlines()
        data.sort(key = lambda x: x[4])
    with open("db.txt", "w") as file:
        file.writelines(data)

def print_name():
    with open("db.txt", "r") as file:
        data = file.readlines()
        for i in data:
            print(i.split(";")[0])

def print_db():
    with open("db.txt", "r") as file:
        print(file.read())

def delete_dat(name, family):
    with open("db.txt", "r") as file:
        data = file.readlines()
        data_clone = []
        flag = False
        for i in data:
            if name and family in i:
                print(f"Запись с именем {name} и фамилией {family} удалена.")
                flag = True
            else:
                data_clone.append(i)
        if flag == False:
            print("Запись по заданным данным не найдена.\n")
    with open("db.txt", "w") as file:
        file.writelines(data_clone) 

def change_dat(name, family):
    with open("db.txt", "r") as file:
        data = file.readlines()
        data_clone = []
        flag = False
        for i in data:
            if name and family in i:
                print(f"Введите номер изменяемого атрибута: \n   1 - имя \n   2 - фамилия \n   3 - отчество \n   4 - дата рождения \n   5 - номер телефона")
                k = int(input())
                j = i.split(";")
                if k == 1:
                   i = i.replace(j[0], input("Введите новое имя: "))
                   data_clone.append(i)
                elif k == 2:
                    i = i.replace(j[1], input("Введите новую фамилию: "))
                    data_clone.append(i)
                elif k == 3:
                    i = i.replace(j[2], input("Введите новое отчество: "))
                    data_clone.append(i)
                elif k == 4:
                    i = i.replace(j[3], input("Введите новую дату рождения: "), 1)
                    data_clone.append(i)
                elif k == 5:
                    i = i.replace(j[4], input("Введите новый номер телефона: "), 1)
                    data_clone.append(i)
                flag = True
            else:
                data_clone.append(i)
        if flag == False:
            print("Запись по заданным данным не найдена.\n")
    with open("db.txt", "w") as file:
        file.writelines(data_clone)