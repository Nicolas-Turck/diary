from model.connection import *
class Change_event():
    """class for change event in the diary"""

    def __init__(self):
        self.db = Connection()

    """"def change_datta(self):
        method for delte user account after connect to bdd
        column = ""
        while column not in ['titre', 'date', 'heure', 'description']:
            column = input("entry champ to change \n[titre], [date], [heure], [description]]")
            self.olddatta = input("enter old datta")
            datta = input("enter new datta:")
            self.db.initialize_connection()
            self.db.cursor.execute("UPDATE events set " + column + " = %s WHERE  %s IN %s" , (, self.olddatta, ))
            self.db.connection.commit()
            self.db.close_connection()"""
