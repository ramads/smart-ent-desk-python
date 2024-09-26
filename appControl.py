import threading
from tkinter import *

from libs import dongle_conn
from libs.camera_port import *
from pages import HomePage
from pages import DongleNotification
from helpers import *
from colors import *
import config

from database.core.data_sync import DataSync


class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry(DEFAULT_APP_CONTROL_GEOMETRY)
        self.configure(bg=BACKGROUND_COLOUR)
        self.title(APP_TITLE)

        config.CAMERA_PORT = int(find_camera())
        if config.CAMERA_PORT is not None:
            print(f"Camera found at index {config.CAMERA_PORT} ===============")
        else:
            print("No camera available.")

        # validate dongle
        if not dongle_conn.DongleCom().isValid():     # correct_Id "12345"
            goToPage(DongleNotification.DongleNotification(self))
        else:
    
            self.homePage = HomePage.HomePage(self)
            self.data_sync = DataSync('database/data_sync.json')            
            self.periodic_sync()
            goToPage(self.homePage)

    def periodic_sync(self):
        self.data_sync.sync_data()
        threading.Timer(3600*24, self.periodic_sync).start()


app = App()