from model.agendaModel import*
class Hydrate():
    """class for hydrate attribut before print them"""


    def __init__(self):
        """method for initialise atrributs """
        self.titre = None
        self.date = None
        self.heure = None
        self.description = None
        self.views = None
        #self.hydrate(views)
        #self.views = views

    def hydrate(self, views):
        """method for add elem in attribus"""
        for key_name, value_name in views.items():
            if hasattr(self, key_name):
                setattr(self, key_name, value_name)

    def __str__(self, views):
        if self.view:
            for row in views:
                print("\n\033[36mrendez vous  :  {} ".format(row['titre']))
                print("a faire  {} \n le {} à {}\033[0m".format(
                    row['description'],
                    row['date'].strftime("%d/%m/%Y"),
                    row['heure'].strftime("%H:%M")
                ))
                print("\n------------------------------")
        else:
            print("\033[36mno events \033[0m")