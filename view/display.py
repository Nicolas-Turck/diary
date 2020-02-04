from model.connection import *
import calendar
import datetime
from model.commander import *

class Display():
    """class for display all informations of program"""
    def __init__(self):
        self.year = 2020
        self.month = 2
        self.date = None
        self.db = Connection()
        self.model = Events()
    def show_calendar(self):
        """method for display calendar with calendar method of python"""
        cal= calendar.TextCalendar(calendar.MONDAY)
        str = cal.formatmonth(self.year,self. month)
        date = datetime.date.today()
        #date = datetime.datetime.now()
        strr = date
        #print(strr)
        print("\033[31mHello Doctor  Derieux \nwe are the : {}\033[0m".format(strr))
        print("\033[36m{}\033[0m".format(str))

    def next_month(self):
        """method for change for next month"""
        self.month += 1
        cal = calendar.TextCalendar(calendar.MONDAY)
        str = cal.formatmonth(self.year, self.month)
        print("\033[36m{}\033[0m".format(str))

    def previous_month(self):
        """method for change for previous month"""
        self.month -= 1
        cal = calendar.TextCalendar(calendar.MONDAY)
        str = cal.formatmonth(self.year, self.month)
        print("\033[36m{}\033[0m".format(str))

    def show_events(self):
        """method for display events  """
        view = self.model.display_events()
        if view:
            for row in view:
                print("\n\033[36mrendez vous  :  {} ".format(row['titre']))
                print("a faire  {} \n le {} à {}\033[0m".format(
                    row['description'],
                    row['date'].strftime("%d/%m/%Y"),
                    row['heure'].strftime("%H:%M")
                ))
                print("\n------------------------------")

        else:
            print("no events ")