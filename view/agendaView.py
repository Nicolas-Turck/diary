import calendar
import datetime
import os
from model.agendaModel import Events
from model.entities import *
class Display():
    """class for display all informations of program"""
    def __init__(self):
        self.date = None
        self.hydr = Events()
        self.events =Events()
        self.cal = Events()

    def show_events(self):
        """method for display events  """
        date = input("\033[35menter date for view events:\33[0m")
        os.system('cls' if os.name == 'nt' else 'clear')
        events = self.hydr.display_events(date)


    def request_events(self):
        titre = input("\033[35menter title :\33[0m")
        date = input("\033[35menter date format AAAA-MM-JJ :\33[0m")
        heure = input("\033[35menter heure format HH:MM :\33[0m")
        description = input("\033[35menter your description :\33[0m")
        os.system('cls' if os.name == 'nt' else 'clear')
        self.events.create_rdv(titre, date, heure, description)

    def change_datta(self):
        """method for delete events after connect to bdd"""
        column = ""
        while column not in ['titre', 'date', 'heure', 'description']:
            column = input("\033[35mentry champ to change \n[titre], [date], [heure], [description]]\33[0m")
            date = input("\033[35mdate :\33[0m")
            heure = input("\033[35mhour :\33[0m")
            new_datta = input("\033[35menter new datta :\33[0m")
            os.system('cls' if os.name == 'nt' else 'clear')
            self.events.change_datta(column, date, heure, new_datta)

    def del_events(self):
        """"method for delete user account after connect to bdd"""
        date = input("\033[35menter date : \33[0m")
        heure = input("\033[35menter heure :\33[0m")
        os.system('cls' if os.name == 'nt' else 'clear')
        self.events.del_events(date, heure)



