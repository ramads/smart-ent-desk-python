from tkinter import *

from pages import (HomePage, DEarProcessPage as page)
from helpers import *
from colors import *

from database.init import Generate_Database

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry(DEFAULT_APP_CONTROL_GEOMETRY)
        self.configure(bg=BACKGROUND_COLOUR)
        self.title(APP_TITLE)

        self.homePage = HomePage.HomePage(self)

        Generate_Database().create_tables()

        goToPage(self.homePage)

app = App()