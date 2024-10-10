from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar
from pprint import pprint
import json
from libs import dongle_conn
from pages import HomePage


class DongleNotification(Canvas, BasePage):
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

    def loadImage(self):
        return PhotoImage(file=relative_to_assets("image_3.png"))

    def reloadDongle(self):
        if dongle_conn.DongleCom().isValid():     # correct_Id "12345"
            self.reload_button.destroy()
            goToPage(HomePage.HomePage(self))
            self.destroy()
    def drawPage(self, data=None):
        self.place(x=0, y=0)

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("control/DongleNotificationFrame/image_1.png"))
        self.image_1 = self.create_image(
            566.0,
            89.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("control/DongleNotificationFrame/image_2.png"))
        self.image_2 = self.create_image(
            566.0,
            372.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("control/DongleNotificationFrame/image_3.png"))
        self.image_3 = self.create_image(
            567.0,
            372.0,
            image=self.image_image_3
        )

        self.inactive_reload = relative_to_assets(f"control/DongleNotificationFrame/{self.lang_code}/inactive_reload.png")
        self.active_reload = relative_to_assets(f"control/DongleNotificationFrame/{self.lang_code}/active_reload.png")

        self.reload_button = create_hover_button(self.window, 471.0, 493.0, 192.0, 54.0,
                            "#FFFFFF", self.inactive_reload, self.active_reload,
                            lambda: self.reloadDongle())

        self.create_text(
            1133 / 2.0,
            449.0,
            anchor="center",
            justify="center",
            text=self.data_localization["dongle_description"],
            fill="#14181F",
            font=("Nunito Regular", 14 * -1)
        )

        self.create_text(
            1133 / 2.0,
            405.0,
            anchor="center",
            justify="center",
            text=self.data_localization["dongle_title"],
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("control/DongleNotificationFrame/image_4.png"))
        self.image_4 = self.create_image(
            567.0,
            281.0,
            image=self.image_image_4
        )

        # Update the UI to ensure all elements are rendered
        self.window.update_idletasks()

        # self.window.after(2000, self.goToNextPage)  # Delay
        self.window.mainloop()
