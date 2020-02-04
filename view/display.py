from model.connection import *
import calendar
import datetime
class Display():
    """class for display all informations of program"""
    def __init__(self):
        self.year = 2020
        self.month = 2
        self.date = None
        self.db = Connection()

    def show_calendar(self):
        """method for display calendar with calendar method of python"""
        cal= calendar.TextCalendar(calendar.MONDAY)
        str = cal.formatmonth(self.year,self. month)
        date = datetime.datetime.now()
        strr = date
        print(strr)
        print(str)

    def next_month(self):
        """method for change for next month"""
        self.month += 1
        cal = calendar.TextCalendar(calendar.MONDAY)
        str = cal.formatmonth(self.year, self.month)
        print(str)

    def previous_month(self):
        """method for change for previous month"""
        self.month -= 1
        cal = calendar.TextCalendar(calendar.MONDAY)
        str = cal.formatmonth(self.year, self.month)
        print(str)

    def show_events(self):
        """method for display events  """
        self.date = input("enter date for view events:")
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM events WHERE date = %s;",(self.date,))
        #self.db.cursor.execute("DELETE FROM events WHERE date = %s AND heure = %s;", (self.date, self.heure))
        view = self.db.cursor.fetchall()
        self.db.close_connection()
        for row in view:
            print("\nrendez vous  :  {} ".format(row['titre']))
            print("a faire  {} \n le {} à {}".format(
                row['description'],
                row['date'].strftime("%d/%m/%Y"),
                row['heure'].strftime("%H:%M")
            ))
            print("\n------------------------------")


        #else:
            #print("no events ")