from tkinter import *
from colors import *
from helpers import *

from pages import HomePage



class NotificationPage(Canvas, BasePage):

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

        image_image_1 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/image_1.png"))
        image_1 = self.create_image(
            565.0,
            201.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/image_2.png"))
        image_2 = self.create_image(
            565.0,
            367.3671875,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/image_3.png"))
        image_3 = self.create_image(
            565.0,
            498.896484375,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/image_4.png"))
        image_4 = self.create_image(
            93.3388671875,
            284.869140625,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/image_5.png"))
        image_5 = self.create_image(
            986.0,
            283.0,
            image=image_image_5
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/image_6.png"))
        image_6 = self.create_image(
            566.0,
            89.0,
            image=image_image_6
        )

        image_image_7 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/image_7.png"))
        image_7 = self.create_image(
            786.0,
            206.0,
            image=image_image_7
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=960.0,
            y=183.0,
            width=88.0,
            height=45.0
        )

        self.create_text(
            82.0,
            183.0,
            anchor="nw",
            text="Notifikasi",
            fill="#404040",
            font=("Nunito Bold", 25 * -1)
        )

        self.create_text(
            62.35595703125,
            274.894775390625,
            anchor="nw",
            text="Hari ini",
            fill="#404040",
            font=("Nunito Regular", 16 * -1)
        )

        self.create_text(
            75.51806640625,
            349.444091796875,
            anchor="nw",
            text="Subhead",
            fill="#9E9E9E",
            font=("Nunito Regular", 14 * -1)
        )

        self.create_text(
            75.51806640625,
            319.444091796875,
            anchor="nw",
            text="Weekly Maintenance",
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        self.create_text(
            75.51806640625,
            377.444091796875,
            anchor="nw",
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Iaculis tempus tellus adipiscing eget non arcu egestas elementum faucibus. Senectus cras nunc et, arcu ultricies tristique. Mi purus ut eget euismod orci, odio eu, non. Massa sapien magna volutpat lorem. Aliquet amet elit sed ac. ",
            fill="#404040",
            font=("Nunito SemiBold", 14 * -1)
        )

        self.create_text(
            75.51806640625,
            508.918212890625,
            anchor="nw",
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Iaculis tempus tellus adipiscing eget non arcu egestas elementum faucibus. Senectus cras nunc et, arcu ultricies tristique. Mi purus ut eget euismod orci, odio eu, non. Massa sapien magna volutpat lorem. Aliquet amet elit sed ac. ",
            fill="#404040",
            font=("Nunito SemiBold", 14 * -1)
        )

        self.create_text(
            75.51806640625,
            480.918212890625,
            anchor="nw",
            text="Subhead",
            fill="#404040",
            font=("Nunito Regular", 14 * -1)
        )

        self.create_text(
            75.51806640625,
            450.918212890625,
            anchor="nw",
            text="Model Update",
            fill="#404040",
            font=("Nunito Bold", 19 * -1)
        )

        image_image_8 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/image_8.png"))
        image_8 = self.create_image(
            1099.333251953125,
            22.33349609375,
            image=image_image_8
        )

        image_image_9 = PhotoImage(
            file=relative_to_assets("control/NotificationFrame/image_9.png"))
        image_9 = self.create_image(
            1074.0,
            22.33056640625,
            image=image_image_9
        )

        self.create_text(
            21.0,
            13.0,
            anchor="nw",
            text="9:41",
            fill="#FFFFFF",
            font=("SFProText Semibold", 15 * -1)
        )

        inactive_button_1 = relative_to_assets("control/NotificationFrame/button_1.png")
        active_button_1 = relative_to_assets("control/NotificationFrame/active_button_1.png")
        
        create_hover_button(self.window, 471.0, 662.0, 192.0, 54.0, 
                            BACKGROUND_COLOUR, inactive_button_1, active_button_1, 
                            lambda: goToPage(HomePage.HomePage(self.window)))
        

        self.window.mainloop()