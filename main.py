from view.display import *
from model.commander import *



import os
test = Display()
test.show_calendar()
if __name__=='__main__':
    choice = ""
    while choice != "q":
        choice = input("enter (n) next month (p) previous month \n"
                       "(c) create events (v) view events (d) delette events (w) change events (q) exit : ")
        if choice == "n":
            test.next_month()
        if choice == "p":
            test.previous_month()
        if choice == "c":
            create = Events()
            create.create_rdv()
        if choice == "v":
            test = Display()
            test.show_events()
        if choice == "d":
            delette = Events()
            delette.del_events()
        if choice == "w":
            write = Events()
            write.change_datta()
        if choice == "q":
            exit()


