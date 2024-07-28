from tkinter import *

from pages import (HomePage, DEarProcessPage as page)
from helpers import *
from colors import *
import config
from database.init import Generate_Database

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry(DEFAULT_APP_CONTROL_GEOMETRY)
        self.configure(bg=BACKGROUND_COLOUR)
        self.title(APP_TITLE)

        config.CAMERA_PORT = int(find_camera())
        if config.CAMERA_PORT is not None:
            print(f"Camera found at index {config.CAMERA_PORT } ===============")
            # Pass the cam_index to the kamera.py script or use it as needed
            # For demonstration purposes, we will print it
            # You can also use it to initialize or configure other modules
        else:
            print("No camera available.")

        self.homePage = HomePage.HomePage(self)
        self.homePage.drawPage()

app = App()
app.mainloop()