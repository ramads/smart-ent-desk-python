from tkinter import *
from colors import *
from helpers import *
from libs.serial_com import SerialCom
import config
# from notificationBar import notificationBar

from pages import HomePage
import json


class SoftwareHardware(Canvas, BasePage):

    seriCom = SerialCom()

    def __init__(self, window):
        self.window = window
        self.lang_code = json.load(open("config.json", "r"))["language"]
        self.data_localization = self.get_localization()
        self.camera_conn = config.CAMERA_PORT
        self.dongle_conn = config.DONGLE_ID == "123" #sementara
        self.seriCom_conn = self.seriCom.connect()

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

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("control/SoftwareHardware/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("control/SoftwareHardware/image_2.png"))
        image_2 = self.create_image(
            566.0,
            392.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("control/SoftwareHardware/vacuum_card.png"
                                    ) if self.seriCom_conn is True else relative_to_assets("control/SoftwareHardware/disconnected_vacuum_card.png"))
        image_3 = self.create_image(
            819.0,
            431.0,
            image=self.image_image_3
        )

        endoscope_card = PhotoImage(
            file=relative_to_assets("control/SoftwareHardware/endoscope_card.png"
                                    ) if self.camera_conn is not None else relative_to_assets("control/SoftwareHardware/disconnected_endoscope_card.png"))
        image_4 = self.create_image(
            312.0,
            431.0,
            image=endoscope_card
        )

        dongle_card = PhotoImage(
            file=relative_to_assets("control/SoftwareHardware/dongle_card.png"
                                    ) if self.dongle_conn is True else relative_to_assets("control/SoftwareHardware/disconnected_dongle_card.png"))
        image_5 = self.create_image(
            312.0,
            293.0,
            image=dongle_card
        )

        self.create_text(
            77.0,
            175.0,
            anchor="nw",
            text=self.data_localization["hardware_software"].title(),
            fill="#000000",
            font=("Nunito Bold", 25 * -1)
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("control/SoftwareHardware/sprayer_card.png"
                                    ) if self.seriCom_conn is True else relative_to_assets("control/SoftwareHardware/disconnected_sprayer_card.png"))
        image_6 = self.create_image(
            819.0,
            293.0,
            image=self.image_image_6
        )

        # self.window.mainloop()