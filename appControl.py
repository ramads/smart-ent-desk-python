from tkinter import *

from libs.camera_port import *
from pages import HomePage
from pages import DongleNotification
from helpers import *
from colors import *
import config


class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry(DEFAULT_APP_CONTROL_GEOMETRY)
        self.configure(bg=BACKGROUND_COLOUR)
        self.title(APP_TITLE)

        config.CAMERA_PORT = int(find_camera())
        if config.CAMERA_PORT is not None:
            print(f"Camera found at index {config.CAMERA_PORT } ===============")
        else:
            print("No camera available.")

        if config.DONGLE_ID != "12344":     # correct_Id "12345"
            goToPage(DongleNotification.DongleNotification(self))

        self.homePage = HomePage.HomePage(self)

        goToPage(self.homePage)


app = App()
