from tkinter import *
from colors import *
from helpers import *
from pages import DEarProcessPage, DiagnosisQuestionPage
# from notificationBar import notificationBar
from pprint import pprint
import json
class DEarPage(Canvas, BasePage):
    def __init__(self, window, temp_data=None):
        self.window = window
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
        self.temp_data = temp_data
        pprint(self.temp_data)
        self.get_disease_title(self.temp_data['diagnosis_type'])

    def get_disease_title(self, disease):
        if self.lang_code == 'id':
            self.disease_title = f"{self.data_localization['disease']} {self.data_localization[disease]}"
        else:
            self.disease_title = f"{self.data_localization[disease]} {self.data_localization['disease']}"

    def get_localization(self):
        path = f"locales/{self.lang_code}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data

    def drawPage(self):
        self.place(x=0, y=0)

        # wifi_clock_app = notificationBar(self.window)

        inactive_button_1 = relative_to_assets(f"control/DEarFrame/{self.lang_code}/button_1.png")
        active_button_1 = relative_to_assets(f"control/DEarFrame/{self.lang_code}/active_button_1.png")
        
        inactive_button_2 = relative_to_assets(f"control/DEarFrame/{self.lang_code}/button_2.png")
        active_button_2 = relative_to_assets(f"control/DEarFrame/{self.lang_code}/active_button_2.png")

        create_hover_button(self.window, 431.0, 600.0, 136.0, 42.0,
                            "#FFFFFF", inactive_button_1, active_button_1, 
                            lambda: goToPage(DiagnosisQuestionPage.DiagnosisQuestionPage(self.window, self.temp_data)))        
        create_hover_button(self.window, 575.0, 600.0, 136.0, 42.0,
                            "#FFFFFF", inactive_button_2, active_button_2,  
                            lambda: goToPage(DEarProcessPage.DEarProcessPage(self.window, self.temp_data)))

        image_image_1 = PhotoImage(
            file=relative_to_assets(f"control/DEarFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets(f"control/DEarFrame/image_2.png"))
        image_2 = self.create_image(
            571.0,
            414.0,
            image=image_image_2
        )

        self.create_text(
            1133/2,
            565.0,
            anchor="center",
            justify="center",
            text=self.data_localization['before_proceed'],
            fill="#8A8C8F",
            font=("Nunito Regular", 15 * -1)
        )

        self.create_text(
            1133/2,
            522.0,
            anchor="center",
            justify="center",
            text=self.disease_title.title(),
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets(f"control/DEarFrame/image_3.png"))
        image_3 = self.create_image(
            568.0,
            326.0,
            image=image_image_3
        )

        self.window.mainloop()
