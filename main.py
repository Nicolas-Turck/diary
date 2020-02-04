from view.display import *
from model.commander import *
from view.hydrate import *
import os
test = Display()
test.show_calendar()
if __name__=='__main__':
    choice = ""
    views = None
    while choice != "q":
        choice = input("\033[32menter:\n-(n) next month\n-(p) previous month\n"
                       "-(c) create events\n-(v) view events\n-(d) delette events\n-(w) change events\n-(q) exit : \033[0m")
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
            viewevents= Events()
            viewevents.display_events()
            #print(views)
            #showevents = Hydrate(views)
            #showevents.show_informations()
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


