import os
from view.agendaView import *
year = 2020
month = 2
cal= calendar.TextCalendar(calendar.MONDAY)
str = cal.formatmonth(year, month)
date = datetime.date.today()
strr = date
print("\033[31mHello Doctor  Derieux \nwe are the : {}\033[0m".format(strr))
print("\033[36m{}\033[0m".format(str))

if __name__=='__main__':
    choice = ""
    #views = None
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
            #os.system("clear")
            test = Display()
            test.request_events()

        if choice == "v":
            #os.system("clear")
            viewevents= Display()
            viewevents.show_events()
            #print(views)

        if choice == "d":
            #os.system("clear")
            delette = Display()
            delette.del_events()

        if choice == "w":
            #os.system("clear")
            write = Display()
            write.change_datta()


        if choice == "q":
            exit()


