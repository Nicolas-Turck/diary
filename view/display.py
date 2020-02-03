from model.connection import *
import calendar
class Display():
    """class for display all informations of program"""
    def __init__(self):

        self.choice = Connection()
    def show_calendar(self):
        """method for display calendar with calendar method of python"""
        c = calendar
        print(calendar.month(2020, 2))
        print(c)

    def show_events(self):
        """method for display events  """

        self.choice.initialize_connection()
        self.choice.cursor.execute("SELECT * FROM events;")
        view = self.choice.cursor.fetchall()
        self.choice.close_connection()

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