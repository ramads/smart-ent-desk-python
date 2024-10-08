from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar

from pages import DiagnosisQuestionPage
from pages import PatientQueuePage

from database.models import MedicalFacility, PatientMedicalFacility
from config import DUMMY_MEDICAL_FACILITY
import json


class DiagnosisPage(Canvas, BasePage):
    def __init__(self, window, temp_data=None):
        self.window = window
        self.lang_code = json.load(open("config.json", "r"))["language"]
        self.data_localization = self.get_localization()
        self.medical_facility_data = MedicalFacility.MedicalFacilityModel().get_medical_facility(DUMMY_MEDICAL_FACILITY)
        self.patient_medical_facility = PatientMedicalFacility.PatientMedicalFacilityModel()
        self.temp_data = temp_data
        self.checking()

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
    
    def checking(self):
        self.patient_medical_facility.update_queue(
            status_periksa='periksa',
            NIK=self.temp_data['NIK'],
            id_faskes=self.temp_data['id_faskes'],
            tanggal_pendaftaran=self.temp_data['tanggal_pendaftaran']
        )

    def cancel_checking(self):
        self.patient_medical_facility.update_queue(
            status_periksa='tunggu',
            NIK=self.temp_data['NIK'],
            id_faskes=self.temp_data['id_faskes'],
            tanggal_pendaftaran=self.temp_data['tanggal_pendaftaran']
        )

    def drawPage(self, data=None):
        self.place(x=0, y=0)

        # wifi_clock_app = notificationBar(self.window)

        inactive_button_1 = relative_to_assets(f"control/DiagnosisFrame/{self.lang_code}/button_1.png")
        active_button_1 = relative_to_assets(f"control/DiagnosisFrame/{self.lang_code}/active_button_1.png")
        
        inactive_button_2 = relative_to_assets(f"control/DiagnosisFrame/{self.lang_code}/button_2.png")
        active_button_2 = relative_to_assets(f"control/DiagnosisFrame/{self.lang_code}/active_button_2.png")

        inactive_button_3 = relative_to_assets(f"control/DiagnosisFrame/{self.lang_code}/button_3.png")
        active_button_3 = relative_to_assets(f"control/DiagnosisFrame/{self.lang_code}/active_button_3.png")

        inactive_button_4 = relative_to_assets(f"control/DiagnosisFrame/{self.lang_code}/button_4.png")
        active_button_4 = relative_to_assets(f"control/DiagnosisFrame/{self.lang_code}/active_button_4.png")
        
        create_hover_button(self.window, 41.0, 223.0, 332.0, 319.0,
                            BACKGROUND_COLOUR, inactive_button_1, active_button_1, 
                            lambda: goToPage(DiagnosisQuestionPage.DiagnosisQuestionPage(self.window, self.temp_data, 'telinga', DiagnosisPage)))
        
        create_hover_button(self.window, 402.0, 223.0, 330.0, 319.0,
                            BACKGROUND_COLOUR, inactive_button_2, active_button_2,  
                            lambda: goToPage(DiagnosisQuestionPage.DiagnosisQuestionPage(self.window, self.temp_data, 'tenggorokan', DiagnosisPage)))
        
        create_hover_button(self.window, 761.0, 223.0, 332.0, 319.0,
                            BACKGROUND_COLOUR, inactive_button_3, active_button_3,  
                            lambda: goToPage(DiagnosisQuestionPage.DiagnosisQuestionPage(self.window, self.temp_data, 'hidung', DiagnosisPage)))
        
        create_hover_button(self.window, 471, 635.0, 192.0, 54.0,
                            BACKGROUND_COLOUR, inactive_button_4, active_button_4,  
                            lambda: [self.cancel_checking(), goToPage(PatientQueuePage.PatientQueuePage(self.window))])

        image_image_1 = PhotoImage(
            file=relative_to_assets(f"control/DiagnosisFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        self.create_text(
            1133/2.0,
            590.0,
            anchor="center",
            justify="center",
            text=self.data_localization["select_diagnosis"].capitalize(),
            fill="#FFFFFF",
            font=("Nunito SemiBold", 16 * -1)
        )

        self.create_text(
            21.0,
            13.0,
            anchor="nw",
            text="9:41",
            fill="#FFFFFF",
            font=("SFProText Semibold", 15 * -1)
        )

        self.create_text(
            130.0,
            117.5,
            anchor="nw",
            text=self.medical_facility_data['nama_faskes'],
            fill="#FFFFFF",
            font=("Nunito Black", 14 * -1)
        )

        self.create_text(
            130.0,
            144.5,
            anchor="nw",
            text="Unit THT",
            fill="#F1F1F1",
            font=("Nunito SemiBold", 12 * -1)
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets(f"control/DiagnosisFrame/image_4.png"))
        image_4 = self.create_image(
            89.0,
            139.0,
            image=image_image_4
        )

        self.window.mainloop()
