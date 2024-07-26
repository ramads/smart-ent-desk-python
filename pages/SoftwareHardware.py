from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar

from pages import HomePage
import json


class SoftwareHardware(Canvas, BasePage):

    def __init__(self, window):
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

    def get_localization(self):
        path = f"locales/{self.lang_code}/string.json"
        with open(path, "r") as file:
            data = json.load(file)
        return data

    def drawPage(self):
        self.place(x=0, y=0)

        # wifi_clock_app = notificationBar(self.window)

        inactive_button_1 = relative_to_assets(f"control/SoftwareHardware/{self.lang_code}/button_1.png")
        active_button_1 = relative_to_assets(f"control/SoftwareHardware/{self.lang_code}/active_button_1.png")

        create_hover_button(self.window, 471.0,662.0, 192.0, 54.0,
                            BACKGROUND_COLOUR, inactive_button_1, active_button_1,
                            lambda: goToPage(HomePage.HomePage(self.window)))

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/SoftwareHardware/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("control/SoftwareHardware/image_2.png"))
        image_2 = self.create_image(
            566.0,
            392.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/SoftwareHardware/connected_image_3.png"))
        image_3 = self.create_image(
            819.0,
            431.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/SoftwareHardware/connected_image_4.png"))
        image_4 = self.create_image(
            312.0,
            431.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("control/SoftwareHardware/connected_image_5.png"))
        image_5 = self.create_image(
            312.0,
            293.0,
            image=image_image_5
        )

        self.create_text(
            77.0,
            175.0,
            anchor="nw",
            text=self.data_localization["hardware_software"].title(),
            fill="#000000",
            font=("Nunito Bold", 25 * -1)
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("control/SoftwareHardware/connected_image_6.png"))
        image_6 = self.create_image(
            819.0,
            293.0,
            image=image_image_6
        )

        self.window.mainloop()