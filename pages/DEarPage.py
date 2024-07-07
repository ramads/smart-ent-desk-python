from tkinter import *
from colours import *
from helpers import *
from pages.DEarProcessPage import DEarProcessPage


class DEarPage(Canvas, BasePage):

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
            file=relative_to_assets("control/frame2/image_1.png"))
        image_1 = self.create_image(
            566.0,
            89.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("control/frame2/image_2.png"))
        image_2 = self.create_image(
            571.0,
            414.0,
            image=image_image_2
        )

        self.create_text(
            102.0,
            556.0,
            anchor="nw",
            text="Sebelum mengambil gambar silakan ambil Otoscope dan pastikan sudah diarahkan dengan benar.",
            fill="#14181F",
            font=("Nunito Regular", 19 * -1)
        )

        self.create_text(
            102.0,
            508.0,
            anchor="nw",
            text="Diagnosa Telinga",
            fill="#404040",
            font=("Nunito Bold", 24 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("control/frame2/button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=431.0,
            y=600.0,
            width=136.0,
            height=42.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("control/frame2/button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: goToPage(DEarProcessPage(self.window)),
            relief="flat"
        )
        button_2.place(
            x=575.0,
            y=600.0,
            width=136.0,
            height=42.0
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("control/frame2/image_3.png"))
        image_3 = self.create_image(
            568.0,
            326.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("control/frame2/image_4.png"))
        image_4 = self.create_image(
            1099.333251953125,
            22.33349609375,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("control/frame2/image_5.png"))
        image_5 = self.create_image(
            1074.0,
            22.33056640625,
            image=image_image_5
        )

        self.create_text(
            21.0,
            13.0,
            anchor="nw",
            text="9:41",
            fill="#FFFFFF",
            font=("SFProText Semibold", 15 * -1)
        )

        self.window.mainloop()