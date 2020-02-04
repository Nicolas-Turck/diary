from model.connection import *
class Verify():
    """ class for verify user entry"""
    def __init__(self):
        self.date = None
        self.heure = None
        self.db = Connection()

    def verifEvents(self, date, heure):
        """method for compore date and heure with bdd date and heure"""
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT date, heure FROM events;")
        elem = self.db.cursor.fetchall()
        print(elem)
        if elem:
            for row in elem:
                for i in row:
                    if self.date == date and self.heure == heure:
                        print("found")
                else:
                    print("not found")
