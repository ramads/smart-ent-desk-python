from tkinter import *

from pages import (HomePage, PreviewImagePage)
from helpers import *
from colours import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry(DEFAULT_APP_CONTROL_GEOMETRY)
        self.configure(bg=BACKGROUND_COLOUR)
        self.title(APP_TITLE)

        self.homePage = HomePage.HomePage(self)
        # self.homePage = PreviewImagePage.PreviewImagePage(self)

        goToPage(self.homePage)

app = App()