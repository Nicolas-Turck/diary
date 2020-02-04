from model.commander import*
class Hydrate():
    """class for hydrate attribut before print them"""


    def __init__(self, views):
        """method for initialise atrributs """
        self.titre = None
        self.date = None
        self.heure = None
        self.description = None
        #self.model = Events()
        #self.views = None
        self.hydrate(views)


    def hydrate(self, views):
        """method for add elem in attribus"""

        for key_name, value_name in views.items():
            if hasattr(self, key_name):
                setattr(self, key_name, value_name)

    def show_informations(self):
        """method for display elem of city"""

        information  = "\033[36mevents \n \
        Title : {} \n\
        Date : {} \n\
        Hour : {} \n\
        Description : {}\033[0m"

        print(information.format(self.titre, self.date, self.heure, self.description))