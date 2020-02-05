
import calendar
import datetime
from model.entities import *
from model.agendaModel import Events

class Display():
    """class for display all informations of program"""
    def __init__(self):
        self.year = 2020
        self.month = 2
        self.date = None
        #self.db = Connection()
        self.events = Events()
        self.hydr = Hydrate()



    def show_events(self):
        """method for display events  """
        date = input("\033[35menter date for view events:\33[0m")

        self.events.display_events(date)
        """if view:
            for row in view:
                print("\n\033[36mrendez vous  :  {} ".format(row['titre']))
                print("a faire  {} \n le {} à {}\033[0m".format(
                    row['description'],
                    row['date'].strftime("%d/%m/%Y"),
                    row['heure'].strftime("%H:%M")
                ))
                print("\n------------------------------")
        else:
            print("\033[36mno events \033[0m")"""

    def request_events(self):
        self.hydr.titre = input("\033[35menter title :\33[0m")
        self.hydr.date = input("\033[35menter date format AAAA-MM-JJ :\33[0m")
        self.hydr.heure = input("\033[35menter heure format HH:MM :\33[0m")
        self.hydr.description = input("\033[35menter your description :\33[0")
        self.events.create_rdv()

    def change_datta(self):
        """method for delete events after connect to bdd"""
        column = ""
        while column not in ['titre', 'date', 'heure', 'description']:
            column = input("\033[35mentry champ to change \n[titre], [date], [heure], [description]]\33[0m")
            self.date = input("\033[35mdate :\33[0m")
            self.hour = input("\033[35mhour :\33[0m")
            self.new_datta = input("\033[35menter new datta :\33[0m")

    def del_events(self):
        """"method for delete user account after connect to bdd"""

        date = input("\033[35menter date : \33[0m")
        heure = input("\033[35menter heure :\33[0m")
        self.events.del_events(self)


    def display_events(self):
        self.date = input("\033[35menter date for view events:\33[0m")
