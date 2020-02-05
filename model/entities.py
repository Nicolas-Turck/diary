from model.agendaModel import*
class Hydrate():
    """class for hydrate attribut before print them"""
    def __init__(self, views):
        """method for initialise atrributs """
        self.titre = None
        self.date = None
        self.heure = None
        self.description = None
        #if views:
        self.hydrate(views)


    def hydrate(self, views):
        """method for add elem in attribus"""
        for i in views:
            print(i)
            for j in i:
                print(j)

                """for key_name, value_name in j:
                    if hasattr(self, key_name):
                        setattr(self, key_name, value_name)"""

    def show(self):
        """method for display elem of city"""
        events = "title \n \
                    date : {} \n\
                    heure : {} \n\
                    description : {} \n"
        print(events.format(self.titre, self.date, self.heure, self.description))