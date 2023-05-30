import view 
import database

def main():
    while True:
        ask = view.user_input()
#        print(ask)
        if ask == 1:
            data = view.man()
            database.add_dat(data)
        elif ask == 2:
            name = view.search()
            database.search_name(name)
        elif ask == 3:
            database.sort_db_name()
        elif ask == 4:
            database.sort_db_data()
        elif ask == 5:
            database.print_name()
        elif ask == 6:
            database.print_db()
        elif ask == 7:
            name = view.search_name()
            family = view.search_family()
            database.delete_dat(name, family)
        elif ask == 8:
            name = view.search_name()
            family = view.search_family()
            database.change_dat(name, family)
        elif ask == 9:
            break

main()