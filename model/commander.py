from model.connection import *

class Events():
    """class for add event in the diary"""
    def __init__(self):
        self.db = Connection()
        self.title = None
        self.date = None
        self.heure = None
        self.new_datta = None
        self.description = None

    def create_rdv(self):
        """method for create user account after register entry in attributes """
        self.db.initialize_connection()
        self.title = input("enter title :")
        self.date = input("enter date format AAAA-MM-JJ :")
        self.heure = input("enter heure format HH:MM :")
        self.description = input("enter your description :")
        self.db.cursor.execute("INSERT INTO events(titre, date, heure, description) VALUES "
                                   "(%s, %s, %s, %s);",
                                   (self.title, self.date, self.heure, self.description))
        self.db.connection.commit()
        self.db.close_connection()

    def change_datta(self):
        """method for delete events after connect to bdd"""
        column = ""
        while column not in ['titre', 'date', 'heure', 'description']:
            column = input("entry champ to change \n[titre], [date], [heure], [description]]")
            self.date = input("date :")
            self.hour = input("hour :")
            self.new_datta = input("enter new datta :")
            self.db.initialize_connection()
            self.db.cursor.execute("UPDATE events set " + column + " = %s WHERE  date = %s AND heure = %s;", (self.new_datta, self.date, self.hour))
            self.db.connection.commit()
            self.db.close_connection()

    def del_events(self):
        """"method for delte user account after connect to bdd"""
        self.db.initialize_connection()
        self.date = input("enter date : ")
        self.heure = input("enter heure :")
        self.db.cursor.execute("DELETE FROM events WHERE date = %s AND heure = %s;", (self.date, self.heure))
        self.db.connection.commit()
        self.db.close_connection()