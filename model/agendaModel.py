from model.connection import *
from model.entities import *


class Events():
    """class for add event in the diary"""
    def __init__(self):
        self.db = Connection()
        self.title = None
        self.date = None
        self.heure = None
        self.new_datta = None
        self.description = None
        self.hydr = Hydrate()



    def create_rdv(self, arg):
        """method for create user account after register entry in attributes """
        sql = "INSERT INTO events(titre, date, heure, description) VALUES (%s, %s, %s, %s);"
        arguments = (arg.titre,  arg.date, arg.heure, arg.description)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def change_datta(self):
        """method for delete events after connect to bdd"""
        self.db.initialize_connection()
        self.db.cursor.execute("UPDATE events set " + column + " = %s WHERE  date = %s AND heure = %s;", (self.new_datta, self.date, self.hour))
        self.db.connection.commit()
        self.db.close_connection()

    def del_events(self):
        """"method for delete user account after connect to bdd"""
        self.db.initialize_connection()
        self.verif.verifEvents(self.date, self.heure)
        self.db.cursor.execute("DELETE FROM events WHERE date = %s AND heure = %s;", (self.date, self.heure))
        self.db.connection.commit()
        self.db.close_connection()

    def display_events(self, date):

        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM events WHERE date = %s;", (self.date,))
        views = self.db.cursor.fetchall()
        print(views)
        self.db.close_connection()
        self.events.__str__(views)
        #showevents = Hydrate(views)
        #showevents.show_informations(views)
        #return views