from tkinter import *
from colors import *
from helpers import *

from pages import HomePage
from pprint import pprint

from database.models.Diagnosis import DiagnosisModel
import json


class EndQueuePage(Canvas, BasePage):
    def __init__(self, window, temp_data=None):
        self.window = window
        self.temp_data = temp_data
        self.lang_code = json.load(open("config.json", "r"))["language"]
        self.data_localization = self.get_localization()
        pprint(temp_data)
        super().__init__(
            window,
            bg=BACKGROUND_COLOUR,
            height=744,
            width=1133,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

    def get_localization(self):
        path = f"locales/{self.lang_code}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data

    def drawPage(self, data = None):
        self.place(x = 0, y = 0)

        # wifi_clock_app = notificationBar(self.window)

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("control/EndQueueFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            377.0,
            image=self.image_image_1
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("control/EndQueueFrame/image_4.png"))
        image_4 = self.create_image(
            566.5,
            304.5,
            image=self.image_image_4
        )

        self.create_text(
            1133.0/2,
            472.0,
            anchor="center",
            justify="center",
            text=self.data_localization['diagnosis_queue_complete'].title(),
            fill="#404040",
            font=("Nunito Bold", 24 * -1),
        )

        self.create_text(
            1133.0/2,
            520.0,
            anchor="center",
            justify="center",
            text=self.data_localization['diagnosis_queue_complete_hint'],
            fill="#8A8C8F",
            font=("Nunito Regular", 16 * -1)
        )

        # Update the UI to ensure all elements are rendered
        self.window.update_idletasks()


        self.window.after(5000, self.go_to_homepage)
        # self.window.mainloop()

    def go_to_homepage(self):
        goToPage(self, HomePage.HomePage(self.window))