import calendar
class Display():
    """class for display all informations of program"""
    def __init__(self):
        pass
    def show_calendar(self):
        """method for display calendar with calendar method of python"""
        c = calendar
        print(calendar.month(2020, 2))
        print(c)