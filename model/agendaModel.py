from model.connection import *
from model.entities import *
import calendar
import datetime
import os

class Events():
    """class for add event in the diary"""
    def __init__(self):
        self.db = Connection()
        self.year = 2020
        self.month = 2
        self.str = None

    def create_rdv(self, titre, date, heure, description):
        """method for create user account after register entry in attributes """
        self.db.initialize_connection()
        sql = "INSERT INTO events(titre, date, heure, description) VALUES (%s, %s, %s, %s);"
        arguments = (titre, date, heure, description)
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
        """method for display event if his in bdd"""
        sql = "SELECT events.titre titre , events.date date, events.heure heure, events.description  description FROM events WHERE date = %s;"
        arguments = (date,)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        rows = self.db.cursor.fetchall()
        liste = list()
        for row in rows:
            #print(row[0], row[1], row[2], row[3])
            liste.append(
                {'titre': row[0], 'date': row[1], 'heure': row[2], 'description': row[3]})
        for dicto in liste:
            ydra = Hydrate(dicto)
            ydra.show()
        self.db.close_connection()

    def show_calendar(self):
        """method for display calendar"""
        cal = calendar.TextCalendar(calendar.MONDAY)
        str = cal.formatmonth(self.year, self.month)
        print("\033[36m{}\033[0m".format(str))

