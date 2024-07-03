from tkinter import *

from pages.HomePage import HomePage
from helpers import *
from colours import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry(DEFAULT_APP_CONTROL_GEOMETRY)
        self.configure(bg=BACKGROUND_COLOUR)
        self.title(APP_TITLE)

        self.homePage = HomePage(self)

        switchPage(self.homePage)

app = App()