from tkinter import *
from colors import *
from helpers import *

from pages import HomePage
from pprint import pprint

from pages import MedicalRecordPage

from database.models.Diagnosis import DiagnosisModel
import json


class MedicalRecordEditPage(Canvas, BasePage):
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

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordEditFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordEditFrame/image_2.png"))
        image_2 = self.create_image(
            566.0,
            371.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/MedicalRecordEditFrame/image_3.png"))
        image_3 = self.create_image(
            567.0,
            372.0,
            image=image_image_3
        )

        inactive_button_1 = relative_to_assets(f"control/MedicalRecordEditFrame/button_1.png")
        active_button_1 = relative_to_assets(f"control/MedicalRecordEditFrame/active_button_1.png")

        inactive_button_2 = relative_to_assets(f"control/MedicalRecordEditFrame/button_2.png")
        active_button_2 = relative_to_assets(f"control/MedicalRecordEditFrame/active_button_2.png")

        create_hover_button(self.window, 575.0, 446.0, 192.0, 54.0,
                            "white", inactive_button_1, active_button_1,
                            lambda: print("goto edit"))

        create_hover_button(self.window, 366.0, 446.0, 192.0, 54.0,
                            "white", inactive_button_2, active_button_2,
                            lambda: goToPage(MedicalRecordPage.MedicalRecordPage(self.window)))

        self.create_text(
            270.0,
            382.0,
            anchor="nw",
            text="Mohon pastikan data pasien yang tampil di atas sesuai!\nJika data tidak sesuai, silakan kembali untuk memilih data yang benar.",
            fill="#14181F",
            font=("Nunito Regular", 14 * -1)
        )

        self.create_text(
            508.5,
            347.5,
            anchor="nw",
            text="Diagnosisis Pasien",
            fill="#14181F",
            font=("Nunito Regular", 14 * -1)
        )

        self.create_text(
            515.5,
            327.5,
            anchor="nw",
            text="Nama Pasien",
            fill="#14181F",
            font=("Nunito Bold", 17 * -1)
        )

        self.create_text(
            270.0,
            286.0,
            anchor="nw",
            text="Pastikan Data Pasien Benar",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.window.mainloop()