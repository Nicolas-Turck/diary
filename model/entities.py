from model.agendaModel import*
class Hydrate():
    """class for hydrate attribut before print them"""
    def __init__(self, datta):
        """method for initialise atrributs """
        self.titre= None
        self.date = None
        self.heure= None
        self.description = None
        #if views:
        self.hydrate(datta)


    def hydrate(self, datta):
        """method for add elem in attribus"""
        for key_name, value_name in datta.items():
            if hasattr(self, key_name):
                setattr(self, key_name, value_name)

    def show(self):
        """method for display elem of city"""
        events = "title {} \n date : {} \n heure : {}  \n description : {} "
        print(events.format(self.titre, self.date, self.heure, self.description))