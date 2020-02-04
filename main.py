from view.display import *
from model.commander import *
import os


test = Display()
test.show_calendar()
if __name__=='__main__':
    choice = ""
    while choice != "q":
        choice = input("\033[32menter (n) next month (p) previous month \n"
                       "(c) create events (v) view events (d) delette events (w) change events (q) exit : \033[0m")
        if choice == "n":
            os.system("clear")
            test.next_month()
        if choice == "p":
            os.system("clear")
            test.previous_month()
        if choice == "c":
            os.system("clear")
            create = Events()
            create.create_rdv()
        if choice == "v":
            os.system("clear")
            test = Display()
            test.show_events()
        if choice == "d":
            os.system("clear")
            delette = Events()
            delette.del_events()
        if choice == "w":
            os.system("clear")
            write = Events()
            write.change_datta()
        if choice == "q":
            exit()


