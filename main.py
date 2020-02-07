import os
from view.agendaView import *
year = 2020
month = 2
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
            os.system('cls' if os.name == 'nt' else 'clear')
            month += 1
            cal = calendar.TextCalendar(calendar.MONDAY)
            str = cal.formatmonth(year, month)
            print("\033[36m{}\033[0m".format(str))

        if choice =="p":
            os.system('cls' if os.name == 'nt' else 'clear')
            month -= 1
            cal = calendar.TextCalendar(calendar.MONDAY)
            str = cal.formatmonth(year, month)
            print("\033[36m{}\033[0m".format(str))

        if choice == "c":
            os.system('cls' if os.name == 'nt' else 'clear')
            test = Display()
            test.request_events()
        if choice == "v":
            os.system('cls' if os.name == 'nt' else 'clear')
            viewevents= Display()
            viewevents.show_events()
        if choice == "d":
            os.system('cls' if os.name == 'nt' else 'clear')
            delette = Display()
            delette.del_events()
        if choice == "w":
            os.system('cls' if os.name == 'nt' else 'clear')
            write = Display()
            write.change_datta()
        if choice == "q":
            exit()


