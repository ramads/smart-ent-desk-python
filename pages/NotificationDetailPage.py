from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar

from pages import HomePage


class NotificationDetailPage(Canvas, BasePage):

    def __init__(self, window):
        self.window = window
        super().__init__(
            window,
            bg=BACKGROUND_COLOUR,
            height=744,
            width=1133,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

    def drawPage(self):
        self.place(x=0, y=0)

        # wifi_clock_app = notificationBar(self.window)

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/NotificationDetailFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("control/NotificationDetailFrame/image_2.png"))
        image_2 = self.create_image(
            572.0,
            335.0,
            image=image_image_2
        )

        self.create_text(
            75.9208984375,
            267.447265625,
            anchor="nw",
            width=1000,
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Iaculis tempus tellus adipiscing eget non arcu egestas elementum faucibus. Senectus cras nunc et, arcu ultricies tristique. Mi purus ut eget euismod orci, odio eu, non. Massa sapien magna volutpat lorem. Aliquet amet elit sed ac. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Iaculis tempus tellus adipiscing eget non arcu egestas elementum faucibus. Senectus cras nunc et, arcu ultricies tristique. Mi purus ut eget euismod orci, odio eu, non. Massa sapien magna volutpat lorem. Aliquet amet elit sed ac. \n\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Iaculis tempus tellus adipiscing eget non arcu egestas elementum faucibus. Senectus cras nunc et, arcu ultricies tristique. Mi purus ut eget euismod orci, odio eu, non. Massa sapien magna volutpat lorem. Aliquet amet elit sed ac. ",
            fill="#404040",
            font=("Nunito SemiBold", 16 * -1)
        )

        self.create_text(
            75.9208984375,
            236.447265625,
            anchor="nw",
            text="Subhead",
            fill="#9E9E9E",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            924.0,
            192.447265625,
            anchor="nw",
            text="Selasa, 16 April 2024",
            fill="#9E9E9E",
            font=("Nunito Regular", 14 * -1)
        )

        self.create_text(
            75.9208984375,
            192.447265625,
            anchor="nw",
            text="Weekly Maintenance",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        inactive_button_1 = relative_to_assets("control/NotificationDetailFrame/edit_button.png")
        active_button_1 = relative_to_assets("control/NotificationDetailFrame/active_button_1.png")

        create_hover_button(self.window, 471.0, 662.0, 192.0, 54.0,
                            BACKGROUND_COLOUR, inactive_button_1, active_button_1,
                            lambda: goToPage(HomePage.HomePage(self.window)))

        self.window.mainloop()