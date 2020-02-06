
from view.agendaView import *
cal = Events()
cal.show_calendar()
date = datetime.date.today()
strr = date
print("\033[31mHello Doctor  Derieux \nwe are the : {}\033[0m".format(strr))
if __name__=='__main__':
    choice = ""
    while choice != "q":
        choice = input("\033[32menter:\n-(n) next month\n-(p) previous month\n"
                       "-(c) create events\n-(v) view events\n-(d) delette events\n-(w) change events\n-(q) exit : \033[0m")

        if choice == "n":
            test = Display()
            test.next_month()
        if choice =="p":
            test = Display()
            test.previous_month()
        if choice == "c":
            test = Display()
            test.request_events()
        if choice == "v":
            viewevents= Display()
            viewevents.show_events()
        if choice == "d":
            delette = Display()
            delette.del_events()
        if choice == "w":
            write = Display()
            write.change_datta()
        if choice == "q":
            exit()


