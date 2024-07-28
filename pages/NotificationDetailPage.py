from tkinter import *
from colors import *
from helpers import *
# from notificationBar import notificationBar

from pages import HomePage, NotificationPage
from database.models.Notification import NotificationModel

import json

class NotificationDetailPage(Canvas, BasePage):

    def __init__(self, window, clicked_notification):
        self.window = window
        self.lang_code = json.loads(open("config.json", "r").read())["language"]
        self.clicked_notification = clicked_notification
        self.notification = NotificationModel()
        self.notification.mark_as_read(clicked_notification["id_notifikasi"])
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

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("control/NotificationDetailFrame/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("control/NotificationDetailFrame/image_2.png"))
        image_2 = self.create_image(
            572.0,
            335.0,
            image=self.image_image_2
        )

        self.create_text(
            75.9208984375,
            267.447265625,
            anchor="nw",
            width=1000,
            text=self.clicked_notification["notif_content"],
            fill="#404040",
            font=("Nunito SemiBold", 16 * -1)
        )

        self.create_text(
            75.9208984375,
            236.447265625,
            anchor="nw",
            text=self.clicked_notification["notif_subheader"],
            fill="#9E9E9E",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            924.0,
            192.447265625,
            anchor="nw",
            text=self.clicked_notification["notif_datetime"].strftime("%d %B %Y %H:%M"),
            fill="#9E9E9E",
            font=("Nunito Regular", 14 * -1)
        )

        self.create_text(
            75.9208984375,
            192.447265625,
            anchor="nw",
            text=self.clicked_notification["notif_header"],
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        inactive_button_1 = relative_to_assets(f"control/NotificationDetailFrame/{self.lang_code}/button_1.png")
        active_button_1 = relative_to_assets(f"control/NotificationDetailFrame/{self.lang_code}/active_button_1.png")

        create_hover_button(self, 471.0, 662.0, 192.0, 54.0,
                            BACKGROUND_COLOUR, inactive_button_1, active_button_1,
                            lambda: goToPage(self, NotificationPage.NotificationPage(self.window)))

        # self.window.mainloop()