from main import *
import os
from view.agendaView import *


class Controller():
    """class for control for user choice """""
    def __init__(self):
        self.year = 2020
        self.month = 2
        cal = Events()
        cal.show_calendar()
        date = datetime.date.today()
        strr = date
        print("\033[31mHello Doctor  Derieux \nwe are the : {}\033[0m".format(strr))

    def start(self):
        choice = ""
        """loops for request an answer for user """
        while choice != "q":
            choice = input("\033[32menter:\n-(n) next month\n-(p) previous month\n"
                           "-(c) create events\n-(v) view events\n-(d) delette events\n-(w) change events\n-(q) exit : \033[0m")

            if choice == "n":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.month += 1
                cal = calendar.TextCalendar(calendar.MONDAY)
                str = cal.formatmonth(self.year, self.month)
                print("\033[36m{}\033[0m".format(str))

            elif choice =="p":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.month -= 1
                cal = calendar.TextCalendar(calendar.MONDAY)
                str = cal.formatmonth(self.year, self.month)
                print("\033[36m{}\033[0m".format(str))

            elif choice == "c":
                os.system('cls' if os.name == 'nt' else 'clear')
                test = Display()
                test.request_events()
            elif choice == "v":
                os.system('cls' if os.name == 'nt' else 'clear')
                viewevents= Display()
                viewevents.show_events()
            elif choice == "d":
                os.system('cls' if os.name == 'nt' else 'clear')
                delette = Display()
                delette.del_events()
            elif choice == "w":
                os.system('cls' if os.name == 'nt' else 'clear')
                write = Display()
                write.change_datta()

            elif choice == "q":
                exit()
