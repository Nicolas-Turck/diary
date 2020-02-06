from model.connection import *
from model.entities import *


class Events():
    """class for add event in the diary"""
    def __init__(self):
        self.db = Connection()

    def create_rdv(self, titre, date, heure, description):
        """method for create user account after register entry in attributes """
        sql = "INSERT INTO events(titre, date, heure, description) VALUES (%s, %s, %s, %s);"
        arguments = (titre, date, heure, description)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def change_datta(self, column, date, heure, new_datta):
        """method for delete events after connect to bdd"""
        sql = "UPDATE events set " + column + " = %s WHERE  date = %s AND heure = %s;"
        arguments = (new_datta, date, heure)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def del_events(self, date, heure):
        """"method for delete user account after connect to bdd"""
        self.db.initialize_connection()
        sql = "DELETE FROM events WHERE date = %s AND heure = %s;"
        arguments = (date, heure)
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def display_events(self, date):
        datta = {}
        sql = "SELECT events.titre titre , events.date date, events.heure heure, events.description  description FROM events WHERE date = %s;"
        arguments = (date,)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        #datta = self.db.cursor.fetchall()
        donnees = self.db.cursor.fetchone()
        fields = self.db.cursor.description
        i = 0
        for field in fields:
            datta[field[0]] = str(donnees[i])
            i += 1
            print(datta)

        ydra = Hydrate(datta)
        ydra.show()
        self.db.close_connection()
