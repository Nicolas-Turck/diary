from model.connection import *
from view.display import *
from model.create import *
from model.delete import *
from model.change import *


calendar = Display()
calendar.show_calendar()
if __name__=='__main__':
    choice =""
    while choice != "q":
        choice = input("enter (n) for next month (p) for prvious month \n"
                       "(c) for create events (v) for view events (d) for delette events (w) for change events : ")

        if choice =="n":
            next = Display()
            next.next_month()

        if choice == "p":
            prev = Display()
            prev.previous_month()

        if choice == "c":
            testcreate = Create_event()
            testcreate.create_rdv()
        if choice == "v":
            view = Display()
            view.show_events()

        if choice == "d":
            test = Delete_event()
            test.del_events()
        if choice == "w":
            test = Change_event()
            test.change_datta()
