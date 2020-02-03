from model.connection import *

class Create_event():
    """class for add event in the diary"""

    def __init__(self):
        self.choice = Connection()
        self.title = None
        self.date = None
        self.heure = None
        self.description = None

    def create_rdv(self):
        """method for create user account after register entry in attributes """
        self.choice.initialize_connection()
        self.title = input("enter title :")
        self.date = input("enter date format AAAA-MM-JJ :")
        self.heure = input("enter heure format HH:MM :")
        self.description = input("enter your description :")

        self.choice.cursor.execute("INSERT INTO events(titre, date, heure, description) VALUES "
                                   "(%s, %s, %s, %s);",
                                   (self.title, self.date, self.heure, self.description))
        self.choice.connection.commit()
        self.choice.close_connection()