from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar

from pages import PatientQueuePage
from pages import NotificationPage
from pages import MedicalRecordPage
from pages import SoftwareHardware
from pages import Settings
from pages import EndQueuePage
from pages import AboutUsPage

# from pages import NotificationDetailv2Page

from config import DUMMY_HOSPITAL
from database.models.Hospital import HospitalModel
import json


class HomePage(Canvas, BasePage):
    def __init__(self, window):
        self.window = window
        self.lang_code = json.load(open("config.json", "r"))["language"]
        self.hospital_data = HospitalModel().get_hospital(DUMMY_HOSPITAL)
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
    
    def drawPage(self):
        self.place(x=0, y=0)

        # wifi_clock_app = notificationBar(self.window)

        inactive_button_1 = relative_to_assets(f"control/HomeFrame/{self.lang_code}/button_1.png")
        active_button_1 = relative_to_assets(f"control/HomeFrame/{self.lang_code}/active_button_1.png")
        
        inactive_button_2 = relative_to_assets(f"control/HomeFrame/{self.lang_code}/button_2.png")
        active_button_2 = relative_to_assets(f"control/HomeFrame/{self.lang_code}/active_button_2.png")

        inactive_button_3 = relative_to_assets(f"control/HomeFrame/{self.lang_code}/button_3.png")
        active_button_3 = relative_to_assets(f"control/HomeFrame/{self.lang_code}/active_button_3.png")
        
        inactive_button_4 = relative_to_assets(f"control/HomeFrame/{self.lang_code}/button_4.png")
        active_button_4 = relative_to_assets(f"control/HomeFrame/{self.lang_code}/active_button_4.png")
        
        inactive_button_5 = relative_to_assets(f"control/HomeFrame/{self.lang_code}/button_5.png")
        active_button_5 = relative_to_assets(f"control/HomeFrame/{self.lang_code}/active_button_5.png")
        
        inactive_button_6 = relative_to_assets(f"control/HomeFrame/{self.lang_code}/button_6.png")
        active_button_6 = relative_to_assets(f"control/HomeFrame/{self.lang_code}/active_button_6.png")
        
        create_hover_button(self.window, 47.0, 216.0, 447.0, 319.0, 
                            BACKGROUND_COLOUR, inactive_button_1, active_button_1,
                            lambda: goToPage(PatientQueuePage.PatientQueuePage(self.window)))
        
        create_hover_button(self.window, 523.0,216.0, 263.0, 319.0, 
                            BACKGROUND_COLOUR, inactive_button_2, active_button_2,  
                            lambda: goToPage(MedicalRecordPage.MedicalRecordPage(self.window)))
        
        create_hover_button(self.window, 815.0,216.0, 271.0, 151.0, 
                            BACKGROUND_COLOUR, inactive_button_3, active_button_3,  
                            lambda: goToPage(NotificationPage.NotificationPage(self.window)))
        
        create_hover_button(self.window, 815.0,384.0, 271.0, 151.0, 
                            BACKGROUND_COLOUR, inactive_button_4, active_button_4,  
                            lambda: goToPage(SoftwareHardware.SoftwareHardware(self.window)))
        
        create_hover_button(self.window, 269.0,591.0, 275.0, 99.0, 
                            BACKGROUND_COLOUR, inactive_button_5, active_button_5,  
                            lambda: goToPage(Settings.Settings(self.window)))
        
        create_hover_button(self.window, 590.0,591.0, 274.0, 99.0,
                            BACKGROUND_COLOUR, inactive_button_6, active_button_6,  
                            lambda: goToPage(AboutUsPage.AboutUsPage(self.window)))

        image_image_1 = PhotoImage(
            file=relative_to_assets(f"control/HomeFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        self.create_text(
            130.0,
            117.5,
            anchor="nw",
            text= self.hospital_data['nama_rumah_sakit'],
            fill="#FFFFFF",
            font=("Nunito Black", 14 * -1)
        )

        self.create_text(
            130.0,
            144.5,
            anchor="nw",
            text=self.data_localization['ent_unit'],
            fill="#F1F1F1",
            font=("Nunito SemiBold", 12 * -1)
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets(f"control/HomeFrame/image_4.png"))
        image_4 = self.create_image(
            89.0,
            139.0,
            image=self.image_image_4
        )

        # self.mainloop()