from view.display import *
from model.create import *
from model.delete import *
from model.change import *
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
            testcreate = Create_event()
            testcreate.create_rdv()
        if choice == "v":
            test.show_events()
        if choice == "d":
            test = Delete_event()
            test.del_events()
        if choice == "w":
            test = Change_event()
            test.change_datta()
        if choice == "q":
            exit()


