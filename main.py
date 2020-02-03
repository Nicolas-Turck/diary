from model.connection import *
from view.display import *


if __name__=='__main__':

    test = Connection()
    test.initialize_connection()
    test.close_connection()
    view = Display()
    view.show_calendar()