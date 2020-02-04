from model.connection import *
from controller.controller import *
from view.hydrate import *
class Events():
    """class for add event in the diary"""
    def __init__(self):
        self.db = Connection()
        self.title = None
        self.date = None
        self.heure = None
        self.new_datta = None
        self.description = None
        self.verif = Verify()
    def create_rdv(self):
        """method for create user account after register entry in attributes """
        self.db.initialize_connection()
        self.title = input("\033[35menter title :\33[0m")
        self.date = input("\033[35menter date format AAAA-MM-JJ :\33[0m")
        self.heure = input("\033[35menter heure format HH:MM :\33[0m")
        self.description = input("\033[35menter your description :\33[0")
        self.db.cursor.execute("INSERT INTO events(titre, date, heure, description) VALUES "
                                   "(%s, %s, %s, %s);",
                                   (self.title, self.date, self.heure, self.description))
        self.db.connection.commit()
        self.db.close_connection()

    def change_datta(self):
        """method for delete events after connect to bdd"""
        column = ""
        while column not in ['titre', 'date', 'heure', 'description']:
            column = input("\033[35mentry champ to change \n[titre], [date], [heure], [description]]\33[0m")
            self.date = input("\033[35mdate :\33[0m")
            self.hour = input("\033[35mhour :\33[0m")
            self.new_datta = input("\033[35menter new datta :\33[0m")
            self.db.initialize_connection()
            self.db.cursor.execute("UPDATE events set " + column + " = %s WHERE  date = %s AND heure = %s;", (self.new_datta, self.date, self.hour))
            self.db.connection.commit()
            self.db.close_connection()

    def del_events(self):
        """"method for delete user account after connect to bdd"""
        self.db.initialize_connection()
        self.date = input("\033[35menter date : \33[0m")
        self.heure = input("\033[35menter heure :\33[0m")
        self.verif.verifEvents(self.date, self.heure)
        #self.db.cursor.execute("DELETE FROM events WHERE date = %s AND heure = %s;", (self.date, self.heure))
        #self.db.connection.commit()
        #self.db.close_connection()

    def display_events(self):
        self.date = input("\033[35menter date for view events:\33[0m")
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM events WHERE date = %s;", (self.date,))
        views = self.db.cursor.fetchall()
        print(views)
        self.db.close_connection()
        showevents = Hydrate(views)
        showevents.show_informations(views)
        #return views