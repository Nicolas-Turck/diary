from model.connection import *
from view.display import *
from model.create import *
from model.delete import *
from model.change import *

if __name__=='__main__':

    test = Connection()
    test.initialize_connection()
    test.close_connection()
    view = Display()
    view.show_calendar()
    choice =""
    while choice != "q":
        choice = input("enter (c) for create events (v) for view events (d) for delette events (w) for change events : ")
        if choice == "c":
            testcreate = Create_event()
            testcreate.create_rdv()
        if choice == "v":
            view.show_events()

        if choice == "d":
            test = Delete_event()
            test.del_events()
        if choice == "w":
            test = Change_event()
            test.change_datta()
