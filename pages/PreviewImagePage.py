from tkinter import *
from colors import *
from helpers import *
from PIL import ImageTk, Image
from notificationBar import notificationBar

from pages import DEarProcessPage
from pages import DEarLoadingPage

from config import LANG_CODE
import json

class PreviewImagePage(Canvas, BasePage):
    def __init__(self, window, temp_data=None):
        self.window = window
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

    def get_localization(self):
        path = f"locales/{LANG_CODE}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data

    def loadImage(self):
        return PhotoImage(file=relative_to_assets("image_3.png"))

    def drawPage(self, data = None):
        self.place(x=0, y=0)

        wifi_clock_app = notificationBar(self.window)

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/PreviewImageFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            378.0,
            image=image_image_1
        )

        captured_img = ImageTk.PhotoImage(Image.open(relative_to_image_capture("test_image.jpg")))
        image_2 = self.create_image(
            566.0,
            292.5,
            image=captured_img
        )

        self.create_text(
            560.0,
            600.0,
            anchor="center",
            text=self.data_localization["make_sure"],
            fill="#8A8C8F",
            font=("Nunito Regular", 15 * -1)
        )


        inactive_button_1 = relative_to_assets(f"control/PreviewImageFrame/{LANG_CODE}/button_1.png")
        active_button_1 = relative_to_assets(f"control/PreviewImageFrame/{LANG_CODE}/active_button_1.png")
        
        inactive_button_2 = relative_to_assets(f"control/PreviewImageFrame/{LANG_CODE}/button_2.png")
        active_button_2 = relative_to_assets(f"control/PreviewImageFrame/{LANG_CODE}/active_button_2.png")
        
        create_hover_button(self.window, 370.5, 631.0, 192.0, 54.0, 
                            "#FFFFFF", inactive_button_1, active_button_1, 
                            lambda: goToPage(DEarProcessPage.DEarProcessPage(self.window, self.temp_data)))
        create_hover_button(self.window, 570.5, 631.0, 192.0, 54.0, 
                            "#FFFFFF", inactive_button_2, active_button_2,  
                            lambda: goToPage(DEarLoadingPage.DEarLoadingPage(self.window, self.temp_data)))



        self.create_text(
            565.0,
            550.0,
            anchor="center",
            text=self.data_localization["taken_success"],
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.create_text(
            21.0,
            13.0,
            anchor="nw",
            text="9:41",
            fill="#FFFFFF",
            font=("SFProText Semibold", 15 * -1))

        self.window.mainloop()