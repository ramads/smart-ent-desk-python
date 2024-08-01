from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar

from pages import DEarPage
from pages import DiagnosisPage

from pprint import pprint

from database.models.Hospital import HospitalModel
from config import DUMMY_HOSPITAL
import json


class DiagnosisQuestionPage(Canvas, BasePage):
    def __init__(self, window, id_patient=None):
        self.window = window
        self.lang_code = json.load(open("config.json", "r"))["language"]
        self.data_localization = self.get_localization()
        self.hospital_data = HospitalModel().get_hospital(DUMMY_HOSPITAL)
        super().__init__(
            window,
            bg=BACKGROUND_COLOUR,
            height=744,
            width=1133,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.temp_data = {
            'id_patient': id_patient,
            'previous_page': DiagnosisQuestionPage
        }

    def get_localization(self):
        path = f"locales/{self.lang_code}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data

    def loadImage(self):
        return PhotoImage(file=relative_to_assets("image_3.png"))

    def drawPage(self, data=None):
        self.place(x=0, y=0)

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/DiagnosisQuestionFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("control/DiagnosisQuestionFrame/image_2.png"))
        image_2 = self.create_image(
            571.0,
            414.0,
            image=image_image_2
        )

        inactive_continue = relative_to_assets(f"control/DiagnosisQuestionFrame/active_continue.png")
        active_continue = relative_to_assets(f"control/DiagnosisQuestionFrame/inactive_continue.png")

        create_hover_button(self.window, 575.0, 614.0, 136.0, 42.0,
                            "#FFFFFF", inactive_continue, active_continue,
                            lambda: goToPage(DEarPage.DEarPage(self.window, self.temp_data, "telinga")))

        inactive_back = relative_to_assets(f"control/DiagnosisQuestionFrame/inactive_back.png")
        active_back = relative_to_assets(f"control/DiagnosisQuestionFrame/active_back.png")

        create_hover_button(self.window, 430.0, 614.0, 136.0, 42.0,
                            "#FFFFFF", inactive_back, active_back,
                            lambda: goToPage(DiagnosisPage.DiagnosisPage(self.window)))

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/DiagnosisQuestionFrame/image_3.png"))
        image_3 = self.create_image(
            571.0,
            522.0,
            image=image_image_3
        )

        self.create_text(
            230.5,
            301.0,
            anchor="nw",
            text="Lorem ipsum",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("control/DiagnosisQuestionFrame/button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=198.5,
            y=301.5,
            width=22.0,
            height=22.0
        )

        self.create_text(
            102.0,
            176.0,
            anchor="nw",
            text="Diagnosa Telinga",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            102.0,
            229.5,
            anchor="nw",
            text="Sebelum melakukan pemeriksaan fisik, silakan pilih gejala yang sesuai dengan keadaan yang sedang dirasakan pasien.",
            fill="#404040",
            font=("Nunito Regular", 19 * -1)
        )

        # Update the UI to ensure all elements are rendered
        self.window.update_idletasks()

        # self.window.after(2000, self.goToNextPage)  # Delay
        self.window.mainloop()
