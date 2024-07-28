from tkinter import *
from colors import *
from helpers import *

from pages import HomePage, DEarPage
from pprint import pprint

from pages import MedicalRecordPage

from database.models.Diagnosis import DiagnosisModel
import json


class MedicalRecordEditPage(Canvas, BasePage):
    def __init__(self, window, clicked_data):
        self.window = window
        self.clicked_data = clicked_data
        self.temp_data = {
            'id_patient': clicked_data['id_pasien'],
            'id_diagnosis': clicked_data['id_diagnosa'],
            'previous_page': MedicalRecordPage.MedicalRecordPage,
        }
        self.lang_code = json.load(open("config.json", "r"))["language"]
        self.data_localization = self.get_localization()
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

        inactive_button_1 = relative_to_assets(f"control/MedicalRecordEditFrame/{self.lang_code}/continue.png")
        active_button_1 = relative_to_assets(f"control/MedicalRecordEditFrame/{self.lang_code}/active_continue.png")

        inactive_button_2 = relative_to_assets(f"control/MedicalRecordEditFrame/{self.lang_code}/back.png")
        active_button_2 = relative_to_assets(f"control/MedicalRecordEditFrame/{self.lang_code}/active_back.png")

        create_hover_button(self.window, 575.0, 446.0, 192.0, 54.0,
                            "white", inactive_button_1, active_button_1,
                            lambda: goToPage(DEarPage.DEarPage(self.window, self.temp_data, self.clicked_data['jenis_diagnosa'])))

        create_hover_button(self.window, 366.0, 446.0, 192.0, 54.0,
                            "white", inactive_button_2, active_button_2,
                            lambda: goToPage(MedicalRecordPage.MedicalRecordPage(self.window)))

        self.create_text(
            1133/2,
            400.0,
            anchor="center",
            justify="center",
            text=self.data_localization['medical_record_edit_hint'],
            fill="#14181F",
            font=("Nunito Regular", 14 * -1)
        )

        self.create_text(
            1133/2,
            350.5,
            anchor="center",
            text=self.clicked_data['diagnosa'],
            fill="#14181F",
            font=("Nunito Regular", 14 * -1)
        )

        self.create_text(
            1133/2,
            330.5,
            anchor="center",
            text=self.clicked_data['nama_pasien'],
            fill="#14181F",
            font=("Nunito Bold", 17 * -1)
        )

        self.create_text(
            1133/2.0,
            286.0,
            anchor="center",
            text=self.data_localization['medical_record_edit_title'],
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.window.mainloop()