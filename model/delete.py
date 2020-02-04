from model.connection import *
class Delete_event():
    """class for delette event in diary """
    def __init__(self):
        self.heure = None
        self.date = None
        self.db = Connection()

    def del_events(self):
        """"method for delte user account after connect to bdd"""
        self.db.initialize_connection()
        self.date = input("enter date : ")
        self.heure = input("enter heure :")
        self.db.cursor.execute("DELETE FROM events WHERE date = %s AND heure = %s;", (self.date, self.heure))
        self.db.connection.commit()
        self.db.close_connection()
